# -*- coding: utf-8 -*-
##############################################################################
#
# Part of Caret IT Solutions Pvt. Ltd. (Website: www.caretit.com).
# See LICENSE file for full copyright and licensing details.
#
##############################################################################

{
    'name': 'Resource Management',
    'summary': 'Resource, Projects and Tasks Management',
    'description': '''
        This module extends user experience for managing project, task and resources effectively.
    ''',
    'author': 'Caret IT Solutions Pvt. Ltd',
    'website': 'http://www.caretit.com',
    'category': 'Resource',
    'sequence': 11,
    'version': '10.0.0.1',
    'depends': ['base',
                'project_native',
                'hr_holidays_gantt_native',
                'google_calendar'],
    'data': [
        'security/ir.model.access.csv',
        'data/timesheet_cron.xml',
        'views/resource_management_template.xml',
        'views/view.xml',
        'wizard/summary.xml',
        'wizard/task_of_day.xml',
        'wizard/quick_task.xml'
    ],
    'js': ['static/src/js/resource_availability.js'],
    'qweb': [
        'static/src/xml/resource_availability_template.xml',
        'static/src/xml/resourse_dashboard.xml',
    ],
    'application': True,
}
