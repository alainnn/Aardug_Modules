# -*- coding: utf-8 -*-
##############################################################################
#
# Part of Caret IT <Caret IT Solutions Pvt. Ltd. (www.caretit.com)>. See LICENSE file for full copyright and licensing details.
#
##############################################################################
import datetime
import math
from odoo import api, fields, models, _
from odoo.exceptions import AccessError, Warning
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT

_MAP_issue_FIELDS = ['inactivity_days', 'day_close','days_since_creation']
_MAP_FIELDS_DATE = ['date_deadline']
_MAP_FIELDS_DATETIME = ['date_last_stage_update', 'create_date', 'date_action_last',
                        'date_action_next', 'date_closed','date_open','write_date',
                       'message_last_post', 'date_assign', 'date_start', 'date_end']
_MAP_COLORS = {
    'orange': 8,
    'red': 9,
    'green': 7,
    'purple': 6,
    'yellow': 5,
    'blue': 4,
}

class ProjectTask(models.Model):
    """ Project Task """
    _inherit = "project.task"

    @api.multi
    def write(self, vals):
        if 'stage_id' in vals:
            vals.update(remainder_mail=False, warning_mail=False)
        return super(ProjectTask, self).write(vals)

    remainder_mail = fields.Boolean(string='FollowUp Mail')
    warning_mail = fields.Boolean(string='Reminder Mail')

    @api.model
    def send_mail(self, custom):
        Mail = self.env['mail.mail']
        for rec in self:
            email_to =  rec.employee_id.work_email
            template = self.env['mail.compose.message'].generate_email_for_composer(custom.template_id.id, rec.id)
            vals = {'auto_delete': True, 'email_to': email_to, 'res_id':rec.id, 'model': rec._name, 'subject': template.get('subject'), 'body_html': template.get('body')}
            mail_id = Mail.create(vals)
            rec.message_post(body=_('sent mail is %s.') % (mail_id.body_html,))
            mail_id.send()
        return True 

    def compare_date(self, date, after_before, real_date):
        duration, unit = date.split('_')
        if(unit == "m"):
            return real_date + datetime.timedelta(minutes=int(duration))
        hours = int(duration) if unit == "h" else int(duration) * 24
        hours = hours * -1 if after_before == 'before' else hours * 1
        return real_date + datetime.timedelta(hours=hours)

    @api.model
    def email_send_stages(self):
        ProjectTaskType = self.env['project.task.type']
        MailMessage = self.env['mail.message']
        User = self.env['res.users']
        if not self.ids:
            rec_ids = self.search([])
            for rec in rec_ids.read():
                stage_id =  rec.get('stage_id')[0] if isinstance(rec.get('stage_id'), tuple) else rec.get('stage_id')
                task_browse = ProjectTaskType.browse(stage_id)
                for custom in task_browse.custom_ids:
                    when, field, send_mail , mail_action , custom_color, stage = custom.action_when, custom.action_perform_task, custom.send_mail , custom.mail_action, custom.action_color, custom.custom_type_id
                    value = rec.get(field)
                    if value:
                        if field in _MAP_FIELDS_DATETIME:
                            date = datetime.datetime.strptime(value, DEFAULT_SERVER_DATETIME_FORMAT)
                            date_to_compare = self.compare_date(custom.action_time, when, date)
                        else:
                            date = datetime.datetime.strptime(value, DEFAULT_SERVER_DATE_FORMAT)
                            date_to_compare = self.compare_date(custom.action_time, when, date)
                        current_date = datetime.datetime.now()
                        task = self.browse(rec.get('id'))
                        if (date >= current_date >= date_to_compare and when == "before") or (when == "after" and current_date >= date_to_compare):
                            if send_mail and mail_action=='remainder' and not rec['remainder_mail']:
                                task.send_mail(custom) 
                                task.remainder_mail = True
                            if send_mail and mail_action=='warning' and not rec['warning_mail']:
                                task.send_mail(custom) 
                                task.warning_mail = True

    @api.multi
    def read(self, fields=None, load='_classic_read'):
        records = super(ProjectTask, self).read(fields=fields, load=load)
        ProjectTaskType = self.env['project.task.type']
        def compare_date(date, after_before, real_date):
            duration, unit = date.split('_')
            if(unit == "m"):
                return real_date + datetime.timedelta(minutes=int(duration))
            hours = int(duration) if unit == "h" else int(duration) * 24
            hours = hours * -1 if after_before == 'before' else hours * 1
            return real_date + datetime.timedelta(hours=hours)
        for rec in records:
            stage_id =  rec.get('stage_id')[0] if isinstance(rec.get('stage_id'), tuple) else rec.get('stage_id')
            tasktype_browse = ProjectTaskType.browse(stage_id)
            if rec.get('color') in [4,5,6,7,8,9]:rec['color'] = 0
            for custom in tasktype_browse.custom_ids:
                # rec['color'] = _MAP_COLORS[custom.action_color]
                when, field = custom.action_when, custom.action_perform_task
                value = rec.get(field)
#                 rec['color'] = _MAP_COLORS[custom.action_color]
                if value:
                    if field in _MAP_FIELDS_DATETIME:
                        date = datetime.datetime.strptime(value, DEFAULT_SERVER_DATETIME_FORMAT)
                        date_to_compare = compare_date(custom.action_time, when, date)
                    else:
                        date = datetime.datetime.strptime(value, DEFAULT_SERVER_DATE_FORMAT)
                        date_to_compare = compare_date(custom.action_time, when, date)
                    current_date = datetime.datetime.now()
                    if (date >= current_date >= date_to_compare and when == "before") or (when == "after" and current_date >= date_to_compare):
                        rec['color'] = _MAP_COLORS[custom.action_color]
        return records


class ProjectTaskType(models.Model):
    _inherit = "project.task.type"

    custom_ids = fields.One2many('project.task.type.custom', 'custom_type_id', string='Kanban Custom')

class ProjectTaskTypeCustom(models.Model):
    _name = "project.task.type.custom"
    _order = 'priority desc'

    priority = fields.Integer(string='Priority', default=1, required=True)
    send_mail = fields.Boolean('Send mail')
    template_id = fields.Many2one('mail.template', string='Template')
    custom_type_id = fields.Many2one('project.task.type', string='Stage', required=True)
    action_when = fields.Selection([('before','Before'),('after','After')], string='Before/After', 
                                   required=True, default='before')
    mail_action = fields.Selection([('remainder','FollowUp Mail'),('warning','Reminder Mail')], string='Mail Action')
    custom_type = fields.Selection([('task', 'Task'), ('issue', 'Issue')], default='task', string="Type", required=True)
    action_time = fields.Selection([
                              ('1_m','1 Minute'),
                              ('5_m','5 Minutes'),
                              ('15_m','15 Minutes'),
                              ('30_m','30 Minutes'),
                              ('1_h','1 Hour'),
                              ('2_h','2 Hours'),
                              ('4_h','4 Hours'),
                              ('8_h','8 Hours'),
                              ('1_d','1 Day'),
                              ('2_d','2 Days'),
                              ('3_d','3 Days'),
                              ('4_d','4 Days'),
                              ('5_d','5 Days'),
                              ('6_d','6 Days'),
                              ('7_d','7 Days'),
                              ('10_d','10 Days'),
                              ('20_d','20 Days'),
                              ('30_d','30 Days'),
                              ('180_d','180 Days'),
                              ('365_d','365 Days'),], string='Time', required=True)
    action_color = fields.Selection([('orange', 'Orange'),
                                      ('red','Red'),
                                      ('green','Green'),
                                      ('purple','Purple'),
                                      ('yellow','Yellow'),
                                      ('blue','Blue')], string='Colors', required=True)
    action_perform_task = fields.Selection([('create_date','Creation Date'),
                                       ('write_date','Update Date'),
                                       ('date_start','Start Date'),
                                       ('date_end','End Date'),
                                       ('date_deadline','Expected Closing'),
                                       ('date_assign','Assigning Date'),
                                       ('date_last_stage_update','Last Stage Update'),
                                       ], string='Field')
    action_perform_issue = fields.Selection([('create_date','Creation Date'),
                                       ('write_date','Update Date'),
                                       ('date_closed','Closed Date'),
                                       ('date_deadline','Expected Closing'),
                                       ('date_action_last','Last Action'),
                                       ('date_action_next','Next Action'),
                                       ('date_last_stage_update','Last Stage Update'),
                                       ('days_since_creation','Days since creation date'),
                                       ('inactivity_days','Days since last action'),
                                       ('day_close','Days to Close'),
                                        ], string='Field')

    @api.one
    @api.constrains('action_time', 'action_perform_task', 'action_perform_issue')
    def _check_action_time(self):
        if (self.action_perform_task in _MAP_FIELDS_DATE or self.action_perform_issue in _MAP_FIELDS_DATE  or self.action_perform_issue in _MAP_issue_FIELDS) and self.action_time in ['1_m','5_m','15_m','30_m','1_h','2_h','4_h','8_h']:
            raise Warning(_('Misconfiguration, check Field and Time. Make sure time should be in days.'))

class ProjectIssue(models.Model):
    """ Project Issue """
    _inherit = "project.issue"

    @api.multi
    def write(self, vals):
        if 'stage_id' in vals:
            vals.update(remainder_mail=False, warning_mail=False)
        return super(ProjectIssue, self).write(vals)

    remainder_mail = fields.Boolean(string='FollowUp Mail')
    warning_mail = fields.Boolean(string='Reminder Mail')

    @api.model
    def send_mail(self, custom):
        Mail = self.env['mail.mail']
        for rec in self:
            email_to =  rec.email_from
            template = self.env['mail.compose.message'].generate_email_for_composer(custom.template_id.id, rec.id)
            vals = {'auto_delete': True, 'email_to': email_to, 'res_id': rec.id,'model': rec._name, 'subject': template.get('subject', "Hellozzzz"), 'body_html': template.get('body')}
            mail_id = Mail.create(vals)
            rec.message_post(body=_('sent mail is %s.') % (mail_id.body_html,))
            mail_id.send()
        return True 

    def compare_date(self, date, after_before, real_date):
        duration, unit = date.split('_')
        if(unit == "m"):
            return real_date + datetime.timedelta(minutes=int(duration))
        hours = int(duration) if unit == "h" else int(duration) * 24
        hours = hours * -1 if after_before == 'before' else hours * 1
        return real_date + datetime.timedelta(hours=hours)

    @api.model
    def email_send_stages(self):
        ProjectTaskType = self.env['project.task.type']
        MailMessage = self.env['mail.message']
        User = self.env['res.users']
        if not self.ids:
            rec_ids = self.search([])
            for rec in rec_ids.read():
                stage_id =  rec.get('stage_id')[0] if isinstance(rec.get('stage_id'), tuple) else rec.get('stage_id')
                task_browse = ProjectTaskType.browse(stage_id)
                for custom in task_browse.custom_ids:
                    allow_send_mail = False
                    date = datetime.datetime
                    date_to_compare = datetime.datetime
                    when, field, send_mail , mail_action , custom_color, stage = custom.action_when, custom.action_perform_issue, custom.send_mail , custom.mail_action, custom.action_color, custom.custom_type_id
                    value = rec.get(field)
                    if value:
                        if field in _MAP_issue_FIELDS:
                            if int(math.floor(value)) == int(custom.action_time.split('_')[0]):
                                allow_send_mail = True
                        if field in _MAP_FIELDS_DATETIME:
                            date = datetime.datetime.strptime(value, DEFAULT_SERVER_DATETIME_FORMAT)
                            date_to_compare = self.compare_date(custom.action_time, when, date)
                        elif field in _MAP_FIELDS_DATE:
                            date = datetime.datetime.strptime(value, DEFAULT_SERVER_DATE_FORMAT)
                            date_to_compare = self.compare_date(custom.action_time, when, date)
                        current_date = datetime.datetime.now()
                        issue = self.browse(rec.get('id'))
                        if (date >= current_date >= date_to_compare and when == "before") or (when == "after" and current_date >= date_to_compare) or allow_send_mail:
                            if send_mail and mail_action=='remainder' and not rec['remainder_mail']:
                                issue.send_mail(custom) 
                                issue.remainder_mail = True
                            if send_mail and mail_action=='warning' and not rec['warning_mail']:
                                issue.send_mail(custom) 
                                issue.warning_mail = True

    @api.multi
    def read(self, fields=None, load='_classic_read'):
        records = super(ProjectIssue, self).read(fields=fields, load=load)
        ProjectTaskType = self.env['project.task.type']
        def compare_date(date, after_before, real_date):
            duration, unit = date.split('_')
            if(unit == "m"):
                return real_date + datetime.timedelta(minutes=int(duration))
            hours = int(duration) if unit == "h" else int(duration) * 24
            hours = hours * -1 if after_before == 'before' else hours * 1
            return real_date + datetime.timedelta(hours=hours)
        for rec in records:
            stage_id =  rec.get('stage_id')[0] if isinstance(rec.get('stage_id'), tuple) else rec.get('stage_id')
            tasktype_browse = ProjectTaskType.browse(stage_id)
            if rec.get('color') in [6,7,8,9]:rec['color'] = 0
            for custom in tasktype_browse.custom_ids:
                change_color = False
                date = datetime.datetime
                date_to_compare = datetime.datetime
                # rec['color'] = _MAP_COLORS[custom.action_color]
                when, field = custom.action_when, custom.action_perform_issue
                value = rec.get(field)
#                 rec['color'] = _MAP_COLORS[custom.action_color]
                if value:
                    if field in _MAP_issue_FIELDS:
                        if int(math.floor(value)) == int(custom.action_time.split('_')[0]):
                            change_color = True
                    if field in _MAP_FIELDS_DATETIME:
                        date = datetime.datetime.strptime(value, DEFAULT_SERVER_DATETIME_FORMAT)
                        date_to_compare = compare_date(custom.action_time, when, date)
                    elif field in _MAP_FIELDS_DATE:
                        date = datetime.datetime.strptime(value, DEFAULT_SERVER_DATE_FORMAT)
                        date_to_compare = compare_date(custom.action_time, when, date)
                    current_date = datetime.datetime.now()
                    if (date >= current_date >= date_to_compare and when == "before") or (when == "after" and current_date >= date_to_compare) or change_color:
                        rec['color'] = _MAP_COLORS[custom.action_color]
        return records