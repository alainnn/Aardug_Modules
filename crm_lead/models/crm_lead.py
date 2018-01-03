# -*- coding: utf-8 -*-
##############################################################################
#
# Part of Caret IT Solutions Pvt. Ltd. (Website: www.caretit.com).
# See LICENSE file for full copyright and licensing details.
#
##############################################################################


from odoo import api, fields, models, _


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    @api.depends('order_ids')
    def _compute_all_so(self):
        sale_obj = self.env['sale.order']
        for lead in self:
            sale_ids = sale_obj.search([('partner_id.id','=',lead.partner_id.id)])
            if sale_ids:
                nbr = 0
                company_currency = lead.company_currency or self.env.user.company_id.currency_id
                for order in sale_ids:
                    nbr += 1
                lead.all_so_count = nbr

    all_so_count = fields.Integer(compute='_compute_all_so', string='# of Sales Order')

    @api.multi
    def view_all_so(self):
        self.ensure_one()
        action = self.env.ref('crm_lead.act_res_partner_all_sale_order').read()[0]
        action['context'] = {
            'search_default_partner_id': self.partner_id and self.partner_id.id or False,
        }
        action['domain'] = [('partner_id','=',self.partner_id.id)]
        return action


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.depends('partner_id')
    def _compute_all_lead(self):
        lead_obj = self.env['crm.lead']
        for so in self:
            lead_ids = lead_obj.search([('partner_id.id','=',so.partner_id.id)])
            if lead_ids:
                nbr = 0
                company_currency = so.company_id.currency_id or self.env.user.company_id.currency_id
                for lead in lead_ids:
                    nbr += 1
                so.all_lead_count = nbr

    all_lead_count = fields.Integer(compute='_compute_all_lead', string='# of LEad')

    @api.multi
    def view_all_lead(self):
        self.ensure_one()
        action = self.env.ref('crm_lead.act_res_partner_all_lead').read()[0]
        action['context'] = {
            'search_default_partner_id': self.partner_id and self.partner_id.id or False,
        }
        action['domain'] = [('partner_id','=',self.partner_id.id)]
        return action