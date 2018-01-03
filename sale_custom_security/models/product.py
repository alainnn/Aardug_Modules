# -*- coding: utf-8 -*-

from odoo import api, fields, models, tools, _
import odoo.addons.decimal_precision as dp

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.depends('margin')
    def _compute_margin(self):
        if self.amount_untaxed > 0:
            margin_percentage = self.margin*100/self.amount_untaxed
            record_ids = self.env['sale.config.settings'].sudo().search([], order='id desc', limit=1)
            if margin_percentage <= record_ids.red_margin_upto:
                self.color = 'red'
            elif (margin_percentage > record_ids.red_margin_upto) and (margin_percentage <= record_ids.orange_margin_from):
                self.color = 'orange'
            elif margin_percentage > record_ids.orange_margin_from:
                self.color = 'green'

    color = fields.Char(string="Margin Color", compute=_compute_margin)

class SaleConfiguration(models.TransientModel):
    _inherit = 'sale.config.settings'

    @api.multi
    def _red_to_percentage_value(self):
        record_ids = self.search([],order='id desc', limit=1)
        return record_ids.red_margin_upto

    # @api.multi
    # def _orange_to_percentage_value(self):
    #     record_ids = self.search([],order='id desc', limit=1)
    #     return record_ids.orange_margin_to

    @api.multi
    def _orange_from_percentage_value(self):
        record_ids = self.search([],order='id desc', limit=1)
        return record_ids.orange_margin_from

    @api.multi
    def _green_from_percentage_value(self):
        record_ids = self.search([],order='id desc', limit=1)
        return record_ids.green_margin_from

    red_margin_upto = fields.Float(string="red margin UPTO", default=_red_to_percentage_value)
    # orange_margin_to = fields.Float(string="orange margin to", default=_orange_to_percentage_value)
    orange_margin_from = fields.Float(string="orange margin from", default=_orange_from_percentage_value)

    green_margin_from = fields.Float(string="green margin from", default=_green_from_percentage_value)

class ProductTemplate(models.Model):
    _inherit = 'product.template'


class ProductProduct(models.Model):
    _inherit = 'product.product'


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    @api.one
    @api.depends('price_unit')
    def _compute_price(self):
        self.price_unit_dummy = self.price_unit

    @api.one
    @api.depends('discount')
    def _compute_discount(self):
        self.discount_dummy = self.discount

    price_unit_dummy = fields.Float('Unit Price', compute=_compute_price, store=True)
    discount_dummy = fields.Float(
        string='Discount(%)', digits=dp.get_precision('Discount'),
        compute=_compute_discount, store=True)

    @api.onchange('discount')
    def _onchange_discount_dummy(self):
        self.discount_dummy = self.discount

    @api.onchange('price_unit')
    def _onchange_price(self):
        self.price_unit_dummy = self.price_unit

    @api.model
    def create(self,vals):
        return super(SaleOrderLine, self).create(vals)

    @api.multi
    def write(self,vals):
        return super(SaleOrderLine, self).write(vals)
