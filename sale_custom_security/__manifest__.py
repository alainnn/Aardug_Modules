# -*- coding: utf-8 -*-
##############################################################################
#
# Part of Caret IT Solutions Pvt. Ltd. (Website: www.caretit.com).
# See LICENSE file for full copyright and licensing details.
#
##############################################################################
{
    'name': 'Sale Custom Security',
    'description': """
        This module Provide security level for different kind users 
         
    """,
    'version': '1.0',
    'summary': """Put some access Rules on fields and module for different kind of users""",
    'author': 'Caret IT Solutions Pvt. Ltd.',
    'website': 'http://www.caretit.com ',
    'category': 'Security',
    'depends': ['base', 'sale_margin','product','hide_cost_price', 'stock_account'],
    'data': [
        'security/ir.model.access.csv',
        'views/custom_permission.xml'
    ],
    'images': [],
    'demo': [],
    'qweb': [],
    'installable': True,
    'auto_install': False,
}
