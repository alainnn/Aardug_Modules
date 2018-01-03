# -*- coding: utf-8 -*-

import datetime
from datetime import time, timedelta
from odoo import models, fields, api
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT as DFORMAT
from odoo.tools.safe_eval import safe_eval

class hr_exipre_doc_employee(models.Model):
    _inherit = 'hr.employee'
     
   
    hr_task_certificate1 = fields.Char("Certificaat 1")
    hr_task_certificate2 = fields.Char("Certificaat 2")
    hr_task_certificate3 = fields.Char("Certificaat 3")
    hr_task_certificate4 = fields.Char("Certificaat 4")
    hr_task_certificate5 = fields.Char("Certificaat 5")
    hr_task_certificate6 = fields.Char("Certificaat 6")
    hr_task_certificate7 = fields.Char("Certificaat 7")
    hr_task_certificate8 = fields.Char("Certificaat 8")
    hr_task_certificate9 = fields.Char("Certificaat 9")
    hr_task_certificate10 = fields.Char("Certificaat 10")

    hr_task_passport = fields.Char("Paspoort")
    hr_task_identification = fields.Char("ID")
    hr_task_driving_license = fields.Char("Rijbewijs")
    hr_task_work_permit = fields.Char("Werkvergunning")

    hr_task_enddate_certificate1 = fields.Date("Eind datum")
    hr_task_enddate_certificate2 = fields.Date("Eind datum")
    hr_task_enddate_certificate3 = fields.Date("Eind datum")
    hr_task_enddate_certificate4 = fields.Date("Eind datum")
    hr_task_enddate_certificate5 = fields.Date("Eind datum")
    hr_task_enddate_certificate6 = fields.Date("Eind datum")
    hr_task_enddate_certificate7 = fields.Date("Eind datum")
    hr_task_enddate_certificate8 = fields.Date("Eind datum")
    hr_task_enddate_certificate9 = fields.Date("Eind datum")
    hr_task_enddate_certificate10 = fields.Date("Eind datum")

    hr_task_enddate_passport = fields.Date("Eind datum")
    hr_task_enddate_identification = fields.Date("Eind datum")
    hr_task_enddate_driving_license = fields.Date("Eind datum")
    hr_task_enddate_work_permit = fields.Date("Eind datum")

    certificate1_duration = fields.Selection([
            ('one_week', '1 Week'),
            ('two_week', '2 Week'),
            ('one_month', '1 Month'),
            ('two_month', '2 Month'),
            ('three_month', '3 Month'),
            ('six_month', '6 Month'),
            ('twelve_month', '12 Month')
        ], string='Duration')
    certificate2_duration = fields.Selection([
            ('one_week', '1 Week'),
            ('two_week', '2 Week'),
            ('one_month', '1 Month'),
            ('two_month', '2 Month'),
            ('three_month', '3 Month'),
            ('six_month', '6 Month'),
            ('twelve_month', '12 Month')
        ], string='Duration')
    certificate3_duration = fields.Selection([
            ('one_week', '1 Week'),
            ('two_week', '2 Week'),
            ('one_month', '1 Month'),
            ('two_month', '2 Month'),
            ('three_month', '3 Month'),
            ('six_month', '6 Month'),
            ('twelve_month', '12 Month')
        ], string='Duration')
    certificate4_duration = fields.Selection([
            ('one_week', '1 Week'),
            ('two_week', '2 Week'),
            ('one_month', '1 Month'),
            ('two_month', '2 Month'),
            ('three_month', '3 Month'),
            ('six_month', '6 Month'),
            ('twelve_month', '12 Month')
        ], string='Duration')
    certificate5_duration = fields.Selection([
            ('one_week', '1 Week'),
            ('two_week', '2 Week'),
            ('one_month', '1 Month'),
            ('two_month', '2 Month'),
            ('three_month', '3 Month'),
            ('six_month', '6 Month'),
            ('twelve_month', '12 Month')
        ], string='Duration')
    certificate6_duration = fields.Selection([
            ('one_week', '1 Week'),
            ('two_week', '2 Week'),
            ('one_month', '1 Month'),
            ('two_month', '2 Month'),
            ('three_month', '3 Month'),
            ('six_month', '6 Month'),
            ('twelve_month', '12 Month')
        ], string='Duration')
    certificate7_duration = fields.Selection([
            ('one_week', '1 Week'),
            ('two_week', '2 Week'),
            ('one_month', '1 Month'),
            ('two_month', '2 Month'),
            ('three_month', '3 Month'),
            ('six_month', '6 Month'),
            ('twelve_month', '12 Month')
        ], string='Duration')
    certificate8_duration = fields.Selection([
            ('one_week', '1 Week'),
            ('two_week', '2 Week'),
            ('one_month', '1 Month'),
            ('two_month', '2 Month'),
            ('three_month', '3 Month'),
            ('six_month', '6 Month'),
            ('twelve_month', '12 Month')
        ], string='Duration')
    certificate9_duration = fields.Selection([
            ('one_week', '1 Week'),
            ('two_week', '2 Week'),
            ('one_month', '1 Month'),
            ('two_month', '2 Month'),
            ('three_month', '3 Month'),
            ('six_month', '6 Month'),
            ('twelve_month', '12 Month')
        ], string='Duration')
    certificate10_duration = fields.Selection([
            ('one_week', '1 Week'),
            ('two_week', '2 Week'),
            ('one_month', '1 Month'),
            ('two_month', '2 Month'),
            ('three_month', '3 Month'),
            ('six_month', '6 Month'),
            ('twelve_month', '12 Month')
        ], string='Duration')

    passport_duration = fields.Selection([
            ('one_week', '1 Week'),
            ('two_week', '2 Week'),
            ('one_month', '1 Month'),
            ('two_month', '2 Month'),
            ('three_month', '3 Month'),
            ('six_month', '6 Month'),
            ('twelve_month', '12 Month')
        ], string='Duration')
    id_duration = fields.Selection([
            ('one_week', '1 Week'),
            ('two_week', '2 Week'),
            ('one_month', '1 Month'),
            ('two_month', '2 Month'),
            ('three_month', '3 Month'),
            ('six_month', '6 Month'),
            ('twelve_month', '12 Month')
        ], string='Duration')
    licence_duration = fields.Selection([
            ('one_week', '1 Week'),
            ('two_week', '2 Week'),
            ('one_month', '1 Month'),
            ('two_month', '2 Month'),
            ('three_month', '3 Month'),
            ('six_month', '6 Month'),
            ('twelve_month', '12 Month')
        ], string='Duration')
    work_permit_duration = fields.Selection([
            ('one_week', '1 Week'),
            ('two_week', '2 Week'),
            ('one_month', '1 Month'),
            ('two_month', '2 Month'),
            ('three_month', '3 Month'),
            ('six_month', '6 Month'),
            ('twelve_month', '12 Month')
        ], string='Duration')

    file_certificate1_attachment = fields.Binary(string='Document', attachment=True)
    file_name_cirtificate1 = fields.Char('File Name')
    certificate2_attachment = fields.Binary(string='Document', attachment=True)
    file_name_cirtificate2 = fields.Char('File Name')
    certificate3_attachment = fields.Binary(string='Document', attachment=True)
    file_name_cirtificate3 = fields.Char('File Name')
    certificate4_attachment = fields.Binary(string='Document', attachment=True)
    file_name_cirtificate4 = fields.Char('File Name')
    certificate5_attachment = fields.Binary(string='Document', attachment=True)
    file_name_cirtificate5 = fields.Char('File Name')
    certificate6_attachment = fields.Binary(string='Document', attachment=True)
    file_name_cirtificate6 = fields.Char('File Name')
    certificate7_attachment = fields.Binary(string='Document', attachment=True)
    file_name_cirtificate7 = fields.Char('File Name')
    certificate8_attachment = fields.Binary(string='Document', attachment=True)
    file_name_cirtificate8 = fields.Char('File Name')
    certificate9_attachment = fields.Binary(string='Document', attachment=True)
    file_name_cirtificate9 = fields.Char('File Name')
    certificate10_attachment = fields.Binary(string='Document', attachment=True)
    file_name_cirtificate10 = fields.Char('File Name')

    passport_attachment = fields.Binary(string='Document', attachment=True)
    file_name_passport = fields.Char('File Name')
    id_attachment = fields.Binary(string='Document', attachment=True)
    file_name_id = fields.Char('File Name')
    licence_attachment = fields.Binary(string='Document', attachment=True)
    file_name_licence = fields.Char('File Name')
    work_permit_attachment = fields.Binary(string='Document', attachment=True)
    file_name_permit = fields.Char('File Name')

    def task_created_serty1(self, employee, project):
        data_obj = self.env['ir.config_parameter'].sudo()
        certificate1_project_id = safe_eval(data_obj.get_param('hr_exipre_doc.certificate1_project_id', 'False'))
        project_id = self.env['project.project'].browse(certificate1_project_id)
        task = self.env['project.task'].create({
               'name': employee.hr_task_certificate1 +' - '+ employee.name,
               'date_deadline': employee.hr_task_enddate_certificate1,
               'employee_id': employee.id,
               'project_id': project_id.id or project and project.id or False,
               'user_id': project_id.user_id.id or project.user_id and project.user_id.id or False
        })
        return task

    def task_created_serty2(self, employee, project):
        data_obj = self.env['ir.config_parameter'].sudo()
        certificate2_project_id = safe_eval(data_obj.get_param('hr_exipre_doc.certificate2_project_id', 'False'))
        project_id = self.env['project.project'].browse(certificate2_project_id)
        task = self.env['project.task'].create({
               'name': employee.hr_task_certificate2 +' - '+ employee.name,
               'date_deadline': employee.hr_task_enddate_certificate2,
               'employee_id': employee.id,
               'project_id': project_id.id or project and project.id or False,
               'user_id': project_id.user_id.id or project.user_id and project.user_id.id or False
        })
        return task

    def task_created_serty3(self, employee, project):
        data_obj = self.env['ir.config_parameter'].sudo()
        certificate3_project_id = safe_eval(data_obj.get_param('hr_exipre_doc.certificate3_project_id', 'False'))
        project_id = self.env['project.project'].browse(certificate3_project_id)
        task = self.env['project.task'].create({
               'name': employee.hr_task_certificate3 +' - '+ employee.name,
               'date_deadline': employee.hr_task_enddate_certificate3,
               'employee_id': employee.id,
               'project_id': project_id.id or project and project.id or False,
               'user_id': project_id.user_id.id or project.user_id and project.user_id.id or False
        })
        return task

    def task_created_serty4(self, employee, project):
        data_obj = self.env['ir.config_parameter'].sudo()
        certificate4_project_id = safe_eval(data_obj.get_param('hr_exipre_doc.certificate4_project_id', 'False'))
        project_id = self.env['project.project'].browse(certificate4_project_id)
        task = self.env['project.task'].create({
               'name': employee.hr_task_certificate4 +' - '+ employee.name,
               'date_deadline': employee.hr_task_enddate_certificate4,
               'employee_id': employee.id,
               'project_id': project_id.id or project and project.id or False,
               'user_id': project_id.user_id.id or project.user_id and project.user_id.id or False
        })
        return task

    def task_created_serty5(self, employee, project):
        data_obj = self.env['ir.config_parameter'].sudo()
        certificate5_project_id = safe_eval(data_obj.get_param('hr_exipre_doc.certificate5_project_id', 'False'))
        project_id = self.env['project.project'].browse(certificate5_project_id)
        task = self.env['project.task'].create({
               'name': employee.hr_task_certificate5 +' - '+ employee.name,
               'date_deadline': employee.hr_task_enddate_certificate5,
               'employee_id': employee.id,
               'project_id': project_id.id or project and project.id or False,
               'user_id': project_id.user_id.id or project.user_id and project.user_id.id or False
        })
        return task

    def task_created_serty6(self, employee, project):
        data_obj = self.env['ir.config_parameter'].sudo()
        certificate6_project_id = safe_eval(data_obj.get_param('hr_exipre_doc.certificate6_project_id', 'False'))
        project_id = self.env['project.project'].browse(certificate6_project_id)
        task = self.env['project.task'].create({
               'name': employee.hr_task_certificate6 +' - '+ employee.name,
               'date_deadline': employee.hr_task_enddate_certificate6,
               'employee_id': employee.id,
               'project_id': project_id.id or project and project.id or False,
               'user_id': project_id.user_id.id or project.user_id and project.user_id.id or False
        })
        return task

    def task_created_serty7(self, employee, project):
        data_obj = self.env['ir.config_parameter'].sudo()
        certificate7_project_id = safe_eval(data_obj.get_param('hr_exipre_doc.certificate7_project_id', 'False'))
        project_id = self.env['project.project'].browse(certificate7_project_id)
        task = self.env['project.task'].create({
               'name': employee.hr_task_certificate7 +' - '+ employee.name,
               'date_deadline': employee.hr_task_enddate_certificate7,
               'employee_id': employee.id,
               'project_id': project_id.id or project and project.id or False,
               'user_id': project_id.user_id.id or project.user_id and project.user_id.id or False
        })
        return task

    def task_created_serty8(self, employee, project):
        data_obj = self.env['ir.config_parameter'].sudo()
        certificate8_project_id = safe_eval(data_obj.get_param('hr_exipre_doc.certificate8_project_id', 'False'))
        project_id = self.env['project.project'].browse(certificate8_project_id)
        task = self.env['project.task'].create({
               'name': employee.hr_task_certificate8 +' - '+ employee.name,
               'date_deadline': employee.hr_task_enddate_certificate8,
               'employee_id': employee.id,
               'project_id': project_id.id or project and project.id or False,
               'user_id': project_id.user_id.id or project.user_id and project.user_id.id or False
        })
        return task

    def task_created_serty9(self, employee, project):
        data_obj = self.env['ir.config_parameter'].sudo()
        certificate9_project_id = safe_eval(data_obj.get_param('hr_exipre_doc.certificate9_project_id', 'False'))
        project_id = self.env['project.project'].browse(certificate9_project_id)
        task = self.env['project.task'].create({
               'name': employee.hr_task_certificate9 +' - '+ employee.name,
               'date_deadline': employee.hr_task_enddate_certificate9,
               'employee_id': employee.id,
               'project_id': project_id.id or project and project.id or False,
               'user_id': project_id.user_id.id or project.user_id and project.user_id.id or False
        })
        return task

    def task_created_serty10(self, employee, project):
        data_obj = self.env['ir.config_parameter'].sudo()
        certificate10_project_id = safe_eval(data_obj.get_param('hr_exipre_doc.certificate10_project_id', 'False'))
        project_id = self.env['project.project'].browse(certificate10_project_id)
        task = self.env['project.task'].create({
               'name': employee.hr_task_certificate10 +' - '+ employee.name,
               'date_deadline': employee.hr_task_enddate_certificate10,
               'employee_id': employee.id,
               'project_id': project_id.id or project and project.id or False,
               'user_id': project_id.user_id.id or project.user_id and project.user_id.id or False
        })
        return task

    def task_created_passport(self, employee, project):
        data_obj = self.env['ir.config_parameter'].sudo()
        passport_project_id = safe_eval(data_obj.get_param('hr_exipre_doc.passport_project_id', 'False'))
        project_id = self.env['project.project'].browse(passport_project_id)
        task = self.env['project.task'].create({
               'name': employee.hr_task_passport +' - '+ employee.name,
               'date_deadline': employee.hr_task_enddate_passport,
               'employee_id': employee.id,
               'project_id': project_id.id or project and project.id or False,
               'user_id': project_id.user_id.id or project.user_id and project.user_id.id or False
        })
        return task

    def task_created_id(self, employee, project):
        data_obj = self.env['ir.config_parameter'].sudo()
        identification_project_id = safe_eval(data_obj.get_param('hr_exipre_doc.identification_project_id', 'False'))
        project_id = self.env['project.project'].browse(identification_project_id)
        task = self.env['project.task'].create({
               'name': employee.hr_task_identification +' - '+ employee.name,
               'date_deadline': employee.hr_task_enddate_identification,
               'employee_id': employee.id,
               'project_id': project_id.id or project and project.id or False,
               'user_id': project_id.user_id.id or project.user_id and project.user_id.id or False
        })
        return task

    def task_created_licence(self, employee, project):
        data_obj = self.env['ir.config_parameter'].sudo()
        license_project_id = safe_eval(data_obj.get_param('hr_exipre_doc.license_project_id', 'False'))
        project_id = self.env['project.project'].browse(license_project_id)
        task = self.env['project.task'].create({
               'name': employee.hr_task_driving_license +' - '+ employee.name,
               'date_deadline': employee.hr_task_enddate_driving_license,
               'employee_id': employee.id,
               'project_id': project_id.id or license_project_id or project and project.id or False,
               'user_id': project_id.user_id.id or project.user_id and project.user_id.id or False
        })
        return task

    def task_created_permit(self, employee, project):
        data_obj = self.env['ir.config_parameter'].sudo()
        permit_project_id = safe_eval(data_obj.get_param('hr_exipre_doc.permit_project_id', 'False'))
        project_id = self.env['project.project'].browse(permit_project_id)
        task = self.env['project.task'].create({
               'name': employee.hr_task_work_permit +' - '+ employee.name,
               'date_deadline': employee.hr_task_enddate_work_permit,
               'employee_id': employee.id,
               'project_id': project_id.id or permit_project_id or project and project.id or False,
               'user_id': project_id.user_id.id or project.user_id and project.user_id.id or False
        })
        return task

    @api.model
    def task_create(self):
        emp_ids = self.search([])
        project_obj = self.env['project.project']
        today = datetime.date.today()
        for employee in emp_ids:
            if employee.hr_task_certificate1 and employee.hr_task_enddate_certificate1:
                if employee.certificate1_duration:
                        project_certificate1 = project_obj.search([('name', '=', 'Certificaat 1')])
                        if employee.certificate1_duration == 'one_week':
                            cirty1_date = datetime.datetime.strptime(
                                employee.hr_task_enddate_certificate1, DFORMAT)
                            day_time = cirty1_date - datetime.timedelta(days=7)
                            day = day_time.date()
                            if day == today:
                                self.task_created_serty1(employee, project_certificate1)
                        elif employee.certificate1_duration == 'two_week':
                            cirty1_date = datetime.datetime.strptime(
                                   employee.hr_task_enddate_certificate1, DFORMAT)
                            day_time = cirty1_date - datetime.timedelta(days=14)
                            day = day_time.date()
                            if day == today:
                                self.task_created_serty1(employee, project_certificate1)
                        elif employee.certificate1_duration == 'one_month':
                            cirty1_date = datetime.datetime.strptime(
                                   employee.hr_task_enddate_certificate1, DFORMAT)
                            day_time = cirty1_date - datetime.timedelta(days=30)
                            day = day_time.date()
                            if day == today:
                                self.task_created_serty1(employee, project_certificate1)
                        elif employee.certificate1_duration == 'two_month':
                            cirty1_date = datetime.datetime.strptime(
                                employee.hr_task_enddate_certificate1, DFORMAT)
                            day_time = cirty1_date - datetime.timedelta(days=60)
                            day = day_time.date()
                            if day == today:
                                self.task_created_serty1(employee, project_certificate1)
                        elif employee.certificate1_duration == 'three_month':
                            cirty1_date = datetime.datetime.strptime(
                                   employee.hr_task_enddate_certificate1, DFORMAT)
                            day_time = cirty1_date - datetime.timedelta(days=90)
                            day = day_time.date()
                            if day == today:
                                self.task_created_serty1(employee, project_certificate1)
                        elif employee.certificate1_duration == 'six_month':
                            cirty1_date = datetime.datetime.strptime(
                                employee.hr_task_enddate_certificate1, DFORMAT)
                            day_time = cirty1_date - datetime.timedelta(days=180)
                            day = day_time.date()
                            if day == today:
                                self.task_created_serty1(employee, project_certificate1)
                        elif employee.certificate1_duration == 'twelve_month':
                            cirty1_date = datetime.datetime.strptime(
                                   employee.hr_task_enddate_certificate1, DFORMAT)
                            day_time = cirty1_date - datetime.timedelta(days=365)
                            day = day_time.date()
                            if day == today:
                                self.task_created_serty1(employee, project_certificate1)
                if employee.hr_task_certificate2 and employee.hr_task_enddate_certificate2:
                    if employee.certificate2_duration:
                        project_certificate2 = project_obj.search([('name', '=', 'Certificaat 2')])
                        if employee.certificate2_duration == 'one_week':
                            cirty2_date = datetime.datetime.strptime(
                                   employee.hr_task_enddate_certificate2, DFORMAT)
                            cirty2_day_time = cirty2_date - datetime.timedelta(days=7)
                            cirty2_day = cirty2_day_time.date()
                            if cirty2_day == today:
                                self.task_created_serty2(employee, project_certificate2)
                        elif employee.certificate2_duration == 'two_week':
                            cirty2_date = datetime.datetime.strptime(
                                   employee.hr_task_enddate_certificate2, DFORMAT)
                            cirty2_day_time = cirty2_date - datetime.timedelta(days=14)
                            cirty2_day = cirty2_day_time.date()
                            if cirty2_day == today:
                                self.task_created_serty2(employee, project_certificate2)
                        elif employee.certificate2_duration == 'one_month':
                            cirty2_date = datetime.datetime.strptime(
                                employee.hr_task_enddate_certificate2, DFORMAT)
                            cirty2_day_time = cirty2_date - datetime.timedelta(days=30)
                            cirty2_day = cirty2_day_time.date()
                            if cirty2_day == today:
                                self.task_created_serty2(employee, project_certificate2)
                        elif employee.certificate2_duration == 'two_month':
                            cirty2_date = datetime.datetime.strptime(
                                employee.hr_task_enddate_certificate2, DFORMAT)
                            cirty2_day_time = cirty2_date - datetime.timedelta(days=60)
                            cirty2_day = cirty2_day_time.date()
                            if cirty2_day == today:
                                self.task_created_serty2(employee, project_certificate2)
                        elif employee.certificate2_duration == 'three_month':
                            cirty2_date = datetime.datetime.strptime(
                                employee.hr_task_enddate_certificate2, DFORMAT)
                            cirty2_day_time = cirty2_date - datetime.timedelta(days=90)
                            cirty2_day = cirty2_day_time.date()
                            if cirty2_day == today:
                                self.task_created_serty2(employee, project_certificate2)
                        elif employee.certificate2_duration == 'six_month':
                            cirty2_date = datetime.datetime.strptime(
                                employee.hr_task_enddate_certificate2, DFORMAT)
                            cirty2_day_time = cirty2_date - datetime.timedelta(days=180)
                            cirty2_day = cirty2_day_time.date()
                            if cirty2_day == today:
                                self.task_created_serty2(employee, project_certificate2)
                        elif employee.certificate2_duration == 'twelve_month':
                            cirty2_date = datetime.datetime.strptime(
                                   employee.hr_task_enddate_certificate2, DFORMAT)
                            cirty2_day_time = cirty2_date - datetime.timedelta(days=365)
                            cirty2_day = cirty2_day_time.date()
                            if cirty2_day == today:
                                self.task_created_serty2(employee, project_certificate2)
                if employee.hr_task_certificate3 and employee.hr_task_enddate_certificate3:
                    if employee.certificate3_duration:
                        project_certificate3 = project_obj.search([('name', '=', 'Certificaat 3')])
                        if employee.certificate3_duration == 'one_week':
                            cirty3_date = datetime.datetime.strptime(
                                employee.hr_task_enddate_certificate3, DFORMAT)
                            cirty3_day_time = cirty3_date - datetime.timedelta(days=7)
                            city3_day = cirty3_day_time.date()
                            if city3_day == today:
                                self.task_created_serty3(employee, project_certificate3)
                        elif employee.certificate3_duration == 'two_week':
                            cirty3_date = datetime.datetime.strptime(
                                employee.hr_task_enddate_certificate3, DFORMAT)
                            cirty3_day_time = cirty3_date - datetime.timedelta(days=14)
                            city3_day = cirty3_day_time.date()
                            if city3_day == today:
                                self.task_created_serty3(employee, project_certificate3)
                        elif employee.certificate3_duration == 'one_month':
                            cirty3_date = datetime.datetime.strptime(
                                employee.hr_task_enddate_certificate3, DFORMAT)
                            cirty3_day_time = cirty3_date - datetime.timedelta(days=30)
                            city3_day = cirty3_day_time.date()
                            if city3_day == today:
                                self.task_created_serty3(employee, project_certificate3)
                        elif employee.certificate3_duration == 'two_month':
                            cirty3_date = datetime.datetime.strptime(
                                employee.hr_task_enddate_certificate3, DFORMAT)
                            cirty3_day_time = cirty3_date - datetime.timedelta(days=60)
                            city3_day = cirty3_day_time.date()
                            if city3_day == today:
                                self.task_created_serty3(employee, project_certificate3)
                        elif employee.certificate3_duration == 'three_month':
                            cirty3_date = datetime.datetime.strptime(
                                employee.hr_task_enddate_certificate3, DFORMAT)
                            cirty3_day_time = cirty3_date - datetime.timedelta(days=90)
                            city3_day = cirty3_day_time.date()
                            if city3_day == today:
                                self.task_created_serty3(employee, project_certificate3)
                        elif employee.certificate3_duration == 'six_month':
                            cirty3_date = datetime.datetime.strptime(
                                employee.hr_task_enddate_certificate3, DFORMAT)
                            cirty3_day_time = cirty3_date - datetime.timedelta(days=180)
                            city3_day = cirty3_day_time.date()
                            if city3_day == today:
                                self.task_created_serty3(employee, project_certificate3)
                        elif employee.certificate3_duration == 'twelve_month':
                            cirty3_date = datetime.datetime.strptime(
                                employee.hr_task_enddate_certificate3, DFORMAT)
                            cirty3_day_time = cirty3_date - datetime.timedelta(days=365)
                            city3_day = cirty3_day_time.date()
                            if city3_day == today:
                                self.task_created_serty3(employee, project_certificate3)

                if employee.hr_task_certificate4 and employee.hr_task_enddate_certificate4:
                    if employee.certificate4_duration:
                        project_certificate4 = project_obj.search([('name', '=', 'Certificaat 4')])
                        if employee.certificate4_duration == 'one_week':
                            cirty4_date = datetime.datetime.strptime(
                                employee.hr_task_enddate_certificate4, DFORMAT)
                            cirty4_day_time = cirty4_date - datetime.timedelta(days=7)
                            city4_day = cirty4_day_time.date()
                            if city4_day == today:
                                self.task_created_serty4(employee, project_certificate4)
                        elif employee.certificate4_duration == 'two_week':
                            cirty4_date = datetime.datetime.strptime(
                                employee.hr_task_enddate_certificate4, DFORMAT)
                            cirty4_day_time = cirty4_date - datetime.timedelta(days=14)
                            city4_day = cirty4_day_time.date()
                            if city4_day == today:
                                self.task_created_serty4(employee, project_certificate4)
                        elif employee.certificate4_duration == 'one_month':
                            cirty4_date = datetime.datetime.strptime(
                                employee.hr_task_enddate_certificate4, DFORMAT)
                            cirty4_day_time = cirty4_date - datetime.timedelta(days=30)
                            city4_day = cirty4_day_time.date()
                            if city4_day == today:
                                self.task_created_serty4(employee, project_certificate4)
                        elif employee.certificate4_duration == 'two_month':
                            cirty4_date = datetime.datetime.strptime(
                                employee.hr_task_enddate_certificate4, DFORMAT)
                            cirty4_day_time = cirty4_date - datetime.timedelta(days=60)
                            city4_day = cirty4_day_time.date()
                            if city4_day == today:
                                self.task_created_serty4(employee, project_certificate4)
                        elif employee.certificate4_duration == 'three_month':
                            cirty4_date = datetime.datetime.strptime(
                                employee.hr_task_enddate_certificate4, DFORMAT)
                            cirty4_day_time = cirty4_date - datetime.timedelta(days=90)
                            city4_day = cirty4_day_time.date()
                            if city4_day == today:
                                self.task_created_serty4(employee, project_certificate4)
                        elif employee.certificate4_duration == 'six_month':
                            cirty4_date = datetime.datetime.strptime(
                                employee.hr_task_enddate_certificate4, DFORMAT)
                            cirty4_day_time = cirty4_date - datetime.timedelta(days=180)
                            city4_day = cirty4_day_time.date()
                            if city4_day == today:
                                self.task_created_serty4(employee, project_certificate4)
                        elif employee.certificate4_duration == 'twelve_month':
                            cirty4_date = datetime.datetime.strptime(
                                employee.hr_task_enddate_certificate4, DFORMAT)
                            cirty4_day_time = cirty4_date - datetime.timedelta(days=365)
                            city4_day = cirty4_day_time.date()
                            if city4_day == today:
                                self.task_created_serty4(employee, project_certificate4)

                if employee.hr_task_certificate5 and employee.hr_task_enddate_certificate5:
                    if employee.certificate5_duration:
                        project_certificate5 = project_obj.search([('name', '=', 'Certificaat 5')])
                        if employee.certificate5_duration == 'one_week':
                            cirty5_date = datetime.datetime.strptime(
                                employee.hr_task_enddate_certificate5, DFORMAT)
                            cirty5_day_time = cirty5_date - datetime.timedelta(days=7)
                            city5_day = cirty5_day_time.date()
                            if city5_day == today:
                                self.task_created_serty5(employee, project_certificate5)
                        elif employee.certificate5_duration == 'two_week':
                            cirty5_date = datetime.datetime.strptime(
                                employee.hr_task_enddate_certificate5, DFORMAT)
                            cirty5_day_time = cirty5_date - datetime.timedelta(days=14)
                            city5_day = cirty5_day_time.date()
                            if city5_day == today:
                                self.task_created_serty5(employee, project_certificate5)
                        elif employee.certificate5_duration == 'one_month':
                            cirty5_date = datetime.datetime.strptime(
                                employee.hr_task_enddate_certificate5, DFORMAT)
                            cirty5_day_time = cirty5_date - datetime.timedelta(days=30)
                            city5_day = cirty5_day_time.date()
                            if city5_day == today:
                                self.task_created_serty5(employee, project_certificate5)
                        elif employee.certificate5_duration == 'two_month':
                            cirty5_date = datetime.datetime.strptime(
                                employee.hr_task_enddate_certificate5, DFORMAT)
                            cirty5_day_time = cirty5_date - datetime.timedelta(days=60)
                            city5_day = cirty5_day_time.date()
                            if city5_day == today:
                                self.task_created_serty5(employee, project_certificate5)
                        elif employee.certificate5_duration == 'three_month':
                            cirty5_date = datetime.datetime.strptime(
                                employee.hr_task_enddate_certificate5, DFORMAT)
                            cirty5_day_time = cirty5_date - datetime.timedelta(days=90)
                            city5_day = cirty5_day_time.date()
                            if city5_day == today:
                                self.task_created_serty5(employee, project_certificate5)
                        elif employee.certificate5_duration == 'six_month':
                            cirty5_date = datetime.datetime.strptime(
                                employee.hr_task_enddate_certificate5, DFORMAT)
                            cirty5_day_time = cirty5_date - datetime.timedelta(days=180)
                            city5_day = cirty5_day_time.date()
                            if city5_day == today:
                                self.task_created_serty5(employee, project_certificate5)
                        elif employee.certificate5_duration == 'twelve_month':
                            cirty5_date = datetime.datetime.strptime(
                                employee.hr_task_enddate_certificate5, DFORMAT)
                            cirty5_day_time = cirty5_date - datetime.timedelta(days=365)
                            city5_day = cirty5_day_time.date()
                            if city5_day == today:
                                self.task_created_serty5(employee, project_certificate5)

                if employee.hr_task_certificate6 and employee.hr_task_enddate_certificate6:
                    if employee.certificate6_duration:
                        project_certificate6 = project_obj.search([('name', '=', 'Certificaat 6')])
                        if employee.certificate6_duration == 'one_week':
                            cirty6_date = datetime.datetime.strptime(
                                employee.hr_task_enddate_certificate6, DFORMAT)
                            cirty6_day_time = cirty6_date - datetime.timedelta(days=7)
                            city6_day = cirty6_day_time.date()
                            if city6_day == today:
                                self.task_created_serty6(employee, project_certificate6)
                        elif employee.certificate6_duration == 'two_week':
                            cirty6_date = datetime.datetime.strptime(
                                employee.hr_task_enddate_certificate6, DFORMAT)
                            cirty6_day_time = cirty6_date - datetime.timedelta(days=14)
                            city6_day = cirty6_day_time.date()
                            if city6_day == today:
                                self.task_created_serty6(employee, project_certificate6)
                        elif employee.certificate6_duration == 'one_month':
                            cirty6_date = datetime.datetime.strptime(
                                employee.hr_task_enddate_certificate6, DFORMAT)
                            cirty6_day_time = cirty6_date - datetime.timedelta(days=30)
                            city6_day = cirty6_day_time.date()
                            if city6_day == today:
                                self.task_created_serty6(employee, project_certificate6)
                        elif employee.certificate6_duration == 'two_month':
                            cirty6_date = datetime.datetime.strptime(
                                employee.hr_task_enddate_certificate6, DFORMAT)
                            cirty6_day_time = cirty6_date - datetime.timedelta(days=60)
                            city6_day = cirty6_day_time.date()
                            if city6_day == today:
                                self.task_created_serty6(employee, project_certificate6)
                        elif employee.certificate6_duration == 'three_month':
                            cirty6_date = datetime.datetime.strptime(
                                employee.hr_task_enddate_certificate6, DFORMAT)
                            cirty6_day_time = cirty6_date - datetime.timedelta(days=90)
                            city6_day = cirty6_day_time.date()
                            if city6_day == today:
                                self.task_created_serty6(employee, project_certificate6)
                        elif employee.certificate6_duration == 'six_month':
                            cirty6_date = datetime.datetime.strptime(
                                employee.hr_task_enddate_certificate6, DFORMAT)
                            cirty6_day_time = cirty6_date - datetime.timedelta(days=180)
                            city6_day = cirty6_day_time.date()
                            if city6_day == today:
                                self.task_created_serty6(employee, project_certificate6)
                        elif employee.certificate6_duration == 'twelve_month':
                            cirty6_date = datetime.datetime.strptime(
                                employee.hr_task_enddate_certificate6, DFORMAT)
                            cirty6_day_time = cirty6_date - datetime.timedelta(days=365)
                            city6_day = cirty6_day_time.date()
                            if city6_day == today:
                                self.task_created_serty6(employee, project_certificate6)

                if employee.hr_task_certificate7 and employee.hr_task_enddate_certificate7:
                    if employee.certificate7_duration:
                        project_certificate7 = project_obj.search([('name', '=', 'Certificaat 7')])
                        if employee.certificate7_duration == 'one_week':
                            cirty7_date = datetime.datetime.strptime(
                                employee.hr_task_enddate_certificate7, DFORMAT)
                            cirty7_day_time = cirty7_date - datetime.timedelta(days=7)
                            city7_day = cirty7_day_time.date()
                            if city7_day == today:
                                self.task_created_serty7(employee, project_certificate7)
                        elif employee.certificate7_duration == 'two_week':
                            cirty7_date = datetime.datetime.strptime(
                                employee.hr_task_enddate_certificate7, DFORMAT)
                            cirty7_day_time = cirty7_date - datetime.timedelta(days=14)
                            city7_day = cirty7_day_time.date()
                            if city7_day == today:
                                self.task_created_serty7(employee, project_certificate7)
                        elif employee.certificate7_duration == 'one_month':
                            cirty7_date = datetime.datetime.strptime(
                                employee.hr_task_enddate_certificate7, DFORMAT)
                            cirty7_day_time = cirty7_date - datetime.timedelta(days=30)
                            city7_day = cirty7_day_time.date()
                            if city7_day == today:
                                self.task_created_serty7(employee, project_certificate7)
                        elif employee.certificate7_duration == 'two_month':
                            cirty7_date = datetime.datetime.strptime(
                                employee.hr_task_enddate_certificate7, DFORMAT)
                            cirty7_day_time = cirty7_date - datetime.timedelta(days=60)
                            city7_day = cirty7_day_time.date()
                            if city7_day == today:
                                self.task_created_serty7(employee, project_certificate7)
                        elif employee.certificate7_duration == 'three_month':
                            cirty7_date = datetime.datetime.strptime(
                                employee.hr_task_enddate_certificate7, DFORMAT)
                            cirty7_day_time = cirty7_date - datetime.timedelta(days=90)
                            city7_day = cirty7_day_time.date()
                            if city7_day == today:
                                self.task_created_serty7(employee, project_certificate7)
                        elif employee.certificate7_duration == 'six_month':
                            cirty7_date = datetime.datetime.strptime(
                                employee.hr_task_enddate_certificate7, DFORMAT)
                            cirty7_day_time = cirty7_date - datetime.timedelta(days=180)
                            city7_day = cirty7_day_time.date()
                            if city7_day == today:
                                self.task_created_serty7(employee, project_certificate7)
                        elif employee.certificate7_duration == 'twelve_month':
                            cirty7_date = datetime.datetime.strptime(
                                employee.hr_task_enddate_certificate7, DFORMAT)
                            cirty7_day_time = cirty7_date - datetime.timedelta(days=365)
                            city7_day = cirty7_day_time.date()
                            if city7_day == today:
                                self.task_created_serty7(employee, project_certificate7)

                if employee.hr_task_certificate8 and employee.hr_task_enddate_certificate8:
                    if employee.certificate8_duration:
                        project_certificate8 = project_obj.search([('name', '=', 'Certificaat 8')])
                        if employee.certificate8_duration == 'one_week':
                            cirty8_date = datetime.datetime.strptime(
                                employee.hr_task_enddate_certificate8, DFORMAT)
                            cirty8_day_time = cirty8_date - datetime.timedelta(days=7)
                            city8_day = cirty8_day_time.date()
                            if city8_day == today:
                                self.task_created_serty8(employee, project_certificate8)
                        elif employee.certificate8_duration == 'two_week':
                            cirty8_date = datetime.datetime.strptime(
                                employee.hr_task_enddate_certificate8, DFORMAT)
                            cirty8_day_time = cirty8_date - datetime.timedelta(days=14)
                            city8_day = cirty8_day_time.date()
                            if city8_day == today:
                                self.task_created_serty8(employee, project_certificate8)
                        elif employee.certificate8_duration == 'one_month':
                            cirty8_date = datetime.datetime.strptime(
                                employee.hr_task_enddate_certificate8, DFORMAT)
                            cirty8_day_time = cirty8_date - datetime.timedelta(days=30)
                            city8_day = cirty8_day_time.date()
                            if city8_day == today:
                                self.task_created_serty8(employee, project_certificate8)
                        elif employee.certificate8_duration == 'two_month':
                            cirty8_date = datetime.datetime.strptime(
                                employee.hr_task_enddate_certificate8, DFORMAT)
                            cirty8_day_time = cirty8_date - datetime.timedelta(days=60)
                            city8_day = cirty8_day_time.date()
                            if city8_day == today:
                                self.task_created_serty8(employee, project_certificate8)
                        elif employee.certificate8_duration == 'three_month':
                            cirty8_date = datetime.datetime.strptime(
                                employee.hr_task_enddate_certificate8, DFORMAT)
                            cirty8_day_time = cirty8_date - datetime.timedelta(days=90)
                            city8_day = cirty8_day_time.date()
                            if city8_day == today:
                                self.task_created_serty8(employee, project_certificate8)
                        elif employee.certificate8_duration == 'six_month':
                            cirty8_date = datetime.datetime.strptime(
                                employee.hr_task_enddate_certificate8, DFORMAT)
                            cirty8_day_time = cirty8_date - datetime.timedelta(days=180)
                            city8_day = cirty8_day_time.date()
                            if city8_day == today:
                                self.task_created_serty8(employee, project_certificate8)
                        elif employee.certificate8_duration == 'twelve_month':
                            cirty8_date = datetime.datetime.strptime(
                                employee.hr_task_enddate_certificate8, DFORMAT)
                            cirty8_day_time = cirty8_date - datetime.timedelta(days=365)
                            city8_day = cirty8_day_time.date()
                            if city8_day == today:
                                self.task_created_serty8(employee, project_certificate8)

                if employee.hr_task_certificate9 and employee.hr_task_enddate_certificate9:
                    if employee.certificate9_duration:
                        project_certificate9 = project_obj.search([('name', '=', 'Certificaat 9')])
                        if employee.certificate9_duration == 'one_week':
                            cirty9_date = datetime.datetime.strptime(
                                employee.hr_task_enddate_certificate9, DFORMAT)
                            cirty9_day_time = cirty9_date - datetime.timedelta(days=7)
                            city9_day = cirty9_day_time.date()
                            if city9_day == today:
                                self.task_created_serty9(employee, project_certificate9)
                        elif employee.certificate9_duration == 'two_week':
                            cirty9_date = datetime.datetime.strptime(
                                employee.hr_task_enddate_certificate9, DFORMAT)
                            cirty9_day_time = cirty9_date - datetime.timedelta(days=14)
                            city9_day = cirty9_day_time.date()
                            if city9_day == today:
                                self.task_created_serty9(employee, project_certificate9)
                        elif employee.certificate9_duration == 'one_month':
                            cirty9_date = datetime.datetime.strptime(
                                employee.hr_task_enddate_certificate9, DFORMAT)
                            cirty9_day_time = cirty9_date - datetime.timedelta(days=30)
                            city9_day = cirty9_day_time.date()
                            if city9_day == today:
                                self.task_created_serty9(employee, project_certificate9)
                        elif employee.certificate9_duration == 'two_month':
                            cirty9_date = datetime.datetime.strptime(
                                employee.hr_task_enddate_certificate9, DFORMAT)
                            cirty9_day_time = cirty9_date - datetime.timedelta(days=60)
                            city9_day = cirty9_day_time.date()
                            if city9_day == today:
                                self.task_created_serty9(employee, project_certificate9)
                        elif employee.certificate9_duration == 'three_month':
                            cirty9_date = datetime.datetime.strptime(
                                employee.hr_task_enddate_certificate9, DFORMAT)
                            cirty9_day_time = cirty9_date - datetime.timedelta(days=90)
                            city9_day = cirty9_day_time.date()
                            if city9_day == today:
                                self.task_created_serty9(employee, project_certificate9)
                        elif employee.certificate9_duration == 'six_month':
                            cirty9_date = datetime.datetime.strptime(
                                employee.hr_task_enddate_certificate9, DFORMAT)
                            cirty9_day_time = cirty9_date - datetime.timedelta(days=180)
                            city9_day = cirty9_day_time.date()
                            if city9_day == today:
                                self.task_created_serty9(employee, project_certificate9)
                        elif employee.certificate9_duration == 'twelve_month':
                            cirty9_date = datetime.datetime.strptime(
                                employee.hr_task_enddate_certificate9, DFORMAT)
                            cirty9_day_time = cirty9_date - datetime.timedelta(days=365)
                            city9_day = cirty9_day_time.date()
                            if city9_day == today:
                                self.task_created_serty9(employee, project_certificate9)

                if employee.hr_task_certificate10 and employee.hr_task_enddate_certificate10:
                    if employee.certificate10_duration:
                        project_certificate10 = project_obj.search([('name', '=', 'Certificaat 10')])
                        if employee.certificate10_duration == 'one_week':
                            cirty10_date = datetime.datetime.strptime(
                                employee.hr_task_enddate_certificate10, DFORMAT)
                            cirty10_day_time = cirty10_date - datetime.timedelta(days=7)
                            city10_day = cirty10_day_time.date()
                            if city10_day == today:
                                self.task_created_serty10(employee, project_certificate10)
                        elif employee.certificate10_duration == 'two_week':
                            cirty10_date = datetime.datetime.strptime(
                                employee.hr_task_enddate_certificate10, DFORMAT)
                            cirty10_day_time = cirty10_date - datetime.timedelta(days=14)
                            city10_day = cirty10_day_time.date()
                            if city10_day == today:
                                self.task_created_serty10(employee, project_certificate10)
                        elif employee.certificate10_duration == 'one_month':
                            cirty10_date = datetime.datetime.strptime(
                                employee.hr_task_enddate_certificate10, DFORMAT)
                            cirty10_day_time = cirty10_date - datetime.timedelta(days=30)
                            city10_day = cirty10_day_time.date()
                            if city10_day == today:
                                self.task_created_serty10(employee, project_certificate10)
                        elif employee.certificate10_duration == 'two_month':
                            cirty10_date = datetime.datetime.strptime(
                                employee.hr_task_enddate_certificate10, DFORMAT)
                            cirty10_day_time = cirty10_date - datetime.timedelta(days=60)
                            city10_day = cirty10_day_time.date()
                            if city10_day == today:
                                self.task_created_serty10(employee, project_certificate10)
                        elif employee.certificate10_duration == 'three_month':
                            cirty10_date = datetime.datetime.strptime(
                                employee.hr_task_enddate_certificate10, DFORMAT)
                            cirty10_day_time = cirty10_date - datetime.timedelta(days=90)
                            city10_day = cirty10_day_time.date()
                            if city10_day == today:
                                self.task_created_serty10(employee, project_certificate10)
                        elif employee.certificate10_duration == 'six_month':
                            cirty10_date = datetime.datetime.strptime(
                                employee.hr_task_enddate_certificate10, DFORMAT)
                            cirty10_day_time = cirty10_date - datetime.timedelta(days=180)
                            city10_day = cirty10_day_time.date()
                            if city10_day == today:
                                self.task_created_serty10(employee, project_certificate10)
                        elif employee.certificate10_duration == 'twelve_month':
                            cirty10_date = datetime.datetime.strptime(
                                employee.hr_task_enddate_certificate10, DFORMAT)
                            cirty10_day_time = cirty10_date - datetime.timedelta(days=365)
                            city10_day = cirty10_day_time.date()
                            if city10_day == today:
                                self.task_created_serty10(employee, project_certificate10)

                if employee.hr_task_passport and employee.hr_task_enddate_passport:
                    if employee.passport_duration:
                        project_passport = project_obj.search([('name', '=', 'Paspoort')])
                        if employee.passport_duration == 'one_week':
                            passport_date = datetime.datetime.strptime(
                                employee.hr_task_enddate_passport, DFORMAT)
                            passport_day_time = passport_date - datetime.timedelta(days=7)
                            passport_day = passport_day_time.date()
                            if passport_day == today:
                                self.task_created_passport(employee, project_passport)
                        elif employee.passport_duration == 'two_week':
                            passport_date = datetime.datetime.strptime(
                                employee.hr_task_enddate_passport, DFORMAT)
                            passport_day_time = passport_date - datetime.timedelta(days=14)
                            passport_day = passport_day_time.date()
                            if passport_day == today:
                                self.task_created_passport(employee, project_passport)
                        elif employee.passport_duration == 'one_month':
                            passport_date = datetime.datetime.strptime(
                                employee.hr_task_enddate_passport, DFORMAT)
                            passport_day_time = passport_date - datetime.timedelta(days=30)
                            passport_day = passport_day_time.date()
                            if passport_day == today:
                                self.task_created_passport(employee, project_passport)
                        elif employee.passport_duration == 'two_month':
                            passport_date = datetime.datetime.strptime(
                                employee.hr_task_enddate_passport, DFORMAT)
                            passport_day_time = passport_date - datetime.timedelta(days=60)
                            passport_day = passport_day_time.date()
                            if passport_day == today:
                                self.task_created_passport(employee, project_passport)
                        elif employee.passport_duration == 'three_month':
                            passport_date = datetime.datetime.strptime(
                                employee.hr_task_enddate_passport, DFORMAT)
                            passport_day_time = passport_date - datetime.timedelta(days=90)
                            passport_day = passport_day_time.date()
                            if passport_day == today:
                                self.task_created_passport(employee, project_passport)
                        elif employee.passport_duration == 'six_month':
                            passport_date = datetime.datetime.strptime(
                                employee.hr_task_enddate_passport, DFORMAT)
                            passport_day_time = passport_date - datetime.timedelta(days=180)
                            passport_day = passport_day_time.date()
                            if passport_day == today:
                                self.task_created_passport(employee, project_passport)
                        elif employee.passport_duration == 'twelve_month':
                            passport_date = datetime.datetime.strptime(
                                employee.hr_task_enddate_passport, DFORMAT)
                            passport_day_time = passport_date - datetime.timedelta(days=365)
                            passport_day = passport_day_time.date()
                            if passport_day == today:
                                self.task_created_passport(employee, project_passport)
                if employee.hr_task_identification and employee.hr_task_enddate_identification:
                    if employee.id_duration:
                        project_identification = project_obj.search([('name', '=', 'ID')])
                        if employee.id_duration == 'one_week':
                            id_date = datetime.datetime.strptime(
                                employee.hr_task_enddate_identification, DFORMAT)
                            id_day_time = id_date - datetime.timedelta(days=7)
                            id_day = id_day_time.date()
                            if id_day == today:
                                self.task_created_id(employee, project_identification)
                        elif employee.id_duration == 'two_week':
                            id_date = datetime.datetime.strptime(
                                employee.hr_task_enddate_identification, DFORMAT)
                            id_day_time = id_date - datetime.timedelta(days=14)
                            id_day = id_day_time.date()
                            if id_day == today:
                                self.task_created_id(employee, project_identification)
                        elif employee.id_duration == 'one_month':
                            id_date = datetime.datetime.strptime(
                                employee.hr_task_enddate_identification, DFORMAT)
                            id_day_time = id_date - datetime.timedelta(days=30)
                            id_day = id_day_time.date()
                            if id_day == today:
                                self.task_created_id(employee, project_identification)
                        elif employee.id_duration == 'two_month':
                            id_date = datetime.datetime.strptime(
                                employee.hr_task_enddate_identification, DFORMAT)
                            id_day_time = id_date - datetime.timedelta(days=60)
                            id_day = id_day_time.date()
                            if id_day == today:
                                self.task_created_id(employee, project_identification)
                        elif employee.id_duration == 'three_month':
                            id_date = datetime.datetime.strptime(
                                employee.hr_task_enddate_identification, DFORMAT)
                            id_day_time = id_date - datetime.timedelta(days=90)
                            id_day = id_day_time.date()
                            if id_day == today:
                                self.task_created_id(employee, project_identification)
                        elif employee.id_duration == 'six_month':
                            id_date = datetime.datetime.strptime(
                                employee.hr_task_enddate_identification, DFORMAT)
                            id_day_time = id_date - datetime.timedelta(days=180)
                            id_day = id_day_time.date()
                            if id_day == today:
                                self.task_created_id(employee, project_identification)
                        elif employee.id_duration == 'twelve_month':
                            id_date = datetime.datetime.strptime(
                                employee.hr_task_enddate_identification, DFORMAT)
                            id_day_time = id_date - datetime.timedelta(days=365)
                            id_day = id_day_time.date()
                            if id_day == today:
                                self.task_created_id(employee, project_identification)
                if employee.hr_task_driving_license and employee.hr_task_enddate_driving_license:
                    if employee.licence_duration:
                        project_licence = project_obj.search([('name', '=', 'Rijbewijs')])
                        if employee.licence_duration == 'one_week':
                            licence_date = datetime.datetime.strptime(
                                employee.hr_task_enddate_driving_license, DFORMAT)
                            licence_day_time = licence_date - datetime.timedelta(days=7)
                            licence_day = licence_day_time.date()
                            if licence_day == today:
                                self.task_created_licence(employee, project_licence)
                        elif employee.licence_duration == 'two_week':
                            licence_date = datetime.datetime.strptime(
                                employee.hr_task_enddate_driving_license, DFORMAT)
                            licence_day_time = licence_date - datetime.timedelta(days=14)
                            licence_day = licence_day_time.date()
                            if licence_day == today:
                                self.task_created_licence(employee, project_licence)
                        elif employee.licence_duration == 'one_month':
                            licence_date = datetime.datetime.strptime(
                                employee.hr_task_enddate_driving_license, DFORMAT)
                            licence_day_time = licence_date - datetime.timedelta(days=30)
                            licence_day = licence_day_time.date()
                            if licence_day == today:
                                self.task_created_licence(employee, project_licence)
                        elif employee.licence_duration == 'two_month':
                            licence_date = datetime.datetime.strptime(
                                employee.hr_task_enddate_driving_license, DFORMAT)
                            licence_day_time = licence_date - datetime.timedelta(days=60)
                            licence_day = licence_day_time.date()
                            if licence_day == today:
                                self.task_created_licence(employee, project_licence)
                        elif employee.licence_duration == 'three_month':
                            licence_date = datetime.datetime.strptime(
                                employee.hr_task_enddate_driving_license, DFORMAT)
                            licence_day_time = licence_date - datetime.timedelta(days=90)
                            licence_day = licence_day_time.date()
                            if licence_day == today:
                                self.task_created_licence(employee, project_licence)
                        elif employee.licence_duration == 'six_month':
                            licence_date = datetime.datetime.strptime(
                                employee.hr_task_enddate_driving_license, DFORMAT)
                            licence_day_time = licence_date - datetime.timedelta(days=180)
                            licence_day = licence_day_time.date()
                            if licence_day == today:
                                self.task_created_licence(employee, project_licence)
                        elif employee.licence_duration == 'twelve_month':
                            licence_date = datetime.datetime.strptime(
                                employee.hr_task_enddate_driving_license, DFORMAT)
                            licence_day_time = licence_date - datetime.timedelta(days=365)
                            licence_day = licence_day_time.date()
                            if licence_day == today:
                                self.task_created_licence(employee, project_licence)
                if employee.hr_task_work_permit and employee.hr_task_enddate_work_permit:
                    if employee.work_permit_duration:
                        project_permit = project_obj.search([('name', '=', 'Werkvergunning')])
                        if employee.work_permit_duration == 'one_week':
                            permit_date = datetime.datetime.strptime(
                                employee.hr_task_enddate_work_permit, DFORMAT)
                            permit_day_time = permit_date - datetime.timedelta(days=7)
                            permit_day = permit_day_time.date()
                            if permit_day == today:
                                self.task_created_permit(employee, project_permit)
                        elif employee.work_permit_duration == 'two_week':
                            permit_date = datetime.datetime.strptime(
                                employee.hr_task_enddate_work_permit, DFORMAT)
                            permit_day_time = permit_date - datetime.timedelta(days=14)
                            permit_day = permit_day_time.date()
                            if permit_day == today:
                                self.task_created_permit(employee, project_permit)
                        elif employee.work_permit_duration == 'one_month':
                            permit_date = datetime.datetime.strptime(
                                employee.hr_task_enddate_work_permit, DFORMAT)
                            permit_day_time = permit_date - datetime.timedelta(days=30)
                            permit_day = permit_day_time.date()
                            if permit_day == today:
                                self.task_created_permit(employee, project_permit)
                        elif employee.work_permit_duration == 'two_month':
                            permit_date = datetime.datetime.strptime(
                                employee.hr_task_enddate_work_permit, DFORMAT)
                            permit_day_time = permit_date - datetime.timedelta(days=60)
                            permit_day = permit_day_time.date()
                            if permit_day == today:
                                self.task_created_permit(employee, project_permit)
                        elif employee.work_permit_duration == 'three_month':
                            permit_date = datetime.datetime.strptime(
                                employee.hr_task_enddate_work_permit, DFORMAT)
                            permit_day_time = permit_date - datetime.timedelta(days=90)
                            permit_day = permit_day_time.date()
                            if permit_day == today:
                                self.task_created_permit(employee, project_permit)
                        elif employee.work_permit_duration == 'six_month':
                            permit_date = datetime.datetime.strptime(
                                employee.hr_task_enddate_work_permit, DFORMAT)
                            permit_day_time = permit_date - datetime.timedelta(days=180)
                            permit_day = permit_day_time.date()
                            if permit_day == today:
                                self.task_created_permit(employee, project_permit)
                        elif employee.work_permit_duration == 'twelve_month':
                            permit_date = datetime.datetime.strptime(
                                employee.hr_task_enddate_work_permit, DFORMAT)
                            permit_day_time = permit_date - datetime.timedelta(days=365)
                            permit_day = permit_day_time.date()
                            if permit_day == today:
                                self.task_created_permit(employee, project_permit)

    @api.onchange('hr_task_certificate1', 'hr_task_certificate2',
                  'hr_task_certificate3', 'hr_task_certificate4',
                  'hr_task_certificate5', 'hr_task_certificate6',
                  'hr_task_certificate7', 'hr_task_certificate8',
                  'hr_task_certificate9', 'hr_task_certificate10', 'hr_task_passport',
                  'hr_task_identification', 'hr_task_driving_license','hr_task_work_permit')
    def _fillDuration(self):
        data_obj = self.env['ir.config_parameter'].sudo()
        if self.hr_task_certificate1:
            certificate1_duration = data_obj.get_param('hr_exipre_doc.certificate1_duration')
            self.certificate1_duration = certificate1_duration
        if self.hr_task_certificate2:
            certificate2_duration = data_obj.get_param('hr_exipre_doc.certificate2_duration')
            self.certificate2_duration = certificate2_duration
        if self.hr_task_certificate3:
            certificate3_duration = data_obj.get_param('hr_exipre_doc.certificate3_duration')
            self.certificate3_duration = certificate3_duration
        if self.hr_task_certificate4:
            certificate4_duration = data_obj.get_param('hr_exipre_doc.certificate4_duration')
            self.certificate4_duration = certificate4_duration
        if self.hr_task_certificate5:
            certificate5_duration = data_obj.get_param('hr_exipre_doc.certificate5_duration')
            self.certificate5_duration = certificate5_duration
        if self.hr_task_certificate6:
            certificate6_duration = data_obj.get_param('hr_exipre_doc.certificate6_duration')
            self.certificate6_duration = certificate6_duration
        if self.hr_task_certificate7:
            certificate7_duration = data_obj.get_param('hr_exipre_doc.certificate7_duration')
            self.certificate7_duration = certificate7_duration
        if self.hr_task_certificate8:
            certificate8_duration = data_obj.get_param('hr_exipre_doc.certificate8_duration')
            self.certificate8_duration = certificate8_duration
        if self.hr_task_certificate9:
            certificate9_duration = data_obj.get_param('hr_exipre_doc.certificate9_duration')
            self.certificate9_duration = certificate9_duration
        if self.hr_task_certificate10:
            certificate10_duration = data_obj.get_param('hr_exipre_doc.certificate10_duration')
            self.certificate10_duration = certificate10_duration
        if self.hr_task_passport:
            passport_duration = data_obj.get_param('hr_exipre_doc.passport_duration')
            self.passport_duration = passport_duration
        if self.hr_task_identification:
            id_duration = data_obj.get_param('hr_exipre_doc.identification_duration')
            self.id_duration = id_duration
        if self.hr_task_driving_license:
            licence_duration = data_obj.get_param('hr_exipre_doc.license_duration')
            self.licence_duration = licence_duration
        if self.hr_task_work_permit:
            work_permit_duration = data_obj.get_param('hr_exipre_doc.permit_duration')
            self.work_permit_duration = work_permit_duration

class hr_exipre_doc_task(models.Model):
    _inherit = 'project.task'

    employee_id = fields.Many2one('hr.employee', string='Employee')


class hr_exipre_doc_config(models.TransientModel):
    _name = 'hr_employee.config.settings'
    _inherit = 'res.config.settings'

    certificate1_label = fields.Selection([
              ('hr_task_certificate1', 'Certificaat 1'),], string='Certificate 1')
    certificate2_label = fields.Selection([
              ('hr_task_certificate2', 'Certificaat 2'),], string='Certificate 2')
    certificate3_label = fields.Selection([
              ('hr_task_certificate3', 'Certificaat 3'),], string='Certificate 3')
    certificate4_label = fields.Selection([
              ('hr_task_certificate4', 'Certificaat 4'),], string='Certificate 4')
    certificate5_label = fields.Selection([
              ('hr_task_certificate5', 'Certificaat 5'),], string='Certificate 5')
    certificate6_label = fields.Selection([
              ('hr_task_certificate6', 'Certificaat 6'),], string='Certificate 6')
    certificate7_label = fields.Selection([
              ('hr_task_certificate7', 'Certificaat 7'),], string='Certificate 7')
    certificate8_label = fields.Selection([
              ('hr_task_certificate8', 'Certificaat 8'),], string='Certificate 8')
    certificate9_label = fields.Selection([
              ('hr_task_certificate9', 'Certificaat 9'),], string='Certificate 9')
    certificate10_label = fields.Selection([
              ('hr_task_certificate10', 'Certificaat 10'),], string='Certificate 10')
    passport_label = fields.Selection([
              ('hr_task_passport', 'Paspoort'),], string='Paspoort')
    identification_label = fields.Selection([
              ('hr_task_identification', 'ID'),], string='ID')
    license_label = fields.Selection([
              ('hr_task_driving_license', 'Rijbewijs'),], string='Rijbewijs')
    work_permit_label = fields.Selection([
              ('hr_task_work_permit', 'Werkvergunning'),], string='Werkvergunning')    

    certificate1_project_id = fields.Many2one('project.project', string='Project')
    certificate2_project_id = fields.Many2one('project.project', string='Project')
    certificate3_project_id = fields.Many2one('project.project', string='Project')
    certificate4_project_id = fields.Many2one('project.project', string='Project')
    certificate5_project_id = fields.Many2one('project.project', string='Project')
    certificate6_project_id = fields.Many2one('project.project', string='Project')
    certificate7_project_id = fields.Many2one('project.project', string='Project')
    certificate8_project_id = fields.Many2one('project.project', string='Project')
    certificate9_project_id = fields.Many2one('project.project', string='Project')
    certificate10_project_id = fields.Many2one('project.project', string='Project')
    passport_project_id = fields.Many2one('project.project', string='Project')
    identification_project_id = fields.Many2one('project.project', string='Project')
    license_project_id = fields.Many2one('project.project', string='Project')
    permit_project_id = fields.Many2one('project.project', string='Project')
    
    certificate1_duration = fields.Selection([
            ('one_week', '1 Week'),
            ('two_week', '2 Week'),
            ('one_month', '1 Month'),
            ('two_month', '2 Month'),
            ('three_month', '3 Month'),
            ('six_month', '6 Month'),
            ('twelve_month', '12 Month')
        ], string='Duration')
    certificate2_duration = fields.Selection([
            ('one_week', '1 Week'),
            ('two_week', '2 Week'),
            ('one_month', '1 Month'),
            ('two_month', '2 Month'),
            ('three_month', '3 Month'),
            ('six_month', '6 Month'),
            ('twelve_month', '12 Month')
        ], string='Duration')
    certificate3_duration = fields.Selection([
            ('one_week', '1 Week'),
            ('two_week', '2 Week'),
            ('one_month', '1 Month'),
            ('two_month', '2 Month'),
            ('three_month', '3 Month'),
            ('six_month', '6 Month'),
            ('twelve_month', '12 Month')
        ], string='Duration')
    certificate4_duration = fields.Selection([
            ('one_week', '1 Week'),
            ('two_week', '2 Week'),
            ('one_month', '1 Month'),
            ('two_month', '2 Month'),
            ('three_month', '3 Month'),
            ('six_month', '6 Month'),
            ('twelve_month', '12 Month')
        ], string='Duration')
    certificate5_duration = fields.Selection([
            ('one_week', '1 Week'),
            ('two_week', '2 Week'),
            ('one_month', '1 Month'),
            ('two_month', '2 Month'),
            ('three_month', '3 Month'),
            ('six_month', '6 Month'),
            ('twelve_month', '12 Month')
        ], string='Duration')
    certificate6_duration = fields.Selection([
            ('one_week', '1 Week'),
            ('two_week', '2 Week'),
            ('one_month', '1 Month'),
            ('two_month', '2 Month'),
            ('three_month', '3 Month'),
            ('six_month', '6 Month'),
            ('twelve_month', '12 Month')
        ], string='Duration')
    certificate7_duration = fields.Selection([
            ('one_week', '1 Week'),
            ('two_week', '2 Week'),
            ('one_month', '1 Month'),
            ('two_month', '2 Month'),
            ('three_month', '3 Month'),
            ('six_month', '6 Month'),
            ('twelve_month', '12 Month')
        ], string='Duration')
    certificate8_duration = fields.Selection([
            ('one_week', '1 Week'),
            ('two_week', '2 Week'),
            ('one_month', '1 Month'),
            ('two_month', '2 Month'),
            ('three_month', '3 Month'),
            ('six_month', '6 Month'),
            ('twelve_month', '12 Month')
        ], string='Duration')
    certificate9_duration = fields.Selection([
            ('one_week', '1 Week'),
            ('two_week', '2 Week'),
            ('one_month', '1 Month'),
            ('two_month', '2 Month'),
            ('three_month', '3 Month'),
            ('six_month', '6 Month'),
            ('twelve_month', '12 Month')
        ], string='Duration')
    certificate10_duration = fields.Selection([
            ('one_week', '1 Week'),
            ('two_week', '2 Week'),
            ('one_month', '1 Month'),
            ('two_month', '2 Month'),
            ('three_month', '3 Month'),
            ('six_month', '6 Month'),
            ('twelve_month', '12 Month')
        ], string='Duration')
    passport_duration = fields.Selection([
            ('one_week', '1 Week'),
            ('two_week', '2 Week'),
            ('one_month', '1 Month'),
            ('two_month', '2 Month'),
            ('three_month', '3 Month'),
            ('six_month', '6 Month'),
            ('twelve_month', '12 Month')
        ], string='Duration')
    identification_duration = fields.Selection([
            ('one_week', '1 Week'),
            ('two_week', '2 Week'),
            ('one_month', '1 Month'),
            ('two_month', '2 Month'),
            ('three_month', '3 Month'),
            ('six_month', '6 Month'),
            ('twelve_month', '12 Month')
        ], string='Duration')
    license_duration = fields.Selection([
            ('one_week', '1 Week'),
            ('two_week', '2 Week'),
            ('one_month', '1 Month'),
            ('two_month', '2 Month'),
            ('three_month', '3 Month'),
            ('six_month', '6 Month'),
            ('twelve_month', '12 Month')
        ], string='Duration')
    permit_duration = fields.Selection([
            ('one_week', '1 Week'),
            ('two_week', '2 Week'),
            ('one_month', '1 Month'),
            ('two_month', '2 Month'),
            ('three_month', '3 Month'),
            ('six_month', '6 Month'),
            ('twelve_month', '12 Month')
        ], string='Duration')

    @api.multi
    def get_default_fields_value(self, fields):
        params = self.env['ir.config_parameter']
        certificate1_label = params.get_param('hr_exipre_doc.certificate1_label')
        certificate2_label = params.get_param('hr_exipre_doc.certificate2_label')
        certificate3_label = params.get_param('hr_exipre_doc.certificate3_label')
        certificate4_label = params.get_param('hr_exipre_doc.certificate4_label')
        certificate5_label = params.get_param('hr_exipre_doc.certificate5_label')
        certificate6_label = params.get_param('hr_exipre_doc.certificate6_label')
        certificate7_label = params.get_param('hr_exipre_doc.certificate7_label')
        certificate8_label = params.get_param('hr_exipre_doc.certificate8_label')
        certificate9_label = params.get_param('hr_exipre_doc.certificate9_label')
        certificate10_label = params.get_param('hr_exipre_doc.certificate10_label')
        passport_label = params.get_param('hr_exipre_doc.passport_label')
        identification_label = params.get_param('hr_exipre_doc.identification_label')
        license_label = params.get_param('hr_exipre_doc.license_label')
        work_permit_label = params.get_param('hr_exipre_doc.work_permit_label')

        certificate1_project_id = safe_eval(params.get_param('hr_exipre_doc.certificate1_project_id', 'False'))
        certificate2_project_id = safe_eval(params.get_param('hr_exipre_doc.certificate2_project_id', 'False'))
        certificate3_project_id = safe_eval(params.get_param('hr_exipre_doc.certificate3_project_id', 'False'))
        certificate4_project_id = safe_eval(params.get_param('hr_exipre_doc.certificate4_project_id', 'False'))
        certificate5_project_id = safe_eval(params.get_param('hr_exipre_doc.certificate5_project_id', 'False'))
        certificate6_project_id = safe_eval(params.get_param('hr_exipre_doc.certificate6_project_id', 'False'))
        certificate7_project_id = safe_eval(params.get_param('hr_exipre_doc.certificate7_project_id', 'False'))
        certificate8_project_id = safe_eval(params.get_param('hr_exipre_doc.certificate8_project_id', 'False'))
        certificate9_project_id = safe_eval(params.get_param('hr_exipre_doc.certificate9_project_id', 'False'))
        certificate10_project_id = safe_eval(params.get_param('hr_exipre_doc.certificate10_project_id', 'False'))
        passport_project_id = safe_eval(params.get_param('hr_exipre_doc.passport_project_id', 'False'))
        identification_project_id = safe_eval(params.get_param('hr_exipre_doc.identification_project_id', 'False'))
        license_project_id = safe_eval(params.get_param('hr_exipre_doc.license_project_id', 'False'))
        permit_project_id = safe_eval(params.get_param('hr_exipre_doc.permit_project_id', 'False'))

        certificate1_duration = params.get_param('hr_exipre_doc.certificate1_duration')
        certificate2_duration = params.get_param('hr_exipre_doc.certificate2_duration')
        certificate3_duration = params.get_param('hr_exipre_doc.certificate3_duration')
        certificate4_duration = params.get_param('hr_exipre_doc.certificate4_duration')
        certificate5_duration = params.get_param('hr_exipre_doc.certificate5_duration')
        certificate6_duration = params.get_param('hr_exipre_doc.certificate6_duration')
        certificate7_duration = params.get_param('hr_exipre_doc.certificate7_duration')
        certificate8_duration = params.get_param('hr_exipre_doc.certificate8_duration')
        certificate9_duration = params.get_param('hr_exipre_doc.certificate9_duration')
        certificate10_duration = params.get_param('hr_exipre_doc.certificate10_duration')
        passport_duration = params.get_param('hr_exipre_doc.passport_duration')
        identification_duration = params.get_param('hr_exipre_doc.identification_duration')
        license_duration = params.get_param('hr_exipre_doc.license_duration')
        permit_duration = params.get_param('hr_exipre_doc.permit_duration')

        return {'certificate1_label': certificate1_label,
                'certificate2_label': certificate2_label,
                'certificate3_label': certificate3_label,
                'certificate4_label': certificate4_label,
                'certificate5_label': certificate5_label,
                'certificate6_label': certificate6_label,
                'certificate7_label': certificate7_label,
                'certificate8_label': certificate8_label,
                'certificate9_label': certificate9_label,
                'certificate10_label': certificate10_label,
                'passport_label': passport_label,
                'identification_label': identification_label,
                'license_label': license_label,
                'work_permit_label': work_permit_label,
                'certificate1_project_id': certificate1_project_id,
                'certificate2_project_id': certificate2_project_id,
                'certificate3_project_id': certificate3_project_id,
                'certificate4_project_id': certificate4_project_id,
                'certificate5_project_id': certificate5_project_id,
                'certificate6_project_id': certificate6_project_id,
                'certificate7_project_id': certificate7_project_id,
                'certificate8_project_id': certificate8_project_id,
                'certificate9_project_id': certificate9_project_id,
                'certificate10_project_id': certificate10_project_id,
                'passport_project_id': passport_project_id,
                'identification_project_id': identification_project_id,
                'license_project_id': license_project_id,
                'permit_project_id': permit_project_id,
                'certificate1_duration': certificate1_duration,
                'certificate2_duration': certificate2_duration,
                'certificate3_duration': certificate3_duration,
                'certificate4_duration': certificate4_duration,
                'certificate5_duration': certificate5_duration,
                'certificate6_duration': certificate6_duration,
                'certificate7_duration': certificate7_duration,
                'certificate8_duration': certificate8_duration,
                'certificate9_duration': certificate9_duration,
                'certificate10_duration': certificate10_duration,
                'passport_duration': passport_duration,
                'identification_duration': identification_duration,
                'license_duration': license_duration,
                'permit_duration': permit_duration}

    @api.multi
    def set_default_fields_value(self):
        params = self.env['ir.config_parameter']
        params.set_param('hr_exipre_doc.certificate1_label', self.certificate1_label)
        params.set_param('hr_exipre_doc.certificate2_label', self.certificate2_label)
        params.set_param('hr_exipre_doc.certificate3_label', self.certificate3_label)
        params.set_param('hr_exipre_doc.certificate4_label', self.certificate4_label)
        params.set_param('hr_exipre_doc.certificate5_label', self.certificate5_label)
        params.set_param('hr_exipre_doc.certificate6_label', self.certificate6_label)
        params.set_param('hr_exipre_doc.certificate7_label', self.certificate7_label)
        params.set_param('hr_exipre_doc.certificate8_label', self.certificate8_label)
        params.set_param('hr_exipre_doc.certificate9_label', self.certificate9_label)
        params.set_param('hr_exipre_doc.certificate10_label', self.certificate10_label)
        params.set_param('hr_exipre_doc.passport_label', self.passport_label)
        params.set_param('hr_exipre_doc.identification_label', self.identification_label)
        params.set_param('hr_exipre_doc.license_label', self.license_label)
        params.set_param('hr_exipre_doc.work_permit_label', self.work_permit_label)

        params.set_param('hr_exipre_doc.certificate1_project_id', repr(self.certificate1_project_id.id))
        params.set_param('hr_exipre_doc.certificate2_project_id', repr(self.certificate2_project_id.id))
        params.set_param('hr_exipre_doc.certificate3_project_id', repr(self.certificate3_project_id.id))
        params.set_param('hr_exipre_doc.certificate4_project_id', repr(self.certificate4_project_id.id))
        params.set_param('hr_exipre_doc.certificate5_project_id', repr(self.certificate5_project_id.id))
        params.set_param('hr_exipre_doc.certificate6_project_id', repr(self.certificate6_project_id.id))
        params.set_param('hr_exipre_doc.certificate7_project_id', repr(self.certificate7_project_id.id))
        params.set_param('hr_exipre_doc.certificate8_project_id', repr(self.certificate8_project_id.id))
        params.set_param('hr_exipre_doc.certificate9_project_id', repr(self.certificate9_project_id.id))
        params.set_param('hr_exipre_doc.certificate10_project_id', repr(self.certificate10_project_id.id))
        params.set_param('hr_exipre_doc.passport_project_id', repr(self.passport_project_id.id))
        params.set_param('hr_exipre_doc.identification_project_id', repr(self.identification_project_id.id))
        params.set_param('hr_exipre_doc.license_project_id', repr(self.license_project_id.id))
        params.set_param('hr_exipre_doc.permit_project_id', repr(self.permit_project_id.id))

        params.set_param('hr_exipre_doc.certificate1_duration', self.certificate1_duration)
        params.set_param('hr_exipre_doc.certificate2_duration', self.certificate2_duration)
        params.set_param('hr_exipre_doc.certificate3_duration', self.certificate3_duration)
        params.set_param('hr_exipre_doc.certificate4_duration', self.certificate4_duration)
        params.set_param('hr_exipre_doc.certificate5_duration', self.certificate5_duration)
        params.set_param('hr_exipre_doc.certificate6_duration', self.certificate6_duration)
        params.set_param('hr_exipre_doc.certificate7_duration', self.certificate7_duration)
        params.set_param('hr_exipre_doc.certificate8_duration', self.certificate8_duration)
        params.set_param('hr_exipre_doc.certificate9_duration', self.certificate9_duration)
        params.set_param('hr_exipre_doc.certificate10_duration', self.certificate10_duration)
        params.set_param('hr_exipre_doc.passport_duration', self.passport_duration)
        params.set_param('hr_exipre_doc.identification_duration', self.identification_duration)
        params.set_param('hr_exipre_doc.license_duration', self.license_duration)
        params.set_param('hr_exipre_doc.permit_duration', self.permit_duration)

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
