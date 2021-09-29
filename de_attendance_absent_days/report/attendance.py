from odoo import models, fields, api
from  odoo import models
from odoo.exceptions import UserError
from datetime import datetime


class EmployeeReportXlS(models.AbstractModel):
    _name = 'report.de_attendance_absent_days.attendance_report_xlx'
    _description = 'Purchase report'
    _inherit = 'report.report_xlsx.abstract'
    
    
    def action_get_abset_days(self, data):
        absent_list = []
        
        employees = self.env['hr.employee'].sudo().search([])
        if  data['company']:
            employees = self.env['hr.employee'].sudo().search([('company_id','in', data.company.ids)])
        sr_no = 1
        for employee in employees:
            leave_status = ' '
            rectification_status = ' '
            shift_lines = self.env['hr.shift.schedule.line'].sudo().search([('employee_id','=', employee.id),('date','>=',data.date_form),('date','<=',data.date_to)])
            for shift_line in shift_lines:
                attendance_exist = self.env['hr.attendance'].sudo().search([('employee_id','=', employee.id),('att_date','=',shift_line.date),('check_in','!=',False),('check_out','!=',False)])
                if not attendance_exist:
                    leave_exist = self.env['hr.leave'].sudo().search([('employee_id','=', employee.id),('request_date_from','<=', shift_line.date),('request_date_to','>=',  shift_line.date),('state','in',('validate','confirm'))], limit=1)
                    if leave_exist:
                        if leave_exist.state=='validate':                            
                            leave_status = 'Approved'
                        elif leave_exist.state=='confirm':                            
                            leave_status = 'To Approved'    
                    elif not leave_exist:
                        daily_rectify = self.env['hr.attendance.rectification'].sudo().search([('employee_id','=', employee.id),('state','in', ('approved','submitted')),('date','=',shift_line.date)], limit=1)
                        if daily_rectify.state=='approved':                            
                            rectification_status = 'Approved'
                        elif daily_rectify.state=='submitted':                            
                            rectification_status = 'To Approved'
                            
                    absent_list.append({
                         'sr_no':  sr_no,
                         'employee': employee.name,
                         'emp_code': employee.emp_number,
                         'absent_on': shift_line.date, 
                         'leave_status': leave_status,
                         'rectification_status': rectification_status,
                    })
                    sr_no += 1
        return absent_list

    def generate_xlsx_report(self, workbook, data, lines):
        company = data['company']
        docs = self.env['attendance.model'].browse(self.env.context.get('active_id'))
        sheet = workbook.add_worksheet('purchase report')
        bold = workbook. add_format({'bold': True, 'align': 'center','bg_color': '#FFFF99','border': True})
        title = workbook.add_format({'bold': True, 'align': 'center', 'font_size': 20, 'bg_color': '#FFFF99', 'border': True})
        header_row_style = workbook.add_format({'bold': True, 'align': 'center', 'border':True})
        format2 = workbook.add_format({'align': 'center'})
        company_list = ' '
        for company in docs.company:
            company_list = company.name + ' '  
            
#         sheet.merge_range('A1:F1', company_list)
#         sheet.write(2,3,'Date From', header_row_style)
#         sheet.write(2,3,docs.date_from.strftime('%d-%b-%y'), header_row_style)
#         sheet.write(2,5,'Date To', header_row_style)
#         sheet.write(2,3,docs.date_to.strftime('%d-%b-%y'), header_row_style)
        sheet.set_column(0,5,10)
        sheet.set_column('A:B', 20,)
        sheet.set_column('C:D', 20,)
        sheet.set_column('E:F', 20,)
        sheet.set_column('G:G', 20,)
        sheet.write(4,0,'Sr.#', header_row_style)
        sheet.write(4,1 , 'Employee name',header_row_style)
        sheet.write(4,2 , 'Employee code',header_row_style)
        sheet.write(4,3 , 'Absent on',header_row_style)
        sheet.write(4,4 , 'Leave status',header_row_style)
        sheet.write(4,5 , 'Rectification status',header_row_style)
        absent_list = self.action_get_abset_days(docs)  
        row = 5
        for line in absent_list:        
            sheet.write(row, 0, line['sr_no'], format2)
            sheet.write(row, 1, line['employee'], format2)
            sheet.write(row, 2, line['emp_code'], format2)            
            sheet.write(row, 3, line['absent_on'].strftime('%d-%b-%y'), format2)            
            sheet.write(row, 4, line['leave_status'], format2)            
            sheet.write(row, 5, line['rectification_status'], format2)            

            row += 1 