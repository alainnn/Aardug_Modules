import datetime
import pytz
from odoo import api, fields, models
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT as DTFORMAT
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT as DFORMAT

class QuickTask(models.Model):
    _name = "project.quick.task"
    _inherit = "project.task"

    def _get_default_partner(self):
        if 'default_project_id' in self.env.context:
            default_project_id = self.env['project.project'].browse(self.env.context['default_project_id'])
            return default_project_id.exists().partner_id

    name = fields.Char(string='Task Title', track_visibility='always', required=True, index=True)
    description = fields.Html(string='Description')
    date_start = fields.Datetime(string='Starting Date',default=fields.Datetime.now,index=True, copy=False)
    date_end = fields.Datetime(string='Ending Date', index=True, copy=False)
    project_id = fields.Many2one('project.project',
        string='Project',
        default=lambda self: self.env.context.get('default_project_id'),
        index=True,
        track_visibility='onchange',
        change_default=True)
    user_id = fields.Many2one('res.users',
        string='Assigned to',
        default=lambda self: self.env.uid,
        index=True, track_visibility='always')
    displayed_image_id = fields.Many2one('ir.attachment', domain="[('res_model', '=', 'project.task'), ('res_id', '=', id), ('mimetype', 'ilike', 'image')]", string='Displayed Image')
    partner_id = fields.Many2one('res.partner',
        string='Customer',
        default=_get_default_partner)
    sequence = fields.Integer(string='Sequence', index=True, default=10,
        help="Gives the sequence order when displaying a list of tasks.")
    company_id = fields.Many2one('res.company',
        string='Company',
        default=lambda self: self.env['res.company']._company_default_get())
    displayed_image_id = fields.Many2one('ir.attachment', domain="[('res_model', '=', 'project.task'), ('res_id', '=', id), ('mimetype', 'ilike', 'image')]", string='Displayed Image')


    @api.model
    def create(self, vals):
        task = super(QuickTask, self).create(vals)
        date_from = datetime.datetime.strptime(task.date_start, DTFORMAT)
        date_to = datetime.datetime.strptime(task.date_end, DTFORMAT)
        project_task = self.env['project.task']
        context_tz = pytz.timezone(self._context.get('tz') or self.env.user.tz or 'utc')
        delta = date_to - date_from
        for i in range(delta.days + 1):
            date_start_obj = datetime.datetime.combine((date_from + 
                datetime.timedelta(days=i)).date(), datetime.time(8))
            date_end_obj = datetime.datetime.combine((date_from + 
                datetime.timedelta(days=i)).date(),datetime.time(17))
            start = context_tz.localize(date_start_obj).astimezone(pytz.utc)
            end = context_tz.localize(date_end_obj).astimezone(pytz.utc)
            project_task.create({'name':task.name,
                                 'date_start':start,
                                 'date_end':end,
                                 'description':task.description,
                                 'project_id':task.project_id.id,
                                 'sequence': task.sequence,
                                 'company_id': task.company_id.id,
                                 'partner_id': task.partner_id.id,
                                 'displayed_image_id': task.displayed_image_id.id,
                                 })
        return task
