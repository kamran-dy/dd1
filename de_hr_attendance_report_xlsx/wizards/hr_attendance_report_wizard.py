# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class HrAttendanceReportExcelWizard(models.TransientModel):
    _name = "attendance.report.excel.wizard"
    _description = "HR Attendance Excel Report wizard"

    employee_ids = fields.Many2many('hr.employee', string='Employee')
    start_date = fields.Datetime('Start Date')
    end_date = fields.Datetime('End Date')
    
    def action_gnerate_excel(self):        
        data = {
            'employee_ids': self.employee_ids.ids,
            'start_date':self.start_date,
            'end_date':self.end_date,
            }
        return self.env.ref('de_hr_attendance_report_xlsx.attendance_report_xlsx').report_action(self, data=data)
    
