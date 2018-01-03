# -*- coding: utf-8 -*-
from openerp import tools,models, fields, api, _
import xlwt
from xlsxwriter.workbook import Workbook
from cStringIO import StringIO
from datetime import datetime

class AccountInvoiceReport(models.TransientModel):

    _name = "account.invoice.wizard"
    _description = "Account Invoice Wizard"

    invoice_ids = fields.Many2many('account.invoice',string='Invoice')


    @api.multi
    def invoice_export_excel(self):
        partner_obj = self.env['res.partner']
        invoice_obj = self.env['account.invoice']
        tax_obj = self.env['account.tax']
        result = []
        if self.invoice_ids:
            account_number = ''
            finalperiod = ''
            Omschrijving = ''
            for invoice in self.invoice_ids:
                result_line = []
                account_name = invoice.account_id.ac_code or ''
                acc = account_name
                partner = invoice.partner_id and invoice.partner_id.name or ''
                invoicenumber = invoice.number or ''
                dateinvoice = invoice.date_invoice or ''
                Omschrijving = partner + ' ' + invoicenumber + ' ' + dateinvoice
                if invoice.date_invoice:
                    finalperiod = '%02d' % datetime.strptime(invoice.date_invoice, '%Y-%m-%d').month
                for line in invoice.invoice_line_ids:
                    taxes = []
                    line_account_name = line.account_id.ac_code or ''
                    lineacc = line_account_name
                    if line.invoice_line_tax_ids:
                        for tax in line.invoice_line_tax_ids:
                            tax_id = tax_obj.search([('name','=',tax.name),('type_tax_use','=',tax.type_tax_use)])
                            if tax_id:
                                taxes.append(tax_id.id)
                    result_line.append({
                       'journal_id': invoice.journal_id and invoice.journal_id.ac_code or '',
                       'period': finalperiod or '',
                       'description': line.name or '',
                       'price_subtotal': line.price_subtotal or '',
                       'account': lineacc,
                       'currency_id': invoice.currency_id and invoice.currency_id.name or '',
                       'invoice_line_tax_id': taxes,
                    })
                result.append({
                   'Omschrijving': Omschrijving or '',
                   'journal_id': invoice.journal_id and invoice.journal_id.ac_code or '',
                   'partner_id': invoice.partner_id and invoice.partner_id.ref or '',
                   'invoice_number': invoice.number or '',
                   'period': finalperiod or '',
                   'date_invoice': invoice.date_invoice or '',
                   'date_due': invoice.date_due or '',
                   'account': acc,
                   'amount_untaxed': invoice.amount_untaxed or '',
                   'currency_id': invoice.currency_id and invoice.currency_id.name or '',
                   'invoice_line_ids':result_line,
                })
                invoice.write({'export_date':datetime.today(),'export':True})

        # Create an new Excel file and add a worksheet.
        import base64
        filename = 'account_export_report.xls'
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
        #worksheet.write(0,2, 'Export Invoice', style)

        zero_col = worksheet.col(5)
        zero_col.width = 236 * 60

        worksheet.write(0, 0, 'Header of regel', style)
        worksheet.write(0, 1, 'Dagboek', style)
        worksheet.write(0, 2, 'sub_nr', style)
        worksheet.write(0, 3, 'fact_nr', style)
        worksheet.write(0, 4, 'Periode', style)
        worksheet.write(0, 5, 'Omschrijving', style)
        worksheet.write(0, 6, 'Factuurdatum', style)
        worksheet.write(0, 7, 'Vervaldatum', style)
        worksheet.write(0, 8, 'Grootboek', style)
        worksheet.write(0, 9, 'Bedrag', style)
        worksheet.write(0, 10, 'Valuta code', style)
        worksheet.write(0, 11, 'BTW-code', style)


        row_2 = 1
        header = 0
        for val in result:
            worksheet.write(row_2, 0, header)
            worksheet.write(row_2, 1, val['journal_id'])
            worksheet.write(row_2, 2, val['partner_id'])
            worksheet.write(row_2, 3, val['invoice_number'])
            worksheet.write(row_2, 4, val['period'])
            worksheet.write(row_2, 5, val['Omschrijving'])
            worksheet.write(row_2, 6, val['date_invoice'])
            worksheet.write(row_2, 7, val['date_due'])
            worksheet.write(row_2, 9, val['amount_untaxed'])
            worksheet.write(row_2, 10,val['currency_id'])
            if val['invoice_line_ids']:
                lineheader = 1
                for valline in val['invoice_line_ids']:
                    worksheet.write(row_2+1, 0, lineheader)
                    worksheet.write(row_2+1, 1, valline['journal_id'])
                    worksheet.write(row_2+1, 2, val['partner_id'])
                    worksheet.write(row_2+1, 3, val['invoice_number'])
                    worksheet.write(row_2+1, 4, valline['period'])
                    worksheet.write(row_2+1, 5, valline['description'])
                    worksheet.write(row_2+1, 6, val['date_invoice'])
                    worksheet.write(row_2+1, 7, val['date_due'])
                    worksheet.write(row_2+1, 8, valline['account'])
                    worksheet.write(row_2+1, 9, valline['price_subtotal'])
                    worksheet.write(row_2+1, 10, valline['currency_id'])
                    if valline['invoice_line_tax_id']:
                        taxname = ''
                        for tax in tax_obj.browse(valline['invoice_line_tax_id']):
                            print "tax obj==============",tax
                            if tax.amount == 21.000:
                                #taxname = tax.tax_code_id.ac_code
                                taxname = taxname + '1' + ','
                            elif tax.amount == 6.000:
                                taxname = taxname + '2' + ','
                        worksheet.write(row_2+1, 11, taxname.rstrip(","))
                    lineheader += 1
                    row_2+=1
            row_2+=1

        
        fp = StringIO()
        workbook.save(fp)
        export_id = self.env['invoice.excel'].create({'excel_file': base64.encodestring(fp.getvalue()), 'file_name': filename})
        fp.close()
        
        return {
            'view_mode': 'form',
            'res_id': export_id.id,
            'res_model': 'invoice.excel',
            'view_type': 'form',
            'type': 'ir.actions.act_window',
            'target': 'new',
        }
        return True

     


class invoice_excel(models.TransientModel):
    _name= "invoice.excel"
    _description = "Invoice Excel Report"

    excel_file = fields.Binary('Excel Report for Invoice')
    file_name = fields.Char('Excel File', size=64)

