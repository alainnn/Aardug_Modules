# -*- coding: utf-8 -*-
##############################################################################
#
# Part of CaretCS <Caret Consulting Serivces (www.caretcs.com)>. See LICENSE file for full copyright and licensing details.
#
##############################################################################
{
    'name': 'Export Report for Partner & Invoice',
    'category': 'Hidden',
    'description': """
Add menus to export report for the Partner and Invoice in excel file""",
    'version': '9.0.1',
    'depends':['account','sale','sales_team'],
    'author': 'CaretCS',
    'website': "http://www.caretcs.com",
    'data' : [
        'views/partner_invoice_view.xml',
        'wizard/partner_wizard.xml',
        'wizard/account_invoice_wizard.xml',
    ],
    'auto_install': False,
    'installable': True,
}
