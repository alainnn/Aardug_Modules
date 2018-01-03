# -*- coding: utf-8 -*-

{
    'name': 'Create lead from fetched email\'s body content',
    'version': '10.0 community',
    'category': 'Customer Relationship Management',
    'sequence': 2,
    'summary': '',
    'description': """
This module enables automatic lead creation in v10 community from fetched email\'s body content using the server action
(created by this module).This server action need to be used in fetchmail configuration to enable automatic lead creation
from the body content.This module also sends an email to the generated lead's email address if there is any active outgoing 
email server configured,otherwise, it will have those emails in exception state under 'Setting/Technical/Email/Emails', 
which then can be send manually when any outgoing email server is configured.
""",
    'author': 'Caretcs',
    'website': 'http://caretcs.com',
    'depends': [
        'crm',
    ],
    'data': [
        'crm_action_rule_data.xml',
        'crm_lead_tree_view.xml'
    ],
    'demo': [
    ],
    'test': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'images': [],
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

