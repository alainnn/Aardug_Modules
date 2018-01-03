# -*- coding: utf-8 -*-
##############################################################################
#
# Part of Caret IT Solutions Pvt. Ltd. (Website: www.caretit.com).
# See LICENSE file for full copyright and licensing details.
#
##############################################################################

from datetime import datetime, timedelta
from odoo import models, fields, api
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT as DTFORMAT


class Crm_Lead(models.Model):
    _inherit = "crm.lead"

    meeting_date = fields.Datetime(string="Meeting Date", help="Customer Meeting Start Date")
    note = fields.Text()

    @api.one
    def create_meeting(self):
        custName = ''
        address = ''
        phone = ''
        mobile = ''
        note = ''
        customer = self.partner_id
        stop = datetime.strptime(self.meeting_date, DTFORMAT) + timedelta(hours=1)
        if customer:
            if customer.name:
                custName = '\n'.join(['Customer Name:', customer.name])
            addressVal = '\n'.join(
                [x for x in [
                    customer.street,
                    customer.street2,
                    customer.city,
                    customer.zip,
                    customer.state_id.name if customer.state_id else '',
                    customer.country_id.name if customer.country_id else '']
                 if x])
            if addressVal:
                address = '\n'.join(['Address:', addressVal])
            if customer.phone:
                phone = '\n'.join(['Customer Phone:', customer.phone])
            if customer.mobile:
                mobile = '\n'.join(['Customer Mobile:', customer.mobile])
        if self.note:
            note = '\n'.join(['Opportunity Note:', self.note])

        description = '\n\n'.join(
            [x for x in [custName, address, phone, mobile, note] if x])
        meeting = {'name': self.name,
                   'start': self.meeting_date,
                   'stop': stop.strftime(DTFORMAT),
                   'opportunity_id': self.id,
                   'state': 'open',
                   'description': description}
        if self.user_id and self.user_id.partner_id:
            meeting.update({'partner_ids': [[6, False, [self.user_id.partner_id.id]]]})
        self.env['calendar.event'].create(meeting)

        activity = self.env['crm.activity'].search(
            [('name', '=', 'Meeting')], limit=1)
        stage = self.env['crm.stage'].search(
            [('name', '=', 'Appointment')], limit=1)

        if activity:
            self.next_activity_id = activity.id
            self.date_action = self.meeting_date
            self.title_action = activity.description
        if stage:
            self.stage_id = stage.id
