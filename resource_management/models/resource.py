# -*- coding: utf-8 -*-
##############################################################################
#
# Part of Caret IT Solutions Pvt. Ltd. (Website: www.caretit.com).
# See LICENSE file for full copyright and licensing details.
#
##############################################################################

import datetime
import dateutil
from datetime import timedelta, date
import pytz    # $ pip install pytz
from odoo import models, fields, api, _, modules, tools
from odoo.http import request
from odoo.exceptions import except_orm, ValidationError
import calendar
from dateutil.relativedelta import relativedelta, MO,SU


DTFORMAT = tools.DEFAULT_SERVER_DATETIME_FORMAT
DFORMAT = tools.DEFAULT_SERVER_DATE_FORMAT

class TaskOverviewDashboard(models.Model):
    _name = 'task.overview.dashboard'

    name = fields.Char('Name')

class Task(models.Model):
    _inherit = 'project.task'

    @api.model
    def _search(self, args, offset=0, limit=None, order=None,
        count=False, access_rights_uid=None):
        domain = []
        context = self.env.context.copy()
        start_dt = datetime.datetime.now().replace(hour=0, minute=0, second=0)
        end_dt = start_dt.replace(hour=23, minute=59, second=59)
        today = fields.date.today()
        
        # Week
        monday = (start_dt + relativedelta(weekday=MO(-1))).replace(hour=0, minute=0, second=0)
        next_monday = monday + relativedelta(weeks=+1)
        last_monday = monday + relativedelta(weeks=-1)
        sunday = (start_dt + relativedelta(weekday=SU(+1))).replace(hour=23, minute=59, second=59)
        next_sunday = sunday + relativedelta(weeks=+1)
        last_sunday = sunday + relativedelta(weeks=-1)

        # month
        first_day_this_month = (start_dt.replace(day=1)).replace(hour=0, minute=0, second=0)
        last_day_this_month = (datetime.datetime(start_dt.year,start_dt.month,1)+relativedelta(months=1,days=-1)).replace(hour=23, minute=59, second=59)
        next_month = start_dt + relativedelta(months=1)
        first_day_next_month = (next_month.replace(day=1)).replace(hour=0, minute=0, second=0)
        last_day_next_month = (datetime.datetime(next_month.year,next_month.month,1)+relativedelta(months=1,days=-1)).replace(hour=23, minute=59, second=59)
        last_month = start_dt + relativedelta(months=-1)
        first_day_last_month = (last_month.replace(day=1)).replace(hour=0, minute=0, second=0)
        last_day_last_month = (datetime.datetime(last_month.year,last_month.month,1)+relativedelta(months=1,days=-1)).replace(hour=23, minute=59, second=59)

        # days
        today_datetime = datetime.datetime.now()
        tomorrow_start_dt = (today_datetime + timedelta(days=1)).replace(hour=0, minute=0, second=0)
        tomorrow_end_dt = (today_datetime + timedelta(days=1)).replace(hour=23, minute=59, second=59)
        yester_start_dt = (today_datetime + timedelta(days=-1)).replace(hour=0, minute=0, second=0)
        yester_end_dt = (today_datetime + timedelta(days=-1)).replace(hour=23, minute=59, second=59)

        if context.get('today_planned_hours'):
            task_ids = self.env['task.schedule'].planned_hours_query(
                            start_dt, end_dt, qstatus='qsearch')
            
            domain = [('id','in',task_ids)]
        elif context.get('tomorrow_planned_hours'):
            task_ids = self.env['task.schedule'].planned_hours_query(
                            tomorrow_start_dt, tomorrow_end_dt, qstatus='qsearch')
            domain = [('id','in',task_ids)]
        elif context.get('this_week_planned_hours'):
            task_ids = self.env['task.schedule'].planned_hours_query(
                            monday, sunday, qstatus='qsearch')
            domain = [('id','in',task_ids)]
        elif context.get('next_week_planned_hours'):
            task_ids = self.env['task.schedule'].planned_hours_query(next_monday, next_sunday,
                            qstatus='qsearch')
            domain = [('id','in',task_ids)]
        elif context.get('this_month_planned_hours'):
            task_ids = self.env['task.schedule'].planned_hours_query(
                            first_day_this_month,
                            last_day_this_month,
                             qstatus='qsearch')
            domain = [('id','in',task_ids)]
        elif context.get('next_month_planned_hours'):
            task_ids = self.env['task.schedule'].planned_hours_query(
                            first_day_next_month, 
                            last_day_next_month, 
                            qstatus='qsearch')
            domain = [('id','in',task_ids)]
        elif context.get('yesterday_planned_hours'):
            task_ids = self.env['task.schedule'].planned_hours_query(
                            first_day_next_month, 
                            last_day_next_month, 
                            qstatus='qsearch')
            domain = [('id','in',task_ids)]
        elif context.get('last_week_planned_hours'):
            task_ids = self.env['task.schedule'].planned_hours_query(
                            first_day_next_month, 
                            last_day_next_month, 
                            qstatus='qsearch')
            domain = [('id','in',task_ids)]
        elif context.get('last_month_planned_hours'):
            task_ids = self.env['task.schedule'].planned_hours_query(
                            first_day_next_month, 
                            last_day_next_month, 
                            qstatus='qsearch')
            domain = [('id','in',task_ids)]
        elif context.get('yesterday_planned_hours'):
            task_ids = self.env['task.schedule'].planned_hours_query(
                            yester_start_dt, yester_end_dt,
                            qstatus='qsearch')
            domain = [('id','in',task_ids)]
        elif context.get('last_week_planned_hours'):
            task_ids = self.env['task.schedule'].planned_hours_query(
                            last_monday, last_sunday, 
                            qstatus='qsearch')
            domain = [('id','in',task_ids)]
        elif context.get('last_month_planned_hours'):
            task_ids = self.env['task.schedule'].planned_hours_query(
                            first_day_last_month,
                            last_day_last_month, 
                            qstatus='qsearch')
            domain = [('id','in',task_ids)]
        elif context.get('today_scheduled_hours'):
            task_ids = self.env['task.schedule'].scheduled_hours_query(
                            start_dt, end_dt, qstatus='qsearch')
            
            domain = [('id','in',task_ids)]
        elif context.get('tomorrow_scheduled_hours'):
            task_ids = self.env['task.schedule'].scheduled_hours_query(
                            tomorrow_start_dt, tomorrow_end_dt, qstatus='qsearch')
            domain = [('id','in',task_ids)]
        elif context.get('this_week_scheduled_hours'):
            task_ids = self.env['task.schedule'].scheduled_hours_query(
                            monday, sunday, qstatus='qsearch')
            domain = [('id','in',task_ids)]
        elif context.get('next_week_scheduled_hours'):
            task_ids = self.env['task.schedule'].scheduled_hours_query(next_monday, next_sunday,
                            qstatus='qsearch')
            domain = [('id','in',task_ids)]
        elif context.get('this_month_scheduled_hours'):
            task_ids = self.env['task.schedule'].scheduled_hours_query(
                            first_day_this_month,
                            last_day_this_month,
                             qstatus='qsearch')
            domain = [('id','in',task_ids)]
        elif context.get('next_month_scheduled_hours'):
            task_ids = self.env['task.schedule'].scheduled_hours_query(
                            first_day_next_month, 
                            last_day_next_month, 
                            qstatus='qsearch')
            domain = [('id','in',task_ids)]
        elif context.get('yesterday_scheduled_hours'):
            task_ids = self.env['task.schedule'].scheduled_hours_query(
                            yester_start_dt, yester_end_dt,
                            qstatus='qsearch')
            domain = [('id','in',task_ids)]
        elif context.get('last_week_scheduled_hours'):
            task_ids = self.env['task.schedule'].scheduled_hours_query(
                            last_monday, last_sunday, 
                            qstatus='qsearch')
            domain = [('id','in',task_ids)]
        elif context.get('last_month_scheduled_hours'):
            task_ids = self.env['task.schedule'].scheduled_hours_query(
                            first_day_last_month,
                            last_day_last_month, 
                            qstatus='qsearch')
            domain = [('id','in',task_ids)]
        elif context.get('today_task_needed'):
            task_ids = self.env['task.schedule'].task_needed_and_overplanned_query(
                            start_dt, end_dt, qstatus='qsearchneeded')
            
            domain = [('id','in',task_ids or ())]
        elif context.get('tomorrow_task_needed'):
            task_ids = self.env['task.schedule'].task_needed_and_overplanned_query(
                            tomorrow_start_dt, tomorrow_end_dt, qstatus='qsearchneeded')
            domain = [('id','in',task_ids or ())]
        elif context.get('this_week_task_needed'):
            task_ids = self.env['task.schedule'].task_needed_and_overplanned_query(
                            monday, sunday, qstatus='qsearchneeded')
            domain = [('id','in',task_ids or ())]
        elif context.get('next_week_task_needed'):
            task_ids = self.env['task.schedule'].task_needed_and_overplanned_query(next_monday, next_sunday,
                            qstatus='qsearchneeded')
            domain = [('id','in',task_ids or ())]
        elif context.get('this_month_task_needed'):
            task_ids = self.env['task.schedule'].task_needed_and_overplanned_query(
                            first_day_this_month,
                            last_day_this_month,
                             qstatus='qsearchneeded')
            domain = [('id','in',task_ids or ())]
        elif context.get('next_month_task_needed'):
            task_ids = self.env['task.schedule'].task_needed_and_overplanned_query(
                            first_day_next_month, 
                            last_day_next_month, 
                            qstatus='qsearchneeded')
        elif context.get('today_task_overplanned'):
            task_ids = self.env['task.schedule'].task_needed_and_overplanned_query(
                            start_dt, end_dt, qstatus='qsearchover')
            
            domain = [('id','in',task_ids or ())]
        elif context.get('tomorrow_task_overplanned'):
            task_ids = self.env['task.schedule'].task_needed_and_overplanned_query(
                            tomorrow_start_dt, tomorrow_end_dt, qstatus='qsearchover')
            domain = [('id','in',task_ids or ())]
        elif context.get('this_week_task_overplanned'):
            task_ids = self.env['task.schedule'].task_needed_and_overplanned_query(
                            monday, sunday, qstatus='qsearchover')
            domain = [('id','in',task_ids or ())]
        elif context.get('next_week_task_overplanned'):
            task_ids = self.env['task.schedule'].task_needed_and_overplanned_query(next_monday, next_sunday,
                            qstatus='qsearchover')
            domain = [('id','in',task_ids or ())]
        elif context.get('this_month_task_overplanned'):
            task_ids = self.env['task.schedule'].task_needed_and_overplanned_query(
                            first_day_this_month,
                            last_day_this_month,
                             qstatus='qsearchover')
            domain = [('id','in',task_ids or ())]
        elif context.get('next_month_task_overplanned'):
            task_ids = self.env['task.schedule'].task_needed_and_overplanned_query(
                            first_day_next_month, 
                            last_day_next_month, 
                            qstatus='qsearchover')
            domain = [('id','in',task_ids or ())]
        elif context.get('new_task'):
            task_ids = self.env['task.schedule'].no_of_task_query( 
                            qstatus='qsearch')
            domain = [('id','in',task_ids or ())]
        elif context.get('task_overdue'):
            task_ids = self.env['task.schedule'].task_overdue_query( 
                            qdate = today_datetime, qstatus='qsearch')
            domain = [('id','in',task_ids or ())]
        elif context.get('yesterday_realized_hours'):
            task_ids = self.env['task.schedule'].realized_hours_query(
                            yester_start_dt, yester_end_dt,
                            qstatus='qsearch')
            domain = [('id','in',task_ids)]
        elif context.get('last_week_realized_hours'):
            task_ids = self.env['task.schedule'].realized_hours_query(
                            last_monday, last_sunday, 
                            qstatus='qsearch')
            domain = [('id','in',task_ids)]
        elif context.get('last_month_realized_hours'):
            task_ids = self.env['task.schedule'].realized_hours_query(
                            first_day_last_month,
                            last_day_last_month, 
                            qstatus='qsearch')
            domain = [('id','in',task_ids)]
        elif context.get('next_week_realized_hours'):
            task_ids = self.env['task.schedule'].realized_hours_query(next_monday, next_sunday,
                            qstatus='qsearch')
            domain = [('id','in',task_ids)]
        elif context.get('this_month_realized_hours'):
            task_ids = self.env['task.schedule'].realized_hours_query(
                            first_day_this_month,
                            last_day_this_month,
                             qstatus='qsearch')
            domain = [('id','in',task_ids)]
        elif context.get('next_month_realized_hours'):
            task_ids = self.env['task.schedule'].realized_hours_query(
                            first_day_next_month, 
                            last_day_next_month, 
                            qstatus='qsearch')
            domain = [('id','in',task_ids)]

        if domain:
            args = args + domain
        return super(Task, self)._search(args=args, offset=offset, limit=limit, order=order,
            count=count, access_rights_uid=access_rights_uid)

    @api.multi
    def defClientEight(self):
        context_tz = pytz.timezone(self._context.get('tz') or
                                   self.env.user.tz or 'utc')
        start = datetime.datetime.combine(datetime.datetime.now().date(),
                                          datetime.time(8))
        return context_tz.localize(start).astimezone(pytz.utc)

    @api.multi
    def defClientSeventeen(self):
        context_tz = pytz.timezone(self._context.get('tz') or
                                   self.env.user.tz or 'utc')
        start = datetime.datetime.combine(datetime.datetime.now().date(),
                                          datetime.time(17))
        return context_tz.localize(start).astimezone(pytz.utc)

    @api.depends('schedule_ids.date_start', 'schedule_ids.date_end')
    def _computeScheduleHours(self):
        for task in self:
            hours = 0
            for schedule in task.schedule_ids:
                if schedule.resource_id.resource_type != 'user':
                    continue
                if isinstance(schedule.date_start, (str, unicode)):
                    start = datetime.datetime.strptime(
                        schedule.date_start, DTFORMAT)
                if isinstance(schedule.date_end, (str, unicode)):
                    end = datetime.datetime.strptime(
                        schedule.date_end, DTFORMAT)
                hours += ((end - start).seconds / 60) / 60.0
            task.hour_count = hours

    @api.depends('planned_hours', 'hour_count')
    def _plan_hours_get(self):
        for task in self:
            if (task.planned_hours > 0.0):
                task.to_plan_hours = round(
                    100.0 * (task.hour_count) / task.planned_hours, 2)
            else:
                task.to_plan_hours = 0.0

    resource_ids = fields.Many2many(
        'resource.resource', string='Team Members', track_visibility='always')
    schedule_ids = fields.One2many(
        'task.schedule', 'task_id', string='Schedule')
    auto_schedule = fields.Boolean(strin="Auto schedule", default=True)
    hour_count = fields.Float(string='Schedule Hours',
                              compute='_computeScheduleHours')
    notes_for_email = fields.Text()
    date_start = fields.Datetime(
        string="Starting Date", default=defClientEight)
    date_end = fields.Datetime(
        string="Ending Date", default=defClientSeventeen)
    to_plan_hours = fields.Float(
        compute='_plan_hours_get', string='To Plan hours')
    display_reschedule = fields.Boolean()

    resource_name = fields.Char("Name", compute='_computeResourceName')

    @api.depends('resource_ids')
    def _computeResourceName(self):
        for rec in self:
            name = []
            for resource in rec.resource_ids:
                name.append(resource.name)
            if name:
                # rec.resource_name = u' •' + u' •'.join(name)
                rec.resource_name = ', '.join(name)

    def kanban_selector(self):
        return {'name': _('Select Employee'),
                'view_mode': 'form',
                'res_model': 'resource.wizard',
                'type': 'ir.actions.act_window',
                'target': 'new'}

    # We are doing many work for dates. So not using constrains now.
    '''@api.one
    @api.constrains('schedule_ids')
    def dateCheck(self):
        for record in self.schedule_ids:
            if record.date_start > record.date_end:
                raise ValidationError('Error! Start date must be lower than '
                                      'end date')
            if record.date_end > self.date_end:
                raise ValidationError('Error! Assign date should be in between'
                                      ' task start date and end date')
            if record.date_start < self.date_start:
                raise ValidationError('Error! Assign date should be in between'
                                      ' task start date and end date')'''

    @api.model
    def leavesInPeriod(self, resource, start, end):
        cr = self.env.cr
        cr.execute("""
            SELECT id FROM resource_calendar_leaves
            WHERE  resource_id = '%s'
              AND (date_from, date_to) OVERLAPS ('%s', '%s')""" % (
            resource.id, start, end))
        data = cr.fetchall()
        return data

    @api.model
    def schedulesInPeriod(self, resource, start, end):
        cr = self.env.cr
        cr.execute("""
            SELECT id FROM task_schedule
            WHERE  resource_id = '%s'
              AND (date_start, date_end) OVERLAPS ('%s', '%s')""" % (
            resource.id, start, end))
        data = cr.fetchall()
        return data

    @api.model
    def getTzTimeForThisTime(self, dtime, tz):
        tzone = pytz.timezone(request.context.get('tz', 'utc') or 'utc')
        if dtime.tzinfo:
            return dtime.astimezone(tzone)
        else:
            dtime = dtime.replace(tzinfo=pytz.timezone('utc'))
        return dtime.astimezone(tzone)

    def manageSchedules(self, vals=None):
        if vals is None:
            vals = {}

        resourceChanged = 'resource_ids' in vals
        if not resourceChanged:
            return vals

        removedResources = list(set(self.resource_ids.ids) -
                                set(vals['resource_ids'][0][2]))
        addedResources = list(set(vals['resource_ids'][0][2]) -
                              set(self.resource_ids.ids))

        # Remove Schedules for removedResources
        self.env['task.schedule'].search(
            [('task_id', '=', self.id),
             ('resource_id', '=', removedResources)]).unlink()
        if addedResources:
            resources = self.env['resource.resource'].browse(addedResources)
        else:
            return vals

        # planMinutes = (self.planned_hours or 0.0) * 60
        # scheduledMinutes = 0.0

        # schedules = self.env['task.schedule'].search(
        #     [('task_id', '=', self.id)])

        # alreadyAllocatedMinutes = sum([(
        #     datetime.datetime.strptime(x.date_end, DTFORMAT) -
        #     datetime.datetime.strptime(x.date_start, DTFORMAT)).seconds / 60
        #     for x in schedules])
        # scheduledMinutes += alreadyAllocatedMinutes

        if not self.auto_schedule:
            return vals

        for resource in resources:
            if not resource.calendar_id:
                continue
            schedules = self.env['task.schedule'].search(
                [('resource_id', '=', resource.id), ('task_id', '=', self.id)])
            if schedules:
                continue

            start = datetime.datetime.strptime(self.date_start, DTFORMAT)
            end = datetime.datetime.strptime(self.date_end, DTFORMAT)
            # tz_info = pytz.timezone(self._context.get('tz') or 'utc')
            # start = start.replace(tzinfo=tz_info).astimezone(pytz.UTC).replace(tzinfo=None)
            # end = end.replace(tzinfo=tz_info).astimezone(pytz.UTC).replace(tzinfo=None)
            workingHrs = resource.calendar_id.get_working_hours(start, end)
            scheduleInterval = resource.calendar_id.schedule_hours(
                workingHrs, start, end)

            for sstart, send in scheduleInterval:
                if sstart > end:
                    continue
                if (send - sstart).seconds < 7200:
                    continue
                # if planMinutes and scheduledMinutes >= planMinutes:
                #     break
                if self.leavesInPeriod(resource, sstart, send):
                    continue
                if self.schedulesInPeriod(resource, sstart, send):
                    continue

                # if planMinutes:
                #     intervalDiffMinutes = (send - sstart).seconds / 60
                #     remainScheduleMinutes = planMinutes - scheduledMinutes
                #     if intervalDiffMinutes > remainScheduleMinutes:
                #         send = sstart + datetime.timedelta(
                #             minutes=remainScheduleMinutes)
                self.env['task.schedule'].create({
                    'name': self.name + ' (' + resource.name + ')',
                    'resource_id': resource.id,
                    'date_start': sstart,
                    'date_end': send,
                    'task_id': self.id})
                # scheduledMinutes += ((send - sstart).seconds) / 60

        return vals

    @api.multi
    def write(self, vals):
        if self.resource_ids and self.auto_schedule:
            startdt = 'date_start' in vals
            enddt = 'date_end' in vals
            if startdt or enddt:
                self.display_reschedule = True
        vals = self.manageSchedules(vals)
        return super(Task, self).write(vals)

    @api.multi
    def action_meeting_create(self):
        custName = ''
        address = ''
        phone = ''
        mobile = ''
        resources = ''
        note = ''
        for schedule in self.schedule_ids:
            event = schedule.meeting_id or None
            empNames = '\n'.join(
                [x.name for x in schedule.task_id.resource_ids])
            customer = schedule.task_id.partner_id
            notes = schedule.task_id.notes_for_email
            if customer:
                if customer.name:
                    custName = '\n'.join(['Customer Name:', customer.name])
                addressVal = '\n'.join(
                    [x for x in [
                        customer.street,
                        customer.street2,
                        customer.city,
                        customer.zip,
                        customer.state_id.name if customer.state_id else '',
                        customer.country_id.name if customer.country_id else ''
                    ] if x])
                if addressVal:
                    address = '\n' .join(['Address:', addressVal])
                if customer.phone:
                    phone = '\n'.join(['Customer Phone:', customer.phone])
                if customer.mobile:
                    mobile = '\n'.join(['Customer Mobile:', customer.mobile])
            if empNames:
                resources = '\n' .join(['Resources:', empNames])
            if notes:
                note = '\n' .join(['Note:', notes])

            description = '\n\n'.join(
                [x for x in [
                    custName, address, phone, mobile, resources, note] if x])
            vals = {'name': 'Task - %s' % schedule.task_id.name,
                    'start': schedule.date_start,
                    'stop': schedule.date_end,
                    'state': 'open',
                    'allday': False,
                    'partner_ids': [[6, False, [
                        schedule.resource_id.user_id.partner_id.id]]],
                    'resource_id': schedule.resource_id.id,
                    'description': description}
            if event:
                event.write(vals)
            else:
                event = self.env['calendar.event'].create(vals)
            schedule.write({'meeting_id': event.id})

    @api.multi
    def action_reschedule(self):
        self.schedule_ids.unlink()
        for resource in self.resource_ids:
            if not resource.calendar_id:
                continue

            start = datetime.datetime.strptime(self.date_start, DTFORMAT)
            end = datetime.datetime.strptime(self.date_end, DTFORMAT)
            workingHrs = resource.calendar_id.get_working_hours(start, end)
            scheduleInterval = resource.calendar_id.schedule_hours(
                workingHrs, start, end)

            for sstart, send in scheduleInterval:
                if sstart > end:
                    continue
                if (send - sstart).seconds < 7200:
                    continue
                if self.leavesInPeriod(resource, sstart, send):
                    continue
                if self.schedulesInPeriod(resource, sstart, send):
                    continue
                self.env['task.schedule'].create({
                    'name': self.name + ' (' + resource.name + ')',
                    'resource_id': resource.id,
                    'date_start': sstart,
                    'date_end': send,
                    'task_id': self.id})


class Resource(models.Model):
    _inherit = 'resource.resource'

    @api.model
    def _search(self, args, offset=0, limit=None, order=None,
        count=False, access_rights_uid=None):
        domain = []
        context = self.env.context.copy()
        start_dt = datetime.datetime.now().replace(hour=0, minute=0, second=0)
        end_dt = start_dt.replace(hour=23, minute=59, second=59)
        today = fields.date.today()
        
        # Week
        monday = (start_dt + relativedelta(weekday=MO(-1))).replace(hour=0, minute=0, second=0)
        next_monday = monday + relativedelta(weeks=+1)
        last_monday = monday + relativedelta(weeks=-1)
        sunday = (start_dt + relativedelta(weekday=SU(+1))).replace(hour=23, minute=59, second=59)
        next_sunday = sunday + relativedelta(weeks=+1)
        last_sunday = sunday + relativedelta(weeks=-1)

        # month
        first_day_this_month = (start_dt.replace(day=1)).replace(hour=0, minute=0, second=0)
        last_day_this_month = (datetime.datetime(start_dt.year,start_dt.month,1)+relativedelta(months=1,days=-1)).replace(hour=23, minute=59, second=59)
        next_month = start_dt + relativedelta(months=1)
        first_day_next_month = (next_month.replace(day=1)).replace(hour=0, minute=0, second=0)
        last_day_next_month = (datetime.datetime(next_month.year,next_month.month,1)+relativedelta(months=1,days=-1)).replace(hour=23, minute=59, second=59)
        last_month = start_dt + relativedelta(months=-1)
        first_day_last_month = (last_month.replace(day=1)).replace(hour=0, minute=0, second=0)
        last_day_last_month = (datetime.datetime(last_month.year,last_month.month,1)+relativedelta(months=1,days=-1)).replace(hour=23, minute=59, second=59)

        # days
        today_datetime = datetime.datetime.now()
        tomorrow_start_dt = (today_datetime + timedelta(days=1)).replace(hour=0, minute=0, second=0)
        tomorrow_end_dt = (today_datetime + timedelta(days=1)).replace(hour=23, minute=59, second=59)
        yester_start_dt = (today_datetime + timedelta(days=-1)).replace(hour=0, minute=0, second=0)
        yester_end_dt = (today_datetime + timedelta(days=-1)).replace(hour=23, minute=59, second=59)

        if context.get('today_resource_available'):
            task_ids = self.env['task.schedule'].resource_available_booked_query(
                            start_dt, end_dt, qstatus='qsearchav')
            
            domain = [('id','in',task_ids)]
        elif context.get('tomorrow_resource_available'):
            task_ids = self.env['task.schedule'].resource_available_booked_query(
                            tomorrow_start_dt, tomorrow_end_dt, qstatus='qsearchav')
            domain = [('id','in',task_ids)]
        elif context.get('this_week_resource_available'):
            task_ids = self.env['task.schedule'].resource_available_booked_query(
                            monday, sunday, qstatus='qsearchav')
            domain = [('id','in',task_ids)]
        elif context.get('next_week_resource_available'):
            task_ids = self.env['task.schedule'].resource_available_booked_query(next_monday, next_sunday,
                            qstatus='qsearchav')
            domain = [('id','in',task_ids)]
        elif context.get('this_month_resource_available'):
            task_ids = self.env['task.schedule'].resource_available_booked_query(
                            first_day_this_month,
                            last_day_this_month,
                             qstatus='qsearchav')
            domain = [('id','in',task_ids)]
        elif context.get('next_month_resource_available'):
            task_ids = self.env['task.schedule'].resource_available_booked_query(
                            first_day_next_month, 
                            last_day_next_month, 
                            qstatus='qsearchav')
            domain = [('id','in',task_ids)]
        elif context.get('today_resource_booked'):
            task_ids = self.env['task.schedule'].resource_available_booked_query(
                            start_dt, end_dt, qstatus='qsearchbook')
            
            domain = [('id','in',task_ids)]
        elif context.get('tomorrow_resource_booked'):
            task_ids = self.env['task.schedule'].resource_available_booked_query(
                            tomorrow_start_dt, tomorrow_end_dt, qstatus='qsearchbook')
            domain = [('id','in',task_ids)]
        elif context.get('this_week_resource_booked'):
            task_ids = self.env['task.schedule'].resource_available_booked_query(
                            monday, sunday, qstatus='qsearchbook')
            domain = [('id','in',task_ids)]
        elif context.get('next_week_resource_booked'):
            task_ids = self.env['task.schedule'].resource_available_booked_query(next_monday, next_sunday,
                            qstatus='qsearchbook')
            domain = [('id','in',task_ids)]
        elif context.get('this_month_resource_booked'):
            task_ids = self.env['task.schedule'].resource_available_booked_query(
                            first_day_this_month,
                            last_day_this_month,
                             qstatus='qsearchbook')
            domain = [('id','in',task_ids)]
        elif context.get('next_month_resource_booked'):
            task_ids = self.env['task.schedule'].resource_available_booked_query(
                            first_day_next_month, 
                            last_day_next_month, 
                            qstatus='qsearchbook')
            domain = [('id','in',task_ids)]

        if domain:
            args = args + domain
        return super(Resource, self)._search(args=args, offset=offset, limit=limit, order=order,
            count=count, access_rights_uid=access_rights_uid)

    @api.onchange('user_id')
    def onUserChange(self):
        if self.user_id and self.user_id.employee_ids:
            self.employee_id = self.user_id.employee_ids[0]
        else:
            self.employee_id = None


    @api.model
    def getTzTimeForThisTime(self, dtime):
        tzone = pytz.timezone(request.context.get('tz', 'utc') or 'utc')
        if dtime.tzinfo:
            return dtime.astimezone(tzone)
        else:
            dtime = dtime.replace(tzinfo=pytz.timezone('utc'))
        return dtime.astimezone(tzone)

    @api.multi
    def _compute_partial_timing(self):
        start = self._context.get('date_start', None)
        end = self._context.get('date_end', None)
        if start and end:
            for record in self:
                cr = self.env.cr
                cr.execute("""
                    SELECT date_start, date_end FROM task_schedule
                    WHERE resource_id = '%s'
                    AND (date_start, date_end) OVERLAPS ('%s', '%s')""" % (
                    record.id, start, end))
                occupied = cr.fetchall()
                '''cr.execute("""
                    SELECT date_from, date_to FROM resource_calendar_leaves
                    WHERE  resource_id = '%s'
                    AND (date_from, date_to) OVERLAPS ('%s', '%s')""" % (
                        record.id, start, end))
                leaves = cr.fetchall()
                data = occupied + leaves'''
                tzOccupied = []
                for start, end in occupied:
                    start = self.getTzTimeForThisTime(
                        datetime.datetime.strptime(
                            start, DTFORMAT)).replace(tzinfo=None)
                    end = self.getTzTimeForThisTime(
                        datetime.datetime.strptime(
                            end, DTFORMAT)).replace(tzinfo=None)
                    tzOccupied.append([start.strftime(DTFORMAT),
                                       end.strftime(DTFORMAT)])

                dataStr = ' • '.join([' to '.join([x[0][:-3], x[1][11:-3]])
                                      for x in tzOccupied])
                record.allocated_timing = dataStr

    @api.one
    @api.constrains('start_end_ids')
    def dateCheck(self):
        for record in self.start_end_ids:
            if record.start_date > record.end_date:
                raise ValidationError('Error! Start date must be lower than '
                                      'End date or same as End date')

    resource_image = fields.Binary('Photo', attachment=True)
    schedule_ids = fields.One2many(
        'task.schedule', 'resource_id', string='Schedule')
    duration = fields.Char(string='Duration')
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')
    allocated_timing = fields.Text(compute='_compute_partial_timing')
    str_category = fields.Char(compute='getCategoryNames')
    start_end_ids = fields.One2many(
        'resource.start_end', 'resource_id', string='Schedule')
    employee_id = fields.Many2one('hr.employee', string='Employee')
    category_ids = fields.Many2many(
        'hr.employee.category', related='employee_id.category_ids',
        string='Tags')

    @api.multi
    def getCategoryNames(self):
        for each in self:
            each.str_category = ', '.join([x.name for x in each.category_ids])

    '''@api.one
    def write(self, values):
        categ = values.get('category_ids', [])
        if len(categ) == 1 and len(categ[0]) == 3 and categ[0][2]:
            categs = self.env['hr.employee.category'].browse(categ[0][2])
            values['str_category'] = ', '.join([x.name for x in categs])
        return super(Resource, self).write(values)'''

    def kanban_done(self):
        return {'type': 'ir.actions.act_window_close', 'auto_refresh': '1'}

    @api.model
    def name_search(self, name, args=None, operator='ilike', limit=100):
        args = args or []
        context = self._context or {}
        if context.get('res_task_id'):
            task = self.env['project.task'].browse(context.get('res_task_id'))
            args += [('id', 'in', [t.id for t in task.resource_ids])]
        return super(Resource, self).name_search(
            name, args=args, operator=operator, limit=limit)

    @api.one
    def write(self, vals, context=None):
        if vals and 'user_id' in vals:
            user = self.user_id.browse(vals.get('user_id'))
            if user and user.employee_ids:
                vals['employee_id'] = user.employee_ids[0].id
            else:
                vals['employee_id'] = None
        return super(Resource, self).write(vals)


class ResourceWizard(models.TransientModel):
    _name = 'resource.wizard'

    # Performance Cache
    customCache = {'time': datetime.datetime.now().replace(second=00,
                                                           microsecond=00)}

    def _default_task(self):
        return self.env['project.task'].browse(self._context.get('active_id'))

    @api.depends('task_id')
    def _default_selected_resources(self):
        return self.task_id.resource_ids

    @api.model
    def getActiveTask(self):
        if self._context.get('active_id'):
            task = self.env['project.task'].browse(
                self._context.get('active_id'))
        else:
            task = self.task_id
        return task

    @api.model
    def getStartEnd(self):
        return (self._context.get('date_start', self.date_start),
                self._context.get('date_end', self.date_end))

    @api.model
    def getTzTimeForThisTime(self, dtime, tz):
        tzone = pytz.timezone(request.context.get('tz', 'utc') or 'utc')
        if dtime.tzinfo:
            return dtime.astimezone(tzone)
        else:
            dtime = dtime.replace(tzinfo=pytz.timezone('utc'))
        return dtime.astimezone(tzone)

    @api.model
    def isResourcePresent(self, resource, start, end):
        if isinstance(start, str) or isinstance(start, unicode):
            start = datetime.datetime.strptime(start, DTFORMAT)
        if isinstance(end, str) or isinstance(end, unicode):
            end = datetime.datetime.strptime(end, DTFORMAT)
        if (end - start).total_seconds() > 365 * 24 * 60 * 60:
            raise except_orm(
                _('User Error!'),
                _('User should not auto schedule task for many days.'))
        start = self.getTzTimeForThisTime(start, 'UTC').replace(tzinfo=None)
        end = self.getTzTimeForThisTime(end, 'UTC').replace(tzinfo=None)
        schedule = resource.calendar_id.get_working_hours(
            start, end, compute_leaves=True, resource_id=resource.id)
        return bool(schedule)

    @api.model
    def leavesInPeriod(self, resource, start, end):
        cr = self.env.cr
        cr.execute("""
            SELECT id FROM resource_calendar_leaves
            WHERE  resource_id = '%s'
              AND (date_from, date_to) OVERLAPS ('%s', '%s')""" % (
            resource.id, start, end))
        data = cr.fetchall()
        return data

    @api.model
    def schedulesInPeriod(self, resource, start, end):
        cr = self.env.cr
        cr.execute("""
            SELECT id FROM task_schedule
            WHERE  resource_id = '%s'
              AND (date_start, date_end) OVERLAPS ('%s', '%s')""" % (
            resource.id, start, end))
        data = cr.fetchall()
        return data

    @api.model
    def isFullOccupied(self, resource, start, end):
        if isinstance(start, str) or isinstance(start, unicode):
            start = datetime.datetime.strptime(start, DTFORMAT)
        if isinstance(end, str) or isinstance(end, unicode):
            end = datetime.datetime.strptime(end, DTFORMAT)

        dayHours = (end - start).days * 24
        floatHours = ((end - start).seconds / 60) / 60
        diffHours = dayHours + floatHours
        possibleIntervals = resource.calendar_id.schedule_hours(
            diffHours, start, resource_id=2)

        possibleWorkSloat = 0
        occupiedStatusForSloat = []
        for pstart, pend in possibleIntervals:
            if pstart > end:
                break
            possibleWorkSloat += 1
            if not self.isResourcePresent(resource, start, end):
                occupiedStatusForSloat.append(True)
            elif self.schedulesInPeriod(resource, pstart, pend):
                occupiedStatusForSloat.append(True)
            elif self.leavesInPeriod(resource, pstart, pend):
                occupiedStatusForSloat.append(True)
            else:
                occupiedStatusForSloat.append(False)
                break

        if possibleWorkSloat == len([x for x in occupiedStatusForSloat if x]):
            return True
        else:
            return False

    @api.model
    def getAllResources(self, start, end):
        """Responsible for considering all valid resources."""
        possible_lines = self.env['resource.start_end'].search(
            [('start_date', '<=', start), ('end_date', '>=', end)]).ids
        resoDomain = [('calendar_id', '!=', False),
                      ('start_end_ids', 'in', possible_lines)]
        if self.type_material and not self.type_user:
            resoDomain.append(('resource_type', '=', 'material'))
        if self.type_user and not self.type_material:
            resoDomain.append(('resource_type', '=', 'user'))
        if self.category_ids:
            resoDomain.append(('category_ids', 'in', self.category_ids.ids))
        return self.env['resource.resource'].search(resoDomain)

    @api.model
    def getResources(self):
        """Responsible for finding partial available resources."""
        start, end = self.getStartEnd()
        if (not start) or (not end):
            return None, None, None, None

        if (not self.type_user) and (not self.type_material):
            return None, None, None, None

        '''
        # Cannot use cache. Requirement from Arjan to use filter.
        if (self.customCache.get('time', None) ==
                datetime.datetime.now().replace(second=00, microsecond=00)):
            data = self.customCache.get('getResources' + start + end, None)
            if data:
                return data
        else:
            self.customCache = {'time': datetime.datetime.now().replace(
                second=00, microsecond=00)}
        '''

        available = []
        partialAvailable = []
        notAvailabale = []

        allResources = self.getAllResources(start, end)

        applicableForPartial = []
        for resource in allResources:
            if not self.isResourcePresent(resource, start, end):
                notAvailabale.append(resource.id)
                continue
            if self.leavesInPeriod(resource, start, end):
                applicableForPartial.append(resource)
            elif self.schedulesInPeriod(resource, start, end):
                applicableForPartial.append(resource)
            else:
                available.append(resource.id)

        for resource in applicableForPartial:
            if self.isFullOccupied(resource, start, end):
                notAvailabale.append(resource.id)
            else:
                partialAvailable.append(resource.id)

        # Cannot use cache. Requirement from Arjan to use filter.
        # self.customCache['getResources' + start + end] = (
        #     allResources, available, partialAvailable, notAvailabale)

        return allResources, available, partialAvailable, notAvailabale

    @api.depends('selected_resource_ids')
    def _default_avail_resources(self):
        _, allAvail, _, _ = self.getResources()
        if allAvail is None:
            return
        task = self.getActiveTask()
        avail = list(set(allAvail) - set(task.resource_ids.ids))
        return avail

    @api.depends('selected_resource_ids')
    def _default_partial_resources(self):
        _, _, allPart, _ = self.getResources()
        if allPart is None:
            return
        task = self.getActiveTask()
        part = list(set(allPart) - set(task.resource_ids.ids))
        return part

    @api.depends('selected_resource_ids')
    def _default_not_avail_resources(self):
        _, _, _, allNot = self.getResources()
        if allNot is None:
            return
        task = self.getActiveTask()
        notavail = list(set(allNot) - set(task.resource_ids.ids))
        return notavail

    @api.onchange('selected_resource_ids')
    def _change_selected(self):
        self._manageResource(event='selected_resource_ids')

    @api.onchange('avail_resource_ids')
    def _change_avail(self):
        self._manageResource(event='avail_resource_ids')

    @api.onchange('partial_resource_ids')
    def _change_partial(self):
        self._manageResource(event='partial_resource_ids')

    @api.onchange('not_avail_resource_ids')
    def _change_notavail(self):
        self._manageResource(event='not_avail_resource_ids')

    @api.onchange('category_ids', 'type_material', 'type_user')
    def _change_category(self):
        self._manageResource(event='category_ids')

    def _manageResource(self, event=None):
        resoObj = self.env['resource.resource']
        start, end = self.getStartEnd()
        if (not start) or (not end):
            return

        allRes, allAvail, allPart, allNot = self.getResources()
        allres = allRes.ids if allRes else []
        avail = self.avail_resource_ids.ids
        selected = self.selected_resource_ids.ids
        notavail = self.not_avail_resource_ids.ids
        partial = self.partial_resource_ids.ids

        if event in ['avail_resource_ids', 'partial_resource_ids',
                     'not_avail_resource_ids']:  # Select Resource
            finalSelected = selected + list(
                set(allres) - set(avail) - set(partial) - set(notavail)
            )
            self.selected_resource_ids = resoObj.browse(finalSelected)
        elif event in ['selected_resource_ids']:  # Deselect Resource
            deselected = list(
                set(allres) - set(avail) - set(partial) -
                set(notavail) - set(selected)
            )
            if allAvail:
                addToAvail = [x for x in deselected if x in allAvail]
                self.avail_resource_ids = resoObj.browse(list(set(
                    self.avail_resource_ids.ids + addToAvail)))
            if allPart:
                addToPart = [x for x in deselected if x in allPart]
                self.partial_resource_ids = resoObj.browse(list(set(
                    self.partial_resource_ids.ids + addToPart)))
                self.partial_resource_ids._compute_partial_timing()
            if allNot:
                addToNot = [x for x in deselected if x in allNot]
                self.not_avail_resource_ids = resoObj.browse(list(set(
                    self.not_avail_resource_ids.ids + addToNot)))
        elif event in ['category_ids']:  # Filter Used
            selectedFilter = (
                set(self.task_id.resource_ids.ids).union(set(selected))
            ).intersection(set(allres))
            self.selected_resource_ids = resoObj.browse(list(selectedFilter))
            self.avail_resource_ids = resoObj.browse(list(
                set(allAvail or []).intersection(set(allres)) - selectedFilter
            ))
            self.partial_resource_ids = resoObj.browse(list(
                set(allPart or []).intersection(set(allres)) - selectedFilter
            ))
            self.not_avail_resource_ids = resoObj.browse(list(
                set(allNot or []).intersection(set(allres)) - selectedFilter
            ))

    task_id = fields.Many2one(
        'project.task', string='Task', required=True, default=_default_task)
    date_start = fields.Datetime(
        string='Start Date', related='task_id.date_start')
    date_end = fields.Datetime(
        string='Start Date', related='task_id.date_end')
    avail_resource_ids = fields.Many2many('resource.resource',
                                          string='Resources',
                                          default=_default_avail_resources)
    partial_resource_ids = fields.Many2many('resource.resource',
                                            string='Resources',
                                            default=_default_partial_resources)
    not_avail_resource_ids = fields.Many2many(
        'resource.resource', string='Resources',
        default=_default_not_avail_resources)
    selected_resource_ids = fields.Many2many(
        'resource.resource', string='Selected Resources',
        related='task_id.resource_ids', default=_default_selected_resources)
    category_ids = fields.Many2many('hr.employee.category', string='Tags')
    type_user = fields.Boolean(string='Human', default=True)
    type_material = fields.Boolean(string='Material', default=True)

    @api.multi
    def save_window_close(self):
        # self.task_id.action_meeting_create()
        return {'type': 'ir.actions.act_window_close', 'auto_refresh': '1'}


class ResourceSchedule(models.Model):
    _name = 'task.schedule'

    @api.model
    def _search(self, args, offset=0, limit=None, order=None,
        count=False, access_rights_uid=None):
        domain = []
        context = self.env.context.copy()
        start_dt = datetime.datetime.now().replace(hour=0, minute=0, second=0)
        end_dt = start_dt.replace(hour=23, minute=59, second=59)
        today = fields.date.today()
        
        # Week
        monday = (start_dt + relativedelta(weekday=MO(-1))).replace(hour=0, minute=0, second=0)
        next_monday = monday + relativedelta(weeks=+1)
        last_monday = monday + relativedelta(weeks=-1)
        sunday = (start_dt + relativedelta(weekday=SU(+1))).replace(hour=23, minute=59, second=59)
        next_sunday = sunday + relativedelta(weeks=+1)
        last_sunday = sunday + relativedelta(weeks=-1)

        # month
        first_day_this_month = (start_dt.replace(day=1)).replace(hour=0, minute=0, second=0)
        last_day_this_month = (datetime.datetime(start_dt.year,start_dt.month,1)+relativedelta(months=1,days=-1)).replace(hour=23, minute=59, second=59)
        next_month = start_dt + relativedelta(months=1)
        first_day_next_month = (next_month.replace(day=1)).replace(hour=0, minute=0, second=0)
        last_day_next_month = (datetime.datetime(next_month.year,next_month.month,1)+relativedelta(months=1,days=-1)).replace(hour=23, minute=59, second=59)
        last_month = start_dt + relativedelta(months=-1)
        first_day_last_month = (last_month.replace(day=1)).replace(hour=0, minute=0, second=0)
        last_day_last_month = (datetime.datetime(last_month.year,last_month.month,1)+relativedelta(months=1,days=-1)).replace(hour=23, minute=59, second=59)

        # days
        today_datetime = datetime.datetime.now()
        tomorrow_start_dt = (today_datetime + timedelta(days=1)).replace(hour=0, minute=0, second=0)
        tomorrow_end_dt = (today_datetime + timedelta(days=1)).replace(hour=23, minute=59, second=59)
        yester_start_dt = (today_datetime + timedelta(days=-1)).replace(hour=0, minute=0, second=0)
        yester_end_dt = (today_datetime + timedelta(days=-1)).replace(hour=23, minute=59, second=59)

        if context.get('today_double_booked'):
            resource_ids = self.double_booked_query(
                            start_dt, end_dt, qstatus='qsearch')
            
            domain = [('id','in',resource_ids)]
        elif context.get('tomorrow_double_booked'):
            resource_ids = self.double_booked_query(
                            tomorrow_start_dt, tomorrow_end_dt, qstatus='qsearch')
            domain = [('id','in',resource_ids)]
        elif context.get('this_week_double_booked'):
            resource_ids = self.double_booked_query(
                            monday, sunday, qstatus='qsearch')
            domain = [('id','in',resource_ids)]
        elif context.get('next_week_double_booked'):
            resource_ids = self.double_booked_query(next_monday, next_sunday,
                            qstatus='qsearch')
            domain = [('id','in',resource_ids)]
        elif context.get('this_month_double_booked'):
            resource_ids = self.double_booked_query(
                            first_day_this_month,
                            last_day_this_month,
                             qstatus='qsearch')
            domain = [('id','in',resource_ids)]
        elif context.get('next_month_double_booked'):
            resource_ids = self.double_booked_query(
                            first_day_next_month, 
                            last_day_next_month, 
                            qstatus='qsearch')
            domain = [('id','in',resource_ids)]
        elif context.get('today_not_linked'):
            resource_ids = self.not_linked_query(
                            start_dt, end_dt, qstatus='qsearch')
            
            domain = [('id','in',resource_ids)]
        elif context.get('tomorrow_not_linked'):
            resource_ids = self.not_linked_query(
                            tomorrow_start_dt, tomorrow_end_dt, qstatus='qsearch')
            domain = [('id','in',resource_ids)]
        elif context.get('this_week_not_linked'):
            resource_ids = self.not_linked_query(
                            monday, sunday, qstatus='qsearch')
            domain = [('id','in',resource_ids)]
        elif context.get('next_week_not_linked'):
            resource_ids = self.not_linked_query(next_monday, next_sunday,
                            qstatus='qsearch')
            domain = [('id','in',resource_ids)]
        elif context.get('this_month_not_linked'):
            resource_ids = self.not_linked_query(
                            first_day_this_month,
                            last_day_this_month,
                             qstatus='qsearch')
            domain = [('id','in',resource_ids)]
        elif context.get('next_month_not_linked'):
            resource_ids = self.not_linked_query(
                            first_day_next_month, 
                            last_day_next_month, 
                            qstatus='qsearch')
            domain = [('id','in',resource_ids)]
        

        if domain:
            args = args + domain
        return super(ResourceSchedule, self)._search(args=args, offset=offset, limit=limit, order=order,
            count=count, access_rights_uid=access_rights_uid)

    @api.model
    def create(self, vals):
        result = super(ResourceSchedule, self).create(vals)
        if not result.name:
            result.name = result.task_id.name + ' (' + result.resource_id.name + ')'
        if result.task_id:
            result.task_id.action_meeting_create()
        return result

    @api.model
    def timesheet_create(self):
        todayDate = datetime.datetime.today()
        schedules = self.env['task.schedule'].search([
            ('date_start', '<', str(todayDate))])
        hours = 0
        for schedule in schedules:
            timesheet = schedule.timesheet_id or None
            if isinstance(schedule.date_start, (str, unicode)):
                start = datetime.datetime.strptime(
                    schedule.date_start, DTFORMAT)
            if isinstance(schedule.date_end, (str, unicode)):
                end = datetime.datetime.strptime(
                    schedule.date_end, DTFORMAT)
            hours = ((end - start).seconds / 60) / 60.0
            vals = {
                'name': schedule.task_id.name,
                'date': start,
                'user_id': schedule.resource_id.user_id.id,
                'task_id': schedule.task_id.id,
                'unit_amount': hours,
                'project_id': schedule.task_id.project_id.id,
                'schedule_id': schedule.id,
                }
            if timesheet:
                timesheet.write(vals)
            else:
                timesheet = self.env['account.analytic.line'].create(vals)
            schedule.write({'timesheet_id': timesheet.id})
            if start < todayDate:
                schedule.write({'locked': True})
            date = datetime.datetime.strptime(timesheet.date, DFORMAT)
            if timesheet.schedule_id and date < todayDate:
                timesheet.write({'locked': True})
                
    @api.multi
    def write(self, vals):
        if vals and self.meeting_id:
            task = vals.get('task_id')
            resource = vals.get('resource_id')
            start = vals.get('date_start')
            end = vals.get('date_end')
            if task and resource:
                res = self.resource_id.browse(resource)
                taskName = self.task_id.browse(task)
                self.name = taskName.name + ' (' + res.name + ')'
                self.meeting_id.write({
                    'partner_ids': [[6, False, [res.user_id.partner_id.id]]],
                    'resource_id': res.id,
                    'name': 'Task - %s' % taskName.name
                })
            if not task and resource:
                res = self.resource_id.browse(resource)
                self.name = self.task_id.name + ' (' + res.name + ')'
                self.meeting_id.write({
                    'partner_ids': [[6, False, [res.user_id.partner_id.id]]],
                    'resource_id': res.id
                })
            if not resource and task:
                taskName = self.task_id.browse(task)
                self.name = taskName.name + ' (' + self.resource_id.name + ')'
                self.meeting_id.write({'name': 'Task - %s' % taskName.name})
            self.meeting_id.write({'start': start or self.date_start,
                                   'stop': end or self.date_end})
        return super(ResourceSchedule, self).write(vals)

    @api.multi
    def defClientEight(self):
        context_tz = pytz.timezone(self._context.get('tz') or
                                   self.env.user.tz or 'utc')
        start = datetime.datetime.combine(datetime.datetime.now().date(),
                                          datetime.time(8))
        return context_tz.localize(start).astimezone(pytz.utc)

    @api.multi
    def defClientTwelve(self):
        context_tz = pytz.timezone(self._context.get('tz') or
                                   self.env.user.tz or 'utc')
        start = datetime.datetime.combine(datetime.datetime.now().date(),
                                          datetime.time(17))
        return context_tz.localize(start).astimezone(pytz.utc)

    name = fields.Char()
    resource_id = fields.Many2one(
        'resource.resource', string='Resource', required=True)
    date_start = fields.Datetime(
        string='Start Date', required=True, default=defClientEight)
    date_end = fields.Datetime(
        string='End Date', required=True, default=defClientTwelve)
    task_id = fields.Many2one('project.task', 'Task')
    meeting_id = fields.Many2one('calendar.event', string='Meeting')
    current_date = fields.Datetime(default=fields.Date.today())
    task_date_start = fields.Datetime(
        string='Task Date Start', related='task_id.date_start')
    task_date_end = fields.Datetime(
        string='Task Date End', related='task_id.date_end')
    raw_color = fields.Selection(
        [('normal', 'Normal'), ('outofrange', 'Out of range'),
         ('conflict', 'Conflict')],
        string='Raw Color', default='normal',
        compute='_compute_raw_color')
    status_icon = fields.Binary(attachment=True, help='Double Book Entry')
    timesheet_id = fields.Many2one('account.analytic.line', 'Timesheet')
    locked = fields.Boolean('Locked')

    # @api.multi
    # def manual_schedule_meeting_create(self):
    #     return self.task_id.action_meeting_create()

    @api.multi
    def _compute_raw_color(self):
        for record in self:
            cr = self.env.cr
            cr.execute("""
                SELECT id FROM task_schedule
                WHERE  resource_id = '%s'
                AND (date_start, date_end) OVERLAPS ('%s', '%s')""" % (
                record.resource_id.id, record.date_start, record.date_end))
            conflict = cr.fetchall()
            length = len(conflict)
            cr.execute("""
                SELECT id FROM resource_calendar_leaves
                WHERE  resource_id = '%s'
                  AND (date_from, date_to) OVERLAPS ('%s', '%s')""" % (
                record.resource_id.id, record.date_start, record.date_end))
            leaves = cr.fetchall()
            length += len(leaves)
            if length > 1:
                image_path = modules.get_module_resource(
                    'resource_management', 'static/src/img', 'conflict.png')
                conflictImg = open(image_path, 'rb').read().encode('base64')
                record.status_icon = conflictImg
                record.raw_color = 'conflict'
                continue
            elif length == 1:
                record.raw_color = 'normal'
                continue

    #double booked
    def double_booked_query(self, start_dt, end_dt, qstatus = None):
        resource_ids = self.env['resource.resource'].search([])
        count = 0
        task_sch_ids = []
        for resource in resource_ids:
            self._cr.execute('''
                    select
                        ts.id
                    from
                        task_schedule as ts
                    where
                        ts.resource_id = '%s'
                        AND (ts.date_start, ts.date_end) 
                        OVERLAPS ('%s', '%s')
                    '''%(resource.id, start_dt, end_dt))
            today_double_booked = self._cr.fetchall()
            if today_double_booked and len(today_double_booked) > 1:
                task_sch_ids += ((x[0] for x in today_double_booked))
                count += 1
        if qstatus == 'qsearch':
            return tuple(task_sch_ids)
        return count

    #Not Linked
    def not_linked_query(self, start_dt, end_dt, qstatus = None):
        self._cr.execute('''
                select
                    ts.id
                from
                    task_schedule as ts, project_task as pt
                where
                    ts.task_id = pt.id
                    AND (ts.date_start, ts.date_end) 
                    OVERLAPS ('%s', '%s')
                    AND ((ts.date_start < pt.date_start) 
                    OR (ts.date_end > pt.date_end))
                '''%(start_dt, end_dt))
        not_linked = [x[0] for x in self._cr.fetchall()]
        if qstatus == 'qsearch':
            return tuple(not_linked)
        else:
            return len(not_linked)

    # Planned Hourse
    def planned_hours_query(self, start_dt, end_dt, qstatus = None):
        self._cr.execute('''
                select
                    pt.id, pt.planned_hours
                from
                    project_task as pt
                where
                    (pt.date_start, pt.date_end) 
                    OVERLAPS ('%s', '%s')
                    AND pt.active IS NOT false
                '''%(start_dt, end_dt))
        rdata = self._cr.fetchall()
        if qstatus == 'qsearch':
            return tuple([x[0] for x in rdata])
        return round(sum([x[1] for x in rdata if len(x) == 2 and x[1]]),2)

    # scheduled Hourse
    def scheduled_hours_query(self, start_dt, end_dt, qstatus = None):
        self._cr.execute('''
                select
                    pt.id
                from
                    project_task as pt
                where
                    (pt.date_start, pt.date_end) 
                    OVERLAPS ('%s', '%s')
                    AND pt.active IS NOT false
                '''%(start_dt, end_dt))
        task_ids = [x[0] for x in self._cr.fetchall()]
        scheduled_hours = 0
        if qstatus == 'qsearch':
            return tuple(task_ids)
        if task_ids:
            for task_id in task_ids:
                scheduled_hours += self.env['project.task'].browse(task_id).hour_count
        return scheduled_hours

    # task_needed and over planned
    def task_needed_and_overplanned_query(self, start_dt, end_dt, qstatus = None):
        self._cr.execute('''
                select
                    pt.id
                from
                    project_task as pt
                where
                    (pt.date_start, pt.date_end) 
                    OVERLAPS ('%s', '%s')
                    AND pt.active IS NOT false
                '''%(start_dt, end_dt))
        task_ids = self._cr.fetchall()
        count = 0
        task_needed_ids =  []
        task_oplann_ids = []
        if task_ids:
            for task_id in task_ids:
                to_plan_hours = self.env['project.task'].\
                browse(task_id[0]).to_plan_hours
                if qstatus == 'qsearchneeded':
                    if to_plan_hours < 100:
                        task_needed_ids.append(task_id)
                    else:
                        continue

                if qstatus == 'qsearchover':
                    if to_plan_hours > 100:
                        task_oplann_ids.append(task_id)
                    else:
                        continue
                    
                if qstatus == 'needed' and to_plan_hours < 100:
                    count += 1
                if qstatus == 'over' and to_plan_hours > 100:
                    count += 1
            if qstatus == 'qsearchneeded':
                return tuple(task_needed_ids)
            if qstatus == 'qsearchover':
                return tuple(task_oplann_ids)
        return count

    # Resource Available
    def resource_available_booked_query(self, start_dt, end_dt, qstatus = None):

        def resourceWorkingInPeriod(resource, start, end):
            working = True

            # Start End on resource.resource.
            cr = self.env.cr
            cr.execute("""
                SELECT id FROM resource_start_end
                WHERE resource_id=%s and
                      (start_date, end_date) OVERLAPS ('%s', '%s')""" % (
                resource.id, start, start))
            line = cr.fetchall()
            if not line:
                working = False

            # Check for working time
            if working and resource.calendar_id:
                hours = resource.calendar_id.get_working_hours(start, end)
                if not hours:
                    working = False

            return working

        def schedulesInPeriod(resourceId, start, end):
            cr = self.env.cr
            cr.execute(
                """SELECT id FROM task_schedule
                   WHERE  resource_id = '%s'
                   AND (date_start, date_end) OVERLAPS ('%s', '%s')""" % (
                    resourceId, start, end))
            return [x[0] for x in cr.fetchall()]

        def leavesInPeriod(resourceId, start, end):
            cr = self.env.cr
            cr.execute("""SELECT id FROM resource_calendar_leaves
                          WHERE resource_id = '%s'
                          AND (date_from, date_to) OVERLAPS ('%s', '%s')""" % (
                       resourceId, start, end))
            return [x[0] for x in cr.fetchall()]

        def getStatusOfResource(resource, date, defaultStatus='Available'):
            dayStart = date
            dayEnd = dayStart + timedelta(hours=12)

            if not resourceWorkingInPeriod(resource, dayStart, dayEnd):
                return 'Notapplicable', None

            leaves = leavesInPeriod(resource.id, dayStart, dayEnd)
            schedules = schedulesInPeriod(resource.id, dayStart, dayEnd)
            if leaves:
                return 'Leave', leaves
            elif schedules:
                return 'Occupied', schedules
            else:
                return defaultStatus, None

        def filterResourceStartEnd(d_frm_obj, d_to_obj):
            d_to_obj += datetime.timedelta(days=1)
            cr = self.env.cr
            cr.execute("""
                SELECT id FROM resource_start_end
                WHERE (start_date, end_date) OVERLAPS ('%s', '%s')""" % (
                d_frm_obj.date(), d_to_obj.date()))
            return cr.fetchall()
        
        lines = filterResourceStartEnd(start_dt, end_dt)

        resources_ids = []
        lines = tuple(x[0] for x in lines if x)
        if lines:
            cr = self.env.cr
            cr.execute("""
                SELECT rr.id FROM resource_resource rr
                    JOIN resource_start_end rse ON rse.resource_id = rr.id
                WHERE rr.calendar_id IS NOT NULL
                    AND rse.id IN %s""" % (lines,))
            resources_ids = [x[0] for x in cr.fetchall()]
        resources = self.env['resource.resource'].browse(resources_ids)
        date_range_list = []
        temp_date = start_dt
        resource_list_human = []
        resource_list_material = []
        resource_list = []
        while(temp_date <= end_dt):
            date_range_list.append(temp_date)
            temp_date += datetime.timedelta(hours=12)
        for resc in resources:
            defaultStatus = 'Available'
            for chkDate in date_range_list[::-1]:
                status, ids = getStatusOfResource(resc, chkDate, defaultStatus)
                if qstatus == 'qsearchbook':
                    if status == 'Occupied':
                        resource_list.append(resc.id)
                    else:
                        continue
                if qstatus == 'qsearchav':
                    if status == 'Available':
                        resource_list.append(resc.id)
                    else:
                        continue
                if qstatus == 'Occupied' and status == 'Occupied':
                    if resc.resource_type == 'material':
                        resource_list_material.append(resc.id)
                    if resc.resource_type == 'user':
                        resource_list_human.append(resc.id)
                if qstatus == 'Available' and status == 'Available':
                    if resc.resource_type == 'material':
                        resource_list_material.append(resc.id)
                    if resc.resource_type == 'user':
                        resource_list_human.append(resc.id)
        if qstatus == 'qsearchbook':
            return tuple(resource_list)
        if qstatus == 'qsearchav':
            return tuple(resource_list)
        return [str(len(set(resource_list_human)))+ ' ',
                ' '+str(len(set(resource_list_material)))]

    # realized_hours
    def realized_hours_query(self, start_dt, end_dt, qstatus = None):
        self._cr.execute('''
                select
                    pt.id, pt.progress
                from
                    project_task as pt
                where
                    (pt.date_start, pt.date_end) 
                    OVERLAPS ('%s', '%s')
                    AND pt.active IS NOT false
                '''%(start_dt, end_dt))

        rdata = self._cr.fetchall()
        if qstatus == 'qsearch':
            return tuple([x[0] for x in rdata])
        return round(sum([x[1] for x in rdata if x and len(x) == 2 and x[1]]),2)

    # no of task
    def no_of_task_query(self, qstatus = None):

        ir_model_obj = self.env['ir.model.data']
        stage_id = ir_model_obj.get_object_reference(
                    'project', 'project_stage_data_0')[1]
        self._cr.execute('''
                select
                    pt.id
                from
                    project_task as pt
                where
                    pt.active IS NOT false
                    AND stage_id IN (%s)
                '''%(stage_id))
        task_ids = [x[0] for x in self._cr.fetchall()]

        if qstatus == 'qsearch':
            return tuple(task_ids)
        else:
            return len(task_ids)

    # task_no_team
    def task_no_team_query(self, qstatus = None):

        project_task_ids = self.env['project.task'].\
                            search([('resource_ids', '=', False)])
        task_ids = [pid.id for pid in project_task_ids]

        if qstatus == 'qsearch':
            return tuple(task_ids)
        else:
            return len(task_ids)

    # task_overdue
    def task_overdue_query(self, qdate = None, qstatus = None):

        ir_model_obj = self.env['ir.model.data']
        #stage_id = ir_model_obj.get_object_reference(
        #            'project', 'project_stage_1')[1]
        self._cr.execute('''
                select
                    pt.id
                from
                    project_task as pt
                where
                    pt.active IS NOT false
                    AND pt.date_end < '%s'
                '''%(qdate))

        task_ids = [x[0] for x in self._cr.fetchall()]

        if qstatus == 'qsearch':
            return tuple(task_ids)
        else:
            return len(task_ids)
        

    @api.model
    def retrieve_resource_dashboard(self):
        """ Fetch data to setup Helpdesk Ticket Dashboard """

        start_dt = datetime.datetime.now().replace(hour=0, minute=0, second=0)
        end_dt = start_dt.replace(hour=23, minute=59, second=59)
        today = fields.date.today()
        
        # Week
        monday = (start_dt + relativedelta(weekday=MO(-1))).replace(hour=0, minute=0, second=0)
        next_monday = monday + relativedelta(weeks=+1)
        last_monday = monday + relativedelta(weeks=-1)
        sunday = (start_dt + relativedelta(weekday=SU(+1))).replace(hour=23, minute=59, second=59)
        next_sunday = sunday + relativedelta(weeks=+1)
        last_sunday = sunday + relativedelta(weeks=-1)

        # month
        first_day_this_month = (start_dt.replace(day=1)).replace(hour=0, minute=0, second=0)
        last_day_this_month = (datetime.datetime(start_dt.year,start_dt.month,1)+relativedelta(months=1,days=-1)).replace(hour=23, minute=59, second=59)
        next_month = start_dt + relativedelta(months=1)
        first_day_next_month = (next_month.replace(day=1)).replace(hour=0, minute=0, second=0)
        last_day_next_month = (datetime.datetime(next_month.year,next_month.month,1)+relativedelta(months=1,days=-1)).replace(hour=23, minute=59, second=59)
        last_month = start_dt + relativedelta(months=-1)
        first_day_last_month = (last_month.replace(day=1)).replace(hour=0, minute=0, second=0)
        last_day_last_month = (datetime.datetime(last_month.year,last_month.month,1)+relativedelta(months=1,days=-1)).replace(hour=23, minute=59, second=59)

        # days
        today_datetime = datetime.datetime.now()
        tomorrow_start_dt = (today_datetime + timedelta(days=1)).replace(hour=0, minute=0, second=0)
        tomorrow_end_dt = (today_datetime + timedelta(days=1)).replace(hour=23, minute=59, second=59)
        yester_start_dt = (today_datetime + timedelta(days=-1)).replace(hour=0, minute=0, second=0)
        yester_end_dt = (today_datetime + timedelta(days=-1)).replace(hour=23, minute=59, second=59)

        result = {
            'double': {
                'today': self.double_booked_query(start_dt, end_dt),
                'tomorrow': self.double_booked_query(tomorrow_start_dt, 
                            tomorrow_end_dt),
                'this_week': self.double_booked_query(monday, sunday),
                'next_week': self.double_booked_query(next_monday, next_sunday),
                'this_month': self.double_booked_query(first_day_this_month,
                              last_day_this_month),
                'next_month': self.double_booked_query(first_day_next_month, 
                            last_day_next_month),
            },
            'not_linked': {
                'today': self.not_linked_query(start_dt, end_dt),
                'tomorrow': self.not_linked_query(tomorrow_start_dt, 
                            tomorrow_end_dt),
                'this_week': self.not_linked_query(monday, sunday),
                'next_week': self.not_linked_query(next_monday, next_sunday),
                'this_month': self.not_linked_query(first_day_this_month, 
                            last_day_this_month),
                'next_month': self.not_linked_query(first_day_next_month, 
                            last_day_next_month),
            },
            'planned_hours': {
                'today': self.planned_hours_query(start_dt, end_dt),
                'yesterday': self.planned_hours_query(yester_start_dt, yester_end_dt),
                'tomorrow': self.planned_hours_query(tomorrow_start_dt, 
                            tomorrow_end_dt),
                'this_week': self.planned_hours_query(monday, sunday),
                'last_week': self.planned_hours_query(last_monday, last_sunday),
                'next_week': self.planned_hours_query(next_monday, next_sunday),
                'this_month': self.planned_hours_query(first_day_this_month,
                              last_day_this_month),
                'last_month': self.planned_hours_query(first_day_last_month,
                              last_day_last_month),
                'next_month': self.planned_hours_query(first_day_next_month, 
                            last_day_next_month),
            },
            'scheduled_hours': {
                'today': self.scheduled_hours_query(start_dt, end_dt),
                'yesterday': self.scheduled_hours_query(yester_start_dt, yester_end_dt),
                'tomorrow': self.scheduled_hours_query(tomorrow_start_dt, 
                            tomorrow_end_dt),
                'this_week': self.scheduled_hours_query(monday, sunday),
                'next_week': self.scheduled_hours_query(next_monday, next_sunday),
                'last_week': self.scheduled_hours_query(last_monday, last_sunday),
                'this_month': self.scheduled_hours_query(first_day_this_month,
                              last_day_this_month),
                'next_month': self.scheduled_hours_query(first_day_next_month, 
                            last_day_next_month),
                'last_month': self.scheduled_hours_query(first_day_last_month,
                              last_day_last_month),
            },
            'task_needed': {
                'today': self.task_needed_and_overplanned_query(
                            start_dt, end_dt, qstatus = 'needed'),
                'tomorrow': self.task_needed_and_overplanned_query(
                                tomorrow_start_dt, tomorrow_end_dt, 
                                qstatus = 'needed'),
                'this_week': self.task_needed_and_overplanned_query(
                                monday, sunday, qstatus = 'needed'),
                'next_week': self.task_needed_and_overplanned_query(
                                next_monday, next_sunday, qstatus = 'needed'),
                'this_month': self.task_needed_and_overplanned_query(
                                first_day_this_month, last_day_this_month, 
                                qstatus = 'needed'),
                'next_month': self.task_needed_and_overplanned_query(
                            first_day_next_month, last_day_next_month, 
                                qstatus = 'needed'),
            },
            'task_overplanned': {
                'today': self.task_needed_and_overplanned_query(start_dt, end_dt, 
                                qstatus ='over'),
                'tomorrow': self.task_needed_and_overplanned_query(
                                tomorrow_start_dt, tomorrow_end_dt, qstatus ='over'),
                'this_week': self.task_needed_and_overplanned_query(
                                monday, sunday, qstatus ='over'),
                'next_week': self.task_needed_and_overplanned_query(
                                next_monday, next_sunday, qstatus ='over'),
                'this_month': self.task_needed_and_overplanned_query(
                                first_day_this_month, last_day_this_month, qstatus ='over'),
                'next_month': self.task_needed_and_overplanned_query(
                            first_day_next_month, last_day_next_month, qstatus ='over'),
            },

            'resource_available': {
                'today': self.resource_available_booked_query(
                            start_dt, end_dt,qstatus = 'Available'),
                'tomorrow': self.resource_available_booked_query(
                                tomorrow_start_dt, tomorrow_end_dt, 
                                qstatus = 'Available'),
                'this_week': self.resource_available_booked_query(
                                monday, sunday, qstatus = 'Available'),
                'next_week': self.resource_available_booked_query(
                                next_monday, next_sunday, qstatus = 'Available'),
                'this_month': self.resource_available_booked_query(
                                first_day_this_month, last_day_this_month,
                                qstatus = 'Available'),
                'next_month': self.resource_available_booked_query(
                            first_day_next_month, last_day_next_month, 
                            qstatus = 'Available'),
            },

            'resource_booked': {
                'today': self.resource_available_booked_query(start_dt, end_dt,
                            qstatus = 'Occupied'),
                'tomorrow': self.resource_available_booked_query(
                                tomorrow_start_dt, tomorrow_end_dt, 
                                qstatus = 'Occupied'),
                'this_week': self.resource_available_booked_query(
                                monday, sunday, qstatus = 'Occupied'),
                'next_week': self.resource_available_booked_query(
                                next_monday, next_sunday, qstatus = 'Occupied'),
                'this_month': self.resource_available_booked_query(
                                first_day_this_month, last_day_this_month, 
                                qstatus = 'Occupied'),
                'next_month': self.resource_available_booked_query(
                                first_day_next_month, last_day_next_month, 
                                qstatus = 'Occupied'),
            },

            'realized_hours': {
                'yesterday': self.realized_hours_query(start_dt, end_dt),
                'last_week': self.realized_hours_query(tomorrow_start_dt, 
                            tomorrow_end_dt),
                'last_month': self.realized_hours_query(monday, sunday),
                'next_week': self.realized_hours_query(next_monday, next_sunday),
                'this_month': self.realized_hours_query(first_day_this_month,
                              last_day_this_month),
                'next_month': self.realized_hours_query(first_day_next_month, 
                            last_day_next_month),
            },

            'no_of_task': {
                'no_of_task': self.no_of_task_query(),
            },
            'task_no_team': {
                'task_no_team': self.task_no_team_query(),
            },
            'task_overdue': {
                'task_overdue': self.task_overdue_query(today_datetime),
            },
            'nb_opportunities': 0,
        }
        assign_domain = [
            ('user_id', '=', [self.env.user.id])
        ]

        return result

    @api.multi
    def unlink(self):
        for record in self:
            meeting = self.env['calendar.event'].search(
                [('id', '=', record.meeting_id.id)]).unlink()
        return super(ResourceSchedule, self).unlink()


class CalendarEvent(models.Model):
    _inherit = "calendar.event"

    resource_id = fields.Many2one('resource.resource', string="Resource")


class ResourceAvailablility(models.Model):
    _name = 'resource.availability'
    _rec_name = 'resource_period'

    resource_period = fields.Selection([('this_week', 'This Week'),
                                        ('next_week', 'Next Week'),
                                        ('this_month', 'This Month'),
                                        ('next_month', 'Next Month'),
                                        ('custom', 'Custom')],
                                       default='this_week',
                                       string="Plan Period")
    date_from = fields.Date('From', default=fields.Date.today())
    date_to = fields.Date(
        'To', default=datetime.date.today() + datetime.timedelta(days=6))
    resource_header = fields.Text('Header')
    resource_info = fields.Text('Resource')
    resource_header_date = fields.Text('Date Header')
    resource_header_day = fields.Text('Day Header')

    @api.onchange('resource_period')
    def get_date(self):
        now = datetime.date.today()
        if self.resource_period == 'this_week':
            self.date_to = (now -
                            timedelta(days=now.weekday())) + timedelta(days=6)
            self.date_from = (now - timedelta(days=now.weekday()))
        elif self.resource_period == 'next_week':
            self.date_from = (now +
                              datetime.timedelta(days=(7 - now.weekday())))
            self.date_to = now + datetime.timedelta(
                days=(7 - now.weekday())) + timedelta(days=6)
        elif self.resource_period == 'this_month':
            month_last_day = calendar.monthrange(now.year, now.month)
            self.date_from = now.replace(day=1)
            self.date_to = now.replace(day=month_last_day[1])
        elif self.resource_period == 'next_month':
            next_month_first_date = now + relativedelta(day=1, months=+1)
            next_month_last_day = calendar.monthrange(
                now.year, next_month_first_date.month)
            self.date_from = next_month_first_date
            self.date_to = (
                next_month_first_date +
                datetime.timedelta(days=next_month_last_day[1] - 1))

    @api.onchange('date_from', 'date_to')
    def get_resource_availability(self):
        res = {}
        if (not self.date_from) or (not self.date_to):
            return res
        if self.date_from > self.date_to:
            raise except_orm(
                _('User Error!'),
                _('Please Check Time period Date From can\'t be greater than Date To !'))

        def leavesInPeriod(resourceId, start, end):
            cr = self.env.cr
            cr.execute("""SELECT id FROM resource_calendar_leaves
                          WHERE resource_id = '%s'
                          AND (date_from, date_to) OVERLAPS ('%s', '%s')""" % (
                       resourceId, start, end))
            return [x[0] for x in cr.fetchall()]

        def schedulesInPeriod(resourceId, start, end):
            cr = self.env.cr
            cr.execute(
                """SELECT id FROM task_schedule
                   WHERE  resource_id = '%s'
                   AND (date_start, date_end) OVERLAPS ('%s', '%s')""" % (
                    resourceId, start, end))
            return [x[0] for x in cr.fetchall()]

        def resourceWorkingInPeriod(resource, start, end):
            working = True

            # Start End on resource.resource.
            cr = self.env.cr
            cr.execute("""
                SELECT id FROM resource_start_end
                WHERE resource_id=%s and
                      (start_date, end_date) OVERLAPS ('%s', '%s')""" % (
                resource.id, start, start))
            line = cr.fetchall()
            if not line:
                working = False

            # Check for working time
            if working and resource.calendar_id:
                hours = resource.calendar_id.get_working_hours(start, end)
                if not hours:
                    working = False

            return working

        def filterResourceStartEnd(d_frm_obj, d_to_obj):
            d_to_obj += datetime.timedelta(days=1)
            cr = self.env.cr
            cr.execute("""
                SELECT id FROM resource_start_end
                WHERE (start_date, end_date) OVERLAPS ('%s', '%s')""" % (
                d_frm_obj.date(), d_to_obj.date()))
            return cr.fetchall()

        def getStatusOfResource(resource, date, defaultStatus='Available'):
            dayStart = datetime.datetime.strptime(date, DTFORMAT)
            dayEnd = dayStart + timedelta(hours=12)

            if not resourceWorkingInPeriod(resource, dayStart, dayEnd):
                return 'Notapplicable', None

            leaves = leavesInPeriod(resource.id, dayStart, dayEnd)
            schedules = schedulesInPeriod(resource.id, dayStart, dayEnd)
            if leaves:
                return 'Leave', leaves
            elif schedules:
                return 'Occupied', schedules
            else:
                return defaultStatus, None

        timezone = pytz.timezone(
            self._context.get('tz', False) or self.env.user.tz or 'UTC')
        d_frm_obj = datetime.datetime.strptime(self.date_from, DFORMAT)
        d_frm_obj = timezone.localize(d_frm_obj).astimezone(pytz.utc)
        d_to_obj = datetime.datetime.strptime(
            self.date_to, DFORMAT).replace(hour=23, minute=59)
        d_to_obj = timezone.localize(d_to_obj).astimezone(pytz.utc)

        date_range_list = []
        temp_date = d_frm_obj
        while(temp_date <= d_to_obj):
            date_range_list.append(temp_date.strftime(DTFORMAT))
            temp_date += datetime.timedelta(hours=12)

        resource_header_list = [_('Employee')]
        date_header_list = []
        day_header_list = []
        header_date = d_frm_obj
        while(header_date <= d_to_obj):
            date_header_list.append({'date':_(header_date.astimezone(timezone).strftime("%d-%b-%y")),
                                     'org_date':_(header_date.astimezone(timezone).strftime("%Y-%m-%d %H:%M:%S"))})
            day_header_list.append(
                _(header_date.astimezone(timezone).strftime("%A")))
            resource_header_list.extend([_('Morning'), _('Evening')])
            header_date += datetime.timedelta(days=1)
        all_resource_detail = []
        lines = filterResourceStartEnd(d_frm_obj, d_to_obj)
        resources = self.env['resource.resource'].search(
            [('calendar_id', '!=', False),
             ('start_end_ids', 'in', lines)])
        for resc in resources:
            resource_detail = {}
            resource_list_stats = []
            resource_detail.update({'name': resc.name or ''})

            defaultStatus = 'Available'
            for chkDate in date_range_list[::-1]:
                status, ids = getStatusOfResource(resc, chkDate, defaultStatus)
                clickDateTime = pytz.utc.localize(
                    datetime.datetime.strptime(
                        chkDate, DTFORMAT)).astimezone(timezone)
                clickDateTimeStr = clickDateTime.strftime(DTFORMAT)
                if status == 'Free':
                    resource_list_stats.append({'state': status,
                                                'date': clickDateTimeStr,
                                                'resource_id': resc.id,
                                                'employee_id': resc.id})
                elif status == 'Occupied':
                    defaultStatus = 'Free'
                    resource_list_stats.append({'state': 'Occupied',
                                                'date': clickDateTimeStr,
                                                'resource_id': resc.id,
                                                'is_draft': 'No',
                                                'data_model': 'task.schedule',
                                                'data_id': ids})
                elif status == 'Leave':
                    defaultStatus = 'Free'
                    resource_list_stats.append({'state': 'Leave',
                                                'date': clickDateTimeStr,
                                                'resource_id': resc.id,
                                                'data_model': '',
                                                'data_id': 0})
                elif status == 'Available':
                    resource_list_stats.append({'state': 'Available',
                                                'date': clickDateTimeStr,
                                                'resource_id': resc.id,
                                                'data_model': '',
                                                'data_id': 0})
                elif status == 'Notapplicable':
                    resource_list_stats.append({'state': 'Notapplicable',
                                                'date': clickDateTimeStr,
                                                'resource_id': resc.id,
                                                'data_model': '',
                                                'data_id': 0})

            resource_detail.update({'value': resource_list_stats[::-1]})
            all_resource_detail.append(resource_detail)

        main_header = [{'header': resource_header_list}]
        date_header = [{'head': date_header_list}]
        day_header = [{'head': day_header_list}]
        self.resource_header = str(main_header)
        self.resource_info = str(all_resource_detail)
        self.resource_header_date = str(date_header)
        self.resource_header_day = str(day_header)
        return res


class HrHolidays(models.Model):
    _inherit = 'hr.holidays'

    @api.multi
    def createResourceLeave(self):
        user = self.employee_id.user_id
        hr_holidays = self.id
        resource = self.env['resource.resource'].search(
            [('user_id', '=', user.id)], limit=1)
        if not resource:
            return
        resource_leave = self.env['resource.calendar.leaves'].search(
            [('resource_id', '=', resource.id),
             ('holiday_id', '=', hr_holidays)])
        if resource_leave:
            return
        else:
            return self.env['resource.calendar.leaves'].create({
                'name': self.name,
                'holiday_id': self.id,
                'calendar_id': resource.calendar_id.id,
                'resource_id': resource.id,
                'date_from': self.date_from,
                'date_to': self.date_to
            })

    @api.multi
    def action_approve(self):
        result = super(HrHolidays, self).action_approve()
        meeting = self.createResourceLeave()
        return result


class ResourceStartEnd(models.Model):
    _name = 'resource.start_end'

    resource_id = fields.Many2one(
        'resource.resource', string='Resource', required=True)
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End date')


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    @api.model
    def create(self, vals):
        result = super(HrEmployee, self).create(vals)
        result.resource_id.employee_id = result.id
        return result


class AccountAnalyticLine(models.Model):
    _inherit = 'account.analytic.line'

    locked = fields.Boolean('Locked')
    schedule_id = fields.Many2one('task.schedule', string='Schedule')