# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-today OpenERP SA (<http://www.openerp.com>)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from odoo import api, fields, models, _
from datetime import datetime, timedelta
from odoo.exceptions import UserError, ValidationError

class crm_lead(models.Model):
    _inherit = 'crm.lead'

    @api.multi
    def _track_subtype(self, init_values):
        self.ensure_one()
        if 'date_action' in init_values:
            return 'crm_sales_extend.mt_lead_next_action_date'
        elif 'title_action' in init_values:
            return 'crm_sales_extend.mt_lead_next_action'
        return super(crm_lead, self)._track_subtype(init_values)

    @api.model
    def _default_activity(self):
        ir_model_data = self.env['ir.model.data']
        return ir_model_data.get_object_reference('crm', 'crm_activity_data_call')[1]

    title_action = fields.Char('Next Action', track_visibility='onchange')
    date_action = fields.Datetime('Next Action Date', index=True, track_visibility='onchange', default=fields.Datetime.now)
    next_activity_id = fields.Many2one("crm.activity", string="Next Activity", index=True, default=_default_activity)

    @api.multi
    def write(self, values):
        if values.get('stage_id'):
            next_action_date = self.date_action
            #print "dates comparer**************",datetime.strptime(next_action_date, "%Y-%m-%d %H:%M:%S"),datetime.now()
            if next_action_date and (datetime.strptime(next_action_date, "%Y-%m-%d %H:%M:%S")+timedelta(seconds=30)) <= datetime.now():
                raise ValidationError(_('You cannot change stage which have action date is older then present date!'))
        res = super(crm_lead, self).write(values)
        return res

    @api.multi
    def crm_next_action_hour(self):
        if self.next_activity_id:
            if not self.next_activity_id.days:
                self.date_action =  datetime.now() + timedelta(hours=1)
            else:
                self.date_action = fields.Datetime.from_string(self.date_action) + timedelta(hours=1)

    @api.multi
    def crm_next_action_day(self):
        if self.next_activity_id:
            if not self.next_activity_id.days:
                self.date_action =  datetime.now() + timedelta(days=1)
            else:
                self.date_action =  fields.Datetime.from_string(self.date_action) + timedelta(days=1)

    @api.onchange('next_activity_id')
    def _onchange_next_activity_id(self):
        res = super(crm_lead, self)._onchange_next_activity_id()
        if self.next_activity_id:
            if not self.next_activity_id.days:
                self.date_action = fields.Datetime.to_string(datetime.now())
        return res