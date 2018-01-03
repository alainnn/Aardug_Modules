import datetime
import pytz
from odoo import api, fields, models
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT as DTFORMAT
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT as DFORMAT


class SummaryReport(models.Model):
    _name = "schedule.report"

    @api.model
    def get_default_dates(self):
        date = fields.Date.today()
        clickDate = self._context.get('click_date', None)
        if clickDate:
            clickDate = datetime.datetime.strptime(clickDate, DTFORMAT).date()
            date = clickDate.strftime(DFORMAT)
        return date

    date_from = fields.Date(string='Date From', default=get_default_dates)
    date_to = fields.Date(string='Date To', default=get_default_dates)
    schedule_ids = fields.Many2many('task.schedule', string='Schedule')

    @api.onchange('date_from', 'date_to')
    def fillTask(self):
        timezone = pytz.timezone(self._context.get('tz', False) or self.env.user.tz or 'UTC')
        d_frm = datetime.datetime.strptime(self.date_from, DFORMAT)
        d_frm = timezone.localize(d_frm).astimezone(pytz.utc).strftime(DTFORMAT)
        d_to = datetime.datetime.strptime(self.date_to, DFORMAT).replace(hour=23, minute=59)
        d_to = timezone.localize(d_to).astimezone(pytz.utc).strftime(DTFORMAT)

        cr = self.env.cr
        cr.execute("SELECT id FROM task_schedule "
                   "WHERE (date_start, date_end) OVERLAPS ('%s', '%s')" % (
                       d_frm, d_to))
        scheduleIds = [x[0] for x in cr.fetchall()]
        self.schedule_ids = self.env['task.schedule'].search(
            [('id', 'in', scheduleIds)]).ids