import json
from odoo import models
from odoo.exceptions import UserError


class GenerateXLSXReport(models.Model):
    _name = 'report.de_payslip_salary_report.payslip_salary_report_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, lines):
        format1 = workbook.add_format({'font_size': '12', 'align': 'vcenter', 'bold': True})
        sheet = workbook.add_worksheet('Salary Details Report')
        sr_no = 1
        sheet.write(3, 0, 'Sr.#', format1)
        sheet.write(3, 1, 'Company Name', format1)
        sheet.write(3, 2, 'Location', format1)
        sheet.write(3, 3, 'Cc', format1)
        sheet.write(3, 4, 'Ccd', format1)
        sheet.write(3, 5, 'Dept Name', format1)
        sheet.write(3, 6, 'Period', format1)
        sheet.write(3, 7, 'Emp code', format1)
        sheet.write(3, 8, 'Name', format1)
        sheet.write(3, 9, 'Doj', format1)
        sheet.write(3, 10, 'Dob', format1)
        sheet.write(3, 11, 'Position', format1)
        sheet.write(3, 12, 'Desig Name', format1)
        sheet.write(3, 13, 'Grade', format1)
        sheet.write(3, 14, 'Grade Type', format1)
        sheet.write(3, 15, 'Emp type', format1)
        sheet.write(3, 16, 'Nic No.', format1)
        sheet.write(3, 17, 'Ipl Variable Cost', format1)
        sheet.write(3, 18, 'Act Gross', format1)
        sheet.write(3, 19, 'Bank Name', format1)
        sheet.write(3, 20, 'Bank Account', format1)
        sheet.write(3, 21, 'Days', format1)
        sheet.write(3, 22, 'Ot hours', format1)
        sheet.write(3, 23, 'Basic salry', format1)
        sheet.write(3, 24, 'Hr', format1)
        sheet.write(3, 25, 'conv', format1)
        sheet.write(3, 26, 'Util', format1)
        sheet.write(3, 27, 'Car Allowance', format1)
        sheet.write(3, 28, 'Spcl All', format1)
        sheet.write(3, 29, 'Gross', format1)
        sheet.write(3, 30, 'Accmdtn', format1)
        sheet.write(3, 31, 'Sal Adj Alwn', format1)
        sheet.write(3, 32, 'Washing', format1)
        sheet.write(3, 33, 'Shift All', format1)
        sheet.write(3, 34, 'Bonus', format1)
        sheet.write(3, 35, 'Arrears', format1)
        sheet.write(3, 36, 'Overtime', format1)
        sheet.write(3, 37, 'Site All', format1)
        sheet.write(3, 38, 'Food Acc Allowance', format1)

        
        format2 = workbook.add_format({'font_size': '12', 'align': 'vcenter'})
        row = 4
        sheet.set_column(row, 0, 50)
        sheet.set_column(row, 1, 25)
        sheet.set_column(row, 2, 25)
        sheet.set_column(row, 3, 25)
        sheet.set_column(row, 4, 25)
        sheet.set_column(row, 5, 25)
        sheet.set_column(row, 6, 25)
        sheet.set_column(row, 7, 25)
        sheet.set_column(row, 8, 25)
        sheet.set_column(row, 9, 25)
        sheet.set_column(row, 10, 25)
        sheet.set_column(row, 11, 25)
        sheet.set_column(row, 12, 25)
        sheet.set_column(row, 13, 25)
        sheet.set_column(row, 14, 25)
        sheet.set_column(row, 15, 25)
        sheet.set_column(row, 16, 25)
        sheet.set_column(row, 17, 25)
        sheet.set_column(row, 18, 25)
        sheet.set_column(row, 19, 25)
        sheet.set_column(row, 20, 25)
        sheet.set_column(row, 21, 25)
        sheet.set_column(row, 22, 25)
        sheet.set_column(row, 23, 25)
        sheet.set_column(row, 24, 25)
        sheet.set_column(row, 25, 25)
        sheet.set_column(row, 26, 25)
        sheet.set_column(row, 27, 25)
        sheet.set_column(row, 28, 25)
        sheet.set_column(row, 29, 25)
        sheet.set_column(row, 30, 25)
        sheet.set_column(row, 31, 25)
        sheet.set_column(row, 32, 25)
        sheet.set_column(row, 33, 25)
        sheet.set_column(row, 34, 25)
        sheet.set_column(row, 35, 25)
        sheet.set_column(row, 36, 25)
        sheet.set_column(row, 37, 25)
        sheet.set_column(row, 38, 25)






        
        
        
        for id in lines:
            if id.date_end:
                date_end = id.date_end
                date_end = date_end.strftime("%d/%m/%Y")
            else:
                date_end = None
            payslips = self.env['hr.payslip'].search([('payslip_run_id','=',id.name)])
            for payslip in payslips:
                if payslip.company_id:
                    company = payslip.company_id.name
                else:
                    company = None
                    
                employee = self.env['hr.employee'].search([('name','=',payslip.employee_id.name)])[0]
                
                if employee.department_id:
                    department = employee.department_id.name
                else:
                    department = None
                
                if employee.work_location:
                    location = employee.work_location
                else:
                    location = None
                if employee.name:
                    name = employee.name
                else:
                    name = None
                
                if employee.date:
                    doj = employee.date
                    doj = doj.strftime("%d-%b-%y")
                else:
                    doj = None
                 
                if employee.birthday:
                    dob = employee.birthday
                    dob = dob.strftime("%d-%b-%y")
                else:
                    dob = None
                
                if employee.job_id:
                    job_position = employee.job_id.name
                else:
                    job_position = None
                
                if employee.cnic:
                    cnic = employee.cnic
                else:
                    cnic = None
                
                if employee.bank_account_id.bank_id:
                    bank_name = employee.bank_account_id.bank_id.name
                else:
                    bank_name = None
                
                if employee.bank_account_id:
                    bank_account = employee.bank_account_id.acc_number
                else:
                    bank_account = None
                
                if employee.grade_designation:
                    grade_designation = employee.grade_designation.name
                else:
                    grade_designation = None
                
                if employee.grade_type:
                    grade_type = employee.grade_type.name
                else:
                    grade_type = None
                    
                basic_salry = 0
                salry = self.env['hr.payslip'].search([('employee_id','=',employee.id),], limit=1)
                for basic in salry.line_ids:
                    if basic.code == 'BASIC':
                        basic_salry = basic.amount
                    
                    
                over_time_works = 0
                time = self.env['hr.payslip'].search([('employee_id','=',employee.id),], limit=1)
                for extra_hourse in time.worked_days_line_ids:
                    if extra_hourse.work_entry_type_id.code in ("Normal OT","Gazetted OT","Rest Day OT"):
                         over_time_works = overtime_work_days + extra_hourse.number_of_hours
                    
                total_days = 0
                days = self.env['hr.payslip'].search([('employee_id','=',employee.id),], limit=1)
                for workday in days.worked_days_line_ids:
                    if workday.work_entry_type_id.code != "ABSENT100":
                        total_days = total_days + workday.number_of_days
                        
                gross_salry = 0
                payroll = self.env['hr.payslip'].search([('employee_id','=',employee.id),], limit=1)
                for payslip_line in payroll.line_ids:
                    if payslip_line.code == 'GROSS':
                        gross_salry = payslip_line.amount
                        
                        
                gross_sal = 0
                gross = self.env['hr.payslip'].search([('employee_id','=',employee.id),], limit=1)
                for gros_line in gross.line_ids:
                    if gros_line.code == 'GROSS':
                        gross_sal = gros_line.amount        
                        
                House_rent = 0
                Hr_rent = self.env['hr.contract'].search([('employee_id','=',employee.id)],limit=1)
                for benifit_line in Hr_rent.benefit_line_ids:
                    if benifit_line.input_type_id.code == 'HR01':
                        House_rent = benifit_line.amount
                        
                        
                Food_Acc_Allowance = 0
                Hr_rent = self.env['hr.contract'].search([('employee_id','=',employee.id)],limit=1)
                for benifit_line in Hr_rent.benefit_line_ids:
                    if benifit_line.input_type_id.code == 'FAA01':
                        Food_Acc_Allowance = benifit_line.amount         
                        
                        
                Site_All = 0
                Hr_rent = self.env['hr.contract'].search([('employee_id','=',employee.id)],limit=1)
                for benifit_line in Hr_rent.benefit_line_ids:
                    if benifit_line.input_type_id.code == 'STA01':
                        Site_All = benifit_line.amount        
                        
                        
                        
                Overtime = 0
                Hr_rent = self.env['hr.contract'].search([('employee_id','=',employee.id)],limit=1)
                for benifit_line in Hr_rent.benefit_line_ids:
                    if benifit_line.input_type_id.code == 'OT100':
                        Overtime = benifit_line.amount        
                        
                        
                special_allown = 0
                spec_allwn = self.env['hr.contract'].search([('employee_id','=',employee.id)],limit=1)
                for spec_line in spec_allwn.benefit_line_ids:
                    if spec_line.input_type_id.code == 'SP01':
                        special_allown = spec_line.amount   
                        
                        
                Bonus = 0
                spec_allwn = self.env['hr.contract'].search([('employee_id','=',employee.id)],limit=1)
                for spec_line in spec_allwn.benefit_line_ids:
                    if spec_line.input_type_id.code == 'B01':
                        Bonus = spec_line.amount         
                        
                        
                        
                Utilities_bills = 0
                Ut_bill = self.env['hr.contract'].search([('employee_id','=',employee.id)],limit=1)
                for utlity_line in Ut_bill.benefit_line_ids:
                    if utlity_line.input_type_id.code == 'UT01':
                        Utilities_bills = utlity_line.amount
                        
                        
                        
                Shift_bills = 0
                shft_bill = self.env['hr.contract'].search([('employee_id','=',employee.id)],limit=1)
                for utlity_line in Ut_bill.benefit_line_ids:
                    if utlity_line.input_type_id.code == 'SA01':
                        Utilities_bills = utlity_line.amount        

                    
                Conv_allown = 0
                conv = self.env['hr.contract'].search([('employee_id','=',employee.id)],limit=1)
                for benifit in conv.benefit_line_ids:
                    if benifit.input_type_id.code == 'CO01':
                        Conv_allown = benifit.amount 
                        
                accomadation_allwn = 0
                acc = self.env['hr.contract'].search([('employee_id','=',employee.id)],limit=1)
                for benifit in acc.benefit_line_ids:
                    if benifit.input_type_id.code == 'ACC01':
                        accomadation_allwn = benifit.amount       
                        
                        
                        
                Car_allown = 0
                car_all = self.env['hr.contract'].search([('employee_id','=',employee.id)],limit=1)
                for car in car_all.benefit_line_ids:
                    if car.input_type_id.code == 'CAR01':
                        Car_allown = car.amount 
                        
                        
                salry_allown = 0
                sal_all = self.env['hr.contract'].search([('employee_id','=',employee.id)],limit=1)
                for sal in sal_all.benefit_line_ids:
                    if sal.input_type_id.code == 'SAR':
                        salry_allown = sal.amount  
                        
                        
                Arrears = 0
                sal_all = self.env['hr.contract'].search([('employee_id','=',employee.id)],limit=1)
                for sal in sal_all.benefit_line_ids:
                    if sal.input_type_id.code == 'ARR01':
                        Arrears = sal.amount         
                        
                washing = 0
                was_all = self.env['hr.contract'].search([('employee_id','=',employee.id)],limit=1)
                for was in was_all.benefit_line_ids:
                    if was.input_type_id.code == 'WA01':
                        washing = was.amount         
                        
                        
        
                cost_account = ' '    
                contract = self.env['hr.contract'].search([('employee_id','=',employee.id)], limit=1)  
                for cost_line in contract.cost_center_information_line:
                    cost_account = cost_line.cost_center_id.name
                sheet.set_column('A:A', 5,)
                sheet.write(row, 0, sr_no, format2)
                sheet.write(row, 1, company, format2)
                sheet.write(row, 2, location, format2)
                sheet.write(row, 3, employee.company_id.segment1, format2)
                sheet.write(row, 4, cost_account, format2)
                sheet.write(row, 5, department, format2)
                sheet.write(row, 6, date_end, format2)
                sheet.write(row, 7, employee.emp_number, format2)
                sheet.write(row, 8, name, format2)
                sheet.write(row, 9, doj, format2)
                sheet.write(row, 10, dob, format2)
                sheet.write(row, 11, job_position, format2)
                sheet.write(row, 12, employee.job_title, format2)
                sheet.write(row, 13, grade_designation, format2)
                sheet.write(row, 14, grade_type, format2)
                sheet.write(row, 15, employee.emp_type, format2)
                sheet.write(row, 16, cnic, format2)
                sheet.write(row, 17, employee.ipl_variable, format2)
                sheet.write(row, 18, gross_salry, format2)
                sheet.write(row, 19, bank_name, format2)
                sheet.write(row, 20, bank_account, format2)
                sheet.write(row, 21, total_days, format2)
                sheet.write(row, 22, over_time_works, format2)
                sheet.write(row, 23, basic_salry, format2)
                sheet.write(row, 24, House_rent, format2)
                sheet.write(row, 25, Conv_allown, format2)
                sheet.write(row, 26, Utilities_bills, format2)
                sheet.write(row, 27, Car_allown, format2)
                sheet.write(row, 28, special_allown, format2)
                sheet.write(row, 29, gross_sal, format2)
                sheet.write(row, 30, accomadation_allwn, format2), format2
                sheet.write(row, 31, salry_allown, format2)
                sheet.write(row, 32, washing, format2)
                sheet.write(row, 33, Shift_bills, format2)
                sheet.write(row, 34, Bonus, format2)
                sheet.write(row, 35, Arrears, format2)
                sheet.write(row, 36, Overtime, format2)
                sheet.write(row, 37, Site_All, format2)
                sheet.write(row, 38, Food_Acc_Allowance, format2)

                row = row + 1
                
                
                    