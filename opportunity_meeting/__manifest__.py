# -*- coding: utf-8 -*-
##############################################################################
#
# Part of Caret IT Solutions Pvt. Ltd. (Website: www.caretit.com).
# See LICENSE file for full copyright and licensing details.
#
##############################################################################

{
    'name': 'Opportunity Meeting',
    'version': '10.0.1.0.0',
    'description': """
        This module usage is Create a calendar meeting to sync with Google.
    """,
    'summary': 'Create a Opportunity Meeting For Calendar.',
    'category': 'CRM',
    'author': "Caret IT Solutions Pvt. Ltd.",
    'website': 'https://www.caretit.com',
    'depends': ['crm', 'google_calendar'],
    'data': ['data/stage_and_activity_demo.xml',
             'views/crm_meeting_view.xml'],
    'test': [],
    'installable': True,
    'auto_install': False,
}
