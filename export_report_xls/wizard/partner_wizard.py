# -*- coding: utf-8 -*-
from openerp import tools,models, fields, api, _
import xlwt
from xlsxwriter.workbook import Workbook
from cStringIO import StringIO
from datetime import datetime
class AccountInvoiceRefund(models.TransientModel):

    _name = "partner.export.wizard"
    _description = "Partner Export Wizard"

    partner_ids = fields.Many2many('res.partner',string='Partner')


    @api.multi
    def partner_export_excel(self):
        partner_obj = self.env['res.partner']
        result = []
        if self.partner_ids:
            account_number = ''
            for partner in self.partner_ids:
                account_name = partner.property_account_payable_id.name
                account_code = partner.property_account_payable_id.ac_code
                Verzamelrekening = account_code
                if partner.bank_ids:
                    account_number =  partner.bank_ids[0].acc_number
                finalstreet = ''
                mainstreet = partner.street
                if mainstreet:
                    if len(mainstreet) > 2:
                        street = mainstreet.replace(' ','')
                        finalstreet = street[0:-2] + ' ' + street[-2] + street[-1]
                    else:
                        finalstreet = mainstreet
                result.append({
                   'relatienummer': partner and partner.ref or '',
                   'zoekcode': partner and partner.ref or '',
                   'bedrijfsnaam': partner.name or '',
                   'verzamelrekening': Verzamelrekening or '',
                   'adres': finalstreet or '',
                   'postcode': partner.zip or '',
                   'plaats': partner.city or '',
                   'land': partner.country_id and partner.country_id.name or '',
                   'fax': partner.fax or '',
                   'telefoon_zakelijk': partner.phone or '',
                   'telefoon_mobiel': partner.mobile or '',
                   'email': partner.email or '',
                   'website': partner.website or '',
                   'bankrekeningnummer': account_number or '',
                   
                })
                partner.write({'export_date':datetime.today(),'export':True})
        # Create an new Excel file and add a worksheet.
        import base64
        filename = 'export_report.xls'
        workbook = xlwt.Workbook()
        style = xlwt.XFStyle()
        tall_style = xlwt.easyxf('font:height 720;') # 36pt
#        ok_style = xlwt.easyxf('pattern: fore_colour light_blue;''font: colour green, bold True;') 
        # Create a font to use with the style
        font = xlwt.Font()
        font.name = 'Times New Roman'
        font.bold = True
        font.height = 250
        style.font = font
        worksheet = workbook.add_sheet('Sheet 1')
        #worksheet.write(0,2, 'Export Customer', style)

        zero_col = worksheet.col(0)
        zero_col.width = 236 * 30
        second_col = worksheet.col(3)
        second_col.width = 236 * 30
        third_col = worksheet.col(2)
        third_col.width = 236 * 60

        fourth_col = worksheet.col(4)
        fourth_col.width = 236 * 60

        first_row = worksheet.row(2)
        first_row.set_style(tall_style)
        
        first_col = worksheet.col(1)
        first_col.width = 156 * 30
        
        fifth_col = worksheet.col(4)
        fifth_col.width = 156 * 30

        user_col = worksheet.col(5)
        user_col.width = 156 * 30

        
        six_col = worksheet.col(6)
        six_col.width = 236 * 60
        

        worksheet.write(0, 0, 'Relatienummer', style)
        worksheet.write(0, 1, 'Zoekcode', style)
        worksheet.write(0, 2, 'Bedrijfsnaam', style)
        worksheet.write(0, 3, 'Verzamelrekening', style)
        worksheet.write(0, 4, 'Adres', style)
        worksheet.write(0, 5, 'Postcode', style)
        worksheet.write(0, 6, 'Plaats', style)
        worksheet.write(0, 7, 'Land', style)
        worksheet.write(0, 8, 'Fax', style)
        worksheet.write(0, 9, 'Telefoon zakelijk', style)
        worksheet.write(0, 10, 'Telefoon mobiel', style)
        worksheet.write(0, 11, 'Mail', style)
        worksheet.write(0, 12, 'Website', style)
        worksheet.write(0, 13, 'Bankrekeningnummer', style)


        row_2 = 1
        for val in result:
            worksheet.write(row_2, 0, tools.ustr(val['relatienummer']))
            worksheet.write(row_2, 1, tools.ustr(val['zoekcode']))
            worksheet.write(row_2, 2, tools.ustr(val['bedrijfsnaam']))
            worksheet.write(row_2, 3, tools.ustr(val['verzamelrekening']))
            worksheet.write(row_2, 4, tools.ustr(val['adres']))
            worksheet.write(row_2, 5, tools.ustr(val['postcode']))
            worksheet.write(row_2, 6, tools.ustr(val['plaats']))
            worksheet.write(row_2, 7, tools.ustr(val['land']))
            worksheet.write(row_2, 8, tools.ustr(val['fax']))
            worksheet.write(row_2, 9, tools.ustr(val['telefoon_zakelijk']))
            worksheet.write(row_2, 10,tools.ustr(val['telefoon_mobiel']))
            worksheet.write(row_2, 11,tools.ustr(val['email']))
            worksheet.write(row_2, 12,tools.ustr(val['website']))
            worksheet.write(row_2, 13,tools.ustr(val['bankrekeningnummer']))
            row_2+=1

        
        fp = StringIO()
        workbook.save(fp)
        export_id = self.env['partner.excel'].create({'excel_file': base64.encodestring(fp.getvalue()), 'file_name': filename})
        fp.close()
        
        return {
            'view_mode': 'form',
            'res_id': export_id.id,
            'res_model': 'partner.excel',
            'view_type': 'form',
            'type': 'ir.actions.act_window',
            'target': 'new',
        }
        return True

     


class partner_excel(models.TransientModel):
    _name= "partner.excel"
    _description = "Partner Excel Report"

    excel_file = fields.Binary('Excel Report for Partners')
    file_name = fields.Char('Excel File', size=64)

