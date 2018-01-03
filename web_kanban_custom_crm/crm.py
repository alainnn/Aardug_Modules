import datetime
from odoo import api, fields, models, _
from odoo.exceptions import AccessError, Warning
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT
from odoo import SUPERUSER_ID


_MAP_FIELDS_DATE = ['date_action', 'date_deadline']
_MAP_FIELDS_DATETIME = ['create_date', 'date_action_last', 'date_action_next', 'date_closed',
                     'date_last_stage_update', 'date_open', 'message_last_post', 'write_date']
_MAP_COLORS = {
  'oranje': 8,
  'red': 9,
  'green': 7,
  'purple': 6,
}

class CrmLead(models.Model):
    """ CRM Lead Case """
    _inherit = "crm.lead"

    @api.multi
    def write(self, vals):
        if 'stage_id' in vals:
            vals.update(remainder_mail=False, warning_mail=False)
        return super(CrmLead, self).write(vals)

    remainder_mail = fields.Boolean(string='FollowUp Mail')
    warning_mail = fields.Boolean(string='Reminder Mail')

    @api.model
    def send_mail(self, custom):
        self.ensure_one()
        Mail = self.env['mail.mail']
        email_to =  self.email_from
        template = self.env['mail.compose.message'].generate_email_for_composer(custom.template_id.id, self.id)
        vals = {'auto_delete': True, 'email_to': email_to, 'subject': template.get('subject'), 'body_html': template.get('body')}
        mail_id = Mail.create(vals)
        Mail.send([mail_id])
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
        CrmStage = self.env['crm.stage']
        MailMessage = self.env['mail.message']
        User = self.env['res.users']
        if not self.ids:
            rec_ids = self.search([('type','=','opportunity')])
            # context = {'default_type':'opportunity'}
            for rec in rec_ids.read():
                stage_id =  rec.get('stage_id')[0] if isinstance(rec.get('stage_id'), tuple) else rec.get('stage_id')
                crm_browse = CrmStage.browse(stage_id)
                for custom in crm_browse.custom_ids:
                    when, field, send_mail , mail_action , custom_color, stage = custom.action_when, custom.action_perform, custom.send_mail , custom.mail_action, custom.action_color, custom.crm_stage_id
                    # mansi: check this

                    # value = rec.read([field, 'stage_id'])[0].get(field,'')
                    value = rec.get(field)
                    if value:
                        if field in _MAP_FIELDS_DATETIME:
                            date = datetime.datetime.strptime(value, DEFAULT_SERVER_DATETIME_FORMAT)
                            date_to_compare = self.compare_date(custom.action_time, when, date)
                        else:
                            date = datetime.datetime.strptime(value, DEFAULT_SERVER_DATE_FORMAT)
                            date_to_compare = self.compare_date(custom.action_time, when, date)
                        current_date = datetime.datetime.now()
                        opportunity = self.browse(rec.get('id'))
                        if (date >= current_date >= date_to_compare and when == "before") or (when == "after" and current_date >= date_to_compare):
                            if send_mail and mail_action=='remainder' and not rec['remainder_mail']:
                                opportunity.send_mail(custom) 
                                opportunity.remainder_mail = True
                            if send_mail and mail_action=='warning' and not rec['warning_mail']:
                                opportunity.send_mail(custom) 
                                opportunity.warning_mail = True


    @api.multi
    def read(self, fields=None, load='_classic_read'):
        records = super(CrmLead, self).read(fields=fields, load=load)
        crm_stage = self.env['crm.stage']
        def compare_date(date, after_before, real_date):
            duration, unit = date.split('_')
            if(unit == "m"):
                return real_date + datetime.timedelta(minutes=int(duration))
            hours = int(duration) if unit == "h" else int(duration) * 24
            hours = hours * -1 if after_before == 'before' else hours * 1
            return real_date + datetime.timedelta(hours=hours)
        # if self.env.context.get('default_type') and self.env.context.get('default_type') == "opportunity":
        for rec in records:
                stage_id =  rec.get('stage_id')[0] if isinstance(rec.get('stage_id'), tuple) else rec.get('stage_id')
                crm_browse = crm_stage.browse(stage_id)
                if rec.get('color') in [6,7,8,9]:rec['color'] = 0
                for custom in crm_browse.custom_ids:
                     # rec['color'] = _MAP_COLORS[custom.action_color]
                     when, field = custom.action_when, custom.action_perform
                     value = rec.get(field)
                     rec['color'] = _MAP_COLORS[custom.action_color]
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


class CrmStage(models.Model):
    """ CRM Lead Case """
    _inherit = "crm.stage"

    custom_ids = fields.One2many('crm.stage.custom', 'crm_stage_id', string='Kanban Custom')

class CrmStageCustom(models.Model):
    _name = "crm.stage.custom"
    _order = 'priority desc'

    priority = fields.Integer(string='Priority', default=1, required=True)
    send_mail = fields.Boolean('Send mail')
    template_id = fields.Many2one('mail.template', string='Template')
    crm_stage_id = fields.Many2one('crm.stage', string='Stage')
    action_when = fields.Selection([('before','Before'),('after','After')], string='Before/After', 
        required=True, default='before')
    mail_action = fields.Selection([('remainder','FollowUp Mail'),('warning','Reminder Mail')], string='Mail Action')
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
                              ('7_d','7 Days'),
                              ('10_d','10 Days'),
                              ('20_d','20 Days'),
                              ('30_d','30 Days'),
                              ('180_d','180 Days'),
                              ('365_d','365 Days'),], string='Time', required=True)
    action_color = fields.Selection([('oranje', 'Oranje'),
                                      ('red','Red'),
                                      ('green','Green'),
                                      ('purple','Purple')], string='Colors', required=True)
    action_perform = fields.Selection([('create_date','Creation Date'),
                                       ('date_action','Action Date'),
                                       ('date_action_last','Last Action'),
                                       ('date_action_next','Next Action'),
                                       ('date_closed','Closed'),
                                       ('date_deadline','Expected Closing'),
                                       ('date_last_stage_update','Last Stage Update'),
                                       ('date_open','Assigned'),
                                       ('message_last_post','Last Message Date'),
                                       ('write_date','Update Date'),
                                       ], string='Field', required=True)

    @api.one
    @api.constrains('action_time', 'action_perform')
    def _check_action_time(self):
        if self.action_perform in _MAP_FIELDS_DATE and self.action_time in ['1_m','5_m','15_m','30_m','1_h','2_h','4_h','8_h']:
            raise Warning(_('Misconfiguration, check Field and Time.'))