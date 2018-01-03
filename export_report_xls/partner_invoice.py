# -*- coding: utf-8 -*-
##############################################################################
#
# Part of CaretCS <Caret Consulting Serivces (www.caretcs.com)>. See LICENSE file for full copyright and licensing details.
#
##############################################################################

from odoo import models, fields, api, _
import datetime


class ResPartner(models.Model):
    _inherit = 'res.partner'

    export = fields.Boolean('Geexporteerd')
    export_date = fields.Date('Exportdatum')

class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    export = fields.Boolean('Geexporteerd')
    export_date = fields.Date('Exportdatum')

class AccountJournal(models.Model):
    _inherit = 'account.journal'

    ac_code = fields.Char('Accountview Code')

class AccountAccount(models.Model):
    _inherit = 'account.account'

    ac_code = fields.Char('Accountview Code')

