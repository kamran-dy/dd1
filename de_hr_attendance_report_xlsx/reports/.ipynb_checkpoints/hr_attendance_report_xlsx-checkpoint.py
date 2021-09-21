import xlwt
from odoo import models
from datetime import datetime, date
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError


class AttendanceReportXlsx(models.AbstractModel):
    _name = 'report.de_hr_attendance_report_xlsx.hr_attendance_report_xlsx'
    _inherit = 'report.report_xlsx.abstract'
    _description = 'Employee Attendance Report XLSX'
    
    def generate_xlsx_report(self, workbook, data, lines):
        #raise UserError(data['start_date'])
        start_date = data['start_date']
        end_date = data['end_date']
        period = start_date + ', ' + end_date
        
        
        employee_shift = self.env['hr.shift.schedule.line'].search([('employee_id','in',data['employee_ids']),
                                                                    ('date','>=',start_date),
                                                                   ('date','<=',end_date)])
        
        format1 = workbook.add_format({'font_size': '14', 'align': 'vcenter', 'bold': True})
        sheet = workbook.add_worksheet('Attendance Report XLSX')
        
        sheet.write(3, 0, 'Employee', format1)
        sheet.write(3, 1, employee_shift[0].employee_id.name, format1)
        sheet.write(3, 2, 'Employee No', format1)
        sheet.write(3, 3, employee_shift[0].employee_number, format1)
        sheet.write(3, 4, 'Period', format1)
        sheet.write(3, 5, period, format1)
        
        sheet.write(6, 0, 'Date', format1)
        sheet.write(6, 1, 'Days', format1)
        sheet.write(6, 2, 'CHECK IN', format1)
        sheet.write(6, 3, 'CHECK OUT', format1)
        sheet.write(6, 4, 'Hours', format1)
        sheet.write(6, 5, 'Shift Allocated', format1)
        sheet.write(6, 6, 'Rest Day', format1)
        sheet.write(6, 7, 'Remarks', format1)
        
        
        format2 = workbook.add_format({'font_size': '12', 'align': 'vcenter'})
        row = 7
        sheet.set_column(row, 0, 50)
        sheet.set_column(row, 1, 25)
        sheet.set_column(row, 2, 20)
        sheet.set_column(row, 3, 20)
        sheet.set_column(row, 4, 20)
        sheet.set_column(row, 5, 20)
        sheet.set_column(row, 6, 20)
        sheet.set_column(row, 7, 20)
        
        holidays = ['Saturday','Sunday']
        days = []
        employee_name = []
        for rec in employee_shift:
            name = rec.employee_id.name
            emp_number = rec.employee_number
            employee_name.append(name)
            date = rec.date
            date_strf = rec.date.strftime("%d/%m/%Y")
            day = rec.day.name
            if rec.first_shift_id.name:
                allocated_shift = rec.first_shift_id.name
            else:
                allocated_shift = None
            rest_day = rec.rest_day
            
            days.append(day)
            
            if (day == 'Saturday') or (day == 'Sunday'): 
                if rest_day == True:
                    rest_day = 'Y'
                else:
                    rest_day = 'N'
                #raise UserError(rest_day)
                employee_attendance_name = self.env['hr.attendance'].search([('employee_id','=',name),('att_date','=',date)])

                for attendance in employee_attendance_name:
                    attendance_date = attendance.att_date
                    checkin_strf = None
                    checkout_strf = None
                    hours = 0.0
                    if attendance.remarks:
                        remarks = attendance.remarks
                    else:
                        remarks = None

                sheet.write(row, 0, date_strf, format2)
                sheet.write(row, 1, day, format2)
                sheet.write(row, 2, checkin_strf, format2)
                sheet.write(row, 3, checkout_strf, format2)
                sheet.write(row, 4, hours, format2)
                sheet.write(row, 5, allocated_shift, format2)
                sheet.write(row, 6, rest_day, format2)
                sheet.write(row, 7, remarks, format2)

                row = row + 1
            
            else: 
                if rest_day == True:
                    rest_day = 'Y'
                else:
                    rest_day = 'N'
                #raise UserError(rest_day)
                employee_attendance_name = self.env['hr.attendance'].search([('employee_id','=',name),('att_date','=',date)])

                for attendance in employee_attendance_name:
                    attendance_date = attendance.att_date
                    if attendance.check_in and attendance.check_out:
                        check_in = attendance.check_in

                        check_out = attendance.check_out
                        checkin_strf = attendance.check_in.strftime("%d/%m/%Y %H:%M:%S")
                        checkout_strf = attendance.check_out.strftime("%d/%m/%Y %H:%M:%S")
                        diff = check_out - check_in
                        hours = diff.total_seconds() / 3600
                        hours = "{:.2f}".format(hours)
                    else:
                        if attendance.check_in:
                            check_in = attendance.check_in
                        else:
                            check_in = None
                        if attendance.check_out:
                            check_out = attendance.check_out
                        else:
                            check_out = None
                        hours = 0.0
                    if attendance.remarks:
                        remarks = attendance.remarks
                    else:
                        remarks = None

                sheet.write(row, 0, date_strf, format2)
                sheet.write(row, 1, day, format2)
                sheet.write(row, 2, checkin_strf, format2)
                sheet.write(row, 3, checkout_strf, format2)
                sheet.write(row, 4, hours, format2)
                sheet.write(row, 5, allocated_shift, format2)
                sheet.write(row, 6, rest_day, format2)
                sheet.write(row, 7, remarks, format2)

                row = row + 1
        
  