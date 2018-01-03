# -*- coding: utf-8 -*-
##############################################################################
#
# Part of Caret IT Solutions Pvt. Ltd. (Website: www.caretit.com).
# See LICENSE file for full copyright and licensing details.
#
##############################################################################

{
    'name': 'Crm Lead Caret',
    'version': '10.0',
    'author' : "Caret IT Solutions Pvt. Ltd.",
    'category': 'Sale, Crm',
    'summary': 'CRM, Sale',
    'website': 'http://caretit.com/',
    'description' : '''
        This module display partners all sale order in crm_lead 
        and display partners all leads in sale_order on button click''',
    'depends': ['sale', 'sale_crm'],
    'data': [
        'views/crm_lead_view.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': True,
}
