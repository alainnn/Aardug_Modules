# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Odoo Source Management Solution
#    Copyright (c) 2016 Caret Consulting Services (http://www.coftware.com)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
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
{
    'name' : 'CRM Sales Extend',
    'version' : '1.1',
    'author' : 'Caret Consulting Services',
    'category' : 'CRM',
    'description' : """
CRM Sales Team.
====================================
This module adds next action date by hour and Day
    """,
    'website': 'https://www.coftware.com',
    'images' : [],
    'depends' : ['crm'],
    'data': [
            'data.xml',
            'views/crm_lead_view_extend.xml'
        ],
    'qweb' : [],
    'demo': [],
    'test': [],
    'installable': True,
    'auto_install': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
