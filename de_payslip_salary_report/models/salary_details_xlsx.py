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
        sheet.write(3, 39, 'Mobile All', format1)
        sheet.write(3, 40, 'Incentive', format1)
        sheet.write(3, 41, 'Off Site All', format1)
        sheet.write(3, 42, 'Variable Pay', format1)
        sheet.write(3, 43, 'Variable Pay Adj', format1)
        sheet.write(3, 44, 'Shutdown_Allowance', format1)
        sheet.write(3, 45, 'Other', format1)
        sheet.write(3, 46, 'Gross payable', format1)
        sheet.write(3, 47, 'Total', format1)
        sheet.write(3, 48, 'PF', format1)
        sheet.write(3, 49, 'EOBI', format1)
        sheet.write(3, 50, 'Prof tax', format1)
        sheet.write(3, 51, 'income tax', format1)
        sheet.write(3, 52, 'Srchrg On ITax', format1)
        sheet.write(3, 53, 'Pf Loan Inst', format1)
        sheet.write(3, 54, 'Pf Loan Markup', format1)
        sheet.write(3, 55, 'Adv. Sala', format1)
        sheet.write(3, 56, 'Spcl Loan', format1)
        sheet.write(3, 57, 'Tele Communication', format1)
        sheet.write(3, 58, 'Fac', format1)
        sheet.write(3, 59, 'Variable Pay Deductions', format1)
        sheet.write(3, 60, 'Variable Pay Adj Ded', format1)
        sheet.write(3, 61, 'Misc Deduct', format1)
        sheet.write(3, 62, 'Total Ded', format1)
        sheet.write(3, 63, 'Net Payable', format1)




 



        




        
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
        sheet.set_column(row, 39, 25)
        sheet.set_column(row, 40, 25)
        sheet.set_column(row, 41, 25)
        sheet.set_column(row, 42, 25)
        sheet.set_column(row, 43, 25)
        sheet.set_column(row, 44, 25)
        sheet.set_column(row, 45, 25)
        sheet.set_column(row, 46, 25)
        sheet.set_column(row, 47, 25)
        sheet.set_column(row, 48, 25)
        sheet.set_column(row, 49, 25)
        sheet.set_column(row, 50, 25)
        sheet.set_column(row, 51, 25)
        sheet.set_column(row, 52, 25)
        sheet.set_column(row, 53, 25)
        sheet.set_column(row, 54, 25)
        sheet.set_column(row, 55, 25)
        sheet.set_column(row, 56, 25)
        sheet.set_column(row, 57, 25)
        sheet.set_column(row, 58, 25)
        sheet.set_column(row, 59, 25)
        sheet.set_column(row, 60, 25)
        sheet.set_column(row, 61, 25)
        sheet.set_column(row, 62, 25)
        sheet.set_column(row, 63, 25)


        
        over_all = 0
        tot_basic_salry = 0
        tot_House_rent = 0
        for id in lines:
            if id.date_end:
                date_end = id.date_end
                date_end = date_end.strftime("%d/%m/%Y")
            else:
                date_end = None
            payslips = self.env['hr.payslip'].search([('payslip_run_id','=',id.name)])
         
            for payslip in payslips:
                total_ded = 0
                
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
                    
                Srchrg_On_ITax =  0
                    
                    
                Prof = 0
                    
                Net_Payable = 0
                payroll = self.env['hr.payslip'].search([('employee_id','=',employee.id),], limit=1)
                for payslip_line in payroll.line_ids:
                    if payslip_line.code == 'NET':
                        Net_Payable = payslip_line.amount 
                 
                        
                 
                    
                basic_salry = 0
                salry = self.env['hr.payslip'].search([('employee_id','=',employee.id),], limit=1)
                for basic in salry.line_ids:
                    if basic.code == 'BASIC':
                        basic_salry = basic.amount     
                        tot_basic_salry += basic_salry
                    
                    
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

                        
                        
                Income_tax = 0
                payroll = self.env['hr.payslip'].search([('employee_id','=',employee.id),], limit=1)
                for payslip_line in payroll.line_ids:
                    if payslip_line.code == 'INC01':
                        Income_tax = payslip_line.amount 
               
                        
                        
                gross_sal = 0
                gross = self.env['hr.payslip'].search([('employee_id','=',employee.id),], limit=1)
                for gros_line in gross.line_ids:
                    if gros_line.category_id.code in ('BASIC', 'ALW'):
                        gross_sal = gros_line.amount  
                 
                  
                        
                gross_payable = 0
                gross = self.env['hr.payslip'].search([('employee_id','=',employee.id),], limit=1)
                for gros_line in gross.line_ids:
                    if gros_line.category_id.code in ('GROSS', 'COMP'):
                        gross_payable = gros_line.amount   
                
                        
                        
                total = 0
                gross = self.env['hr.payslip'].search([('employee_id','=',employee.id),], limit=1)
                for gros_line in gross.line_ids:
                    if gros_line.category_id.code in ('GROSS', 'COMP'):
                        total = gros_line.amount         
               
                        
                       
                        
                PF = 0
                gross = self.env['hr.payslip'].search([('employee_id','=',employee.id),], limit=1)
                for gros_line in gross.line_ids:
                    if gros_line.code in ('PF01'):
                        PF = gros_line.amount   
                   
                        
                EOBI = 0
                gross = self.env['hr.payslip'].search([('employee_id','=',employee.id),], limit=1)
                for gros_line in gross.line_ids:
                    if gros_line.code in ('EOB01'):
                        EOBI = gros_line.amount          
                
                        
                        
                House_rent = 0
                Hr_rent = self.env['hr.contract'].search([('employee_id','=',employee.id)],limit=1)
                for benifit_line in Hr_rent.benefit_line_ids:
                    if benifit_line.input_type_id.code == 'HR01':
                        House_rent = benifit_line.amount
                        tot_House_rent += House_rent
                        
                        
                Misc_Deduct = 0
                Hr_rent = self.env['hr.contract'].search([('employee_id','=',employee.id)],limit=1)
                for benifit_line in Hr_rent.benefit_line_ids:
                    if benifit_line.input_type_id.code == 'MD01':
                        Misc_Deduct = benifit_line.amount       
                    
                        
                Variable_Pay_Adj_Ded = 0
                Hr_rent = self.env['hr.contract'].search([('employee_id','=',employee.id)],limit=1)
                for benifit_line in Hr_rent.benefit_line_ids:
                    if benifit_line.input_type_id.code == 'VPA01':
                        Variable_Pay_Adj_Ded = benifit_line.amount        
                        
                    
                        
                Variable_Pay_Deductions = 0
                Hr_rent = self.env['hr.contract'].search([('employee_id','=',employee.id)],limit=1)
                for benifit_line in Hr_rent.benefit_line_ids:
                    if benifit_line.input_type_id.code == 'VP01':
                        Variable_Pay_Deductions = benifit_line.amount        
                    
                        
                        
                Fac = 0
                Hr_rent = self.env['hr.contract'].search([('employee_id','=',employee.id)],limit=1)
                for benifit_line in Hr_rent.benefit_line_ids:
                    if benifit_line.input_type_id.code == 'FAC01':
                        Fac = benifit_line.amount        
                
                            
                        
                        
                Tele_Comm = 0
                Hr_rent = self.env['hr.contract'].search([('employee_id','=',employee.id)],limit=1)
                for benifit_line in Hr_rent.benefit_line_ids:
                    if benifit_line.input_type_id.code == 'TC01':
                        Tele_Comm = benifit_line.amount
                          
                        
                        
                        
                Spcl_Loan = 0
                Hr_rent = self.env['hr.contract'].search([('employee_id','=',employee.id)],limit=1)
                for benifit_line in Hr_rent.benefit_line_ids:
                    if benifit_line.input_type_id.code == 'SLO01':
                        Spcl_Loan = benifit_line.amount        
                        
                        
                        
                        
                Adv_Sala = 0
                Hr_rent = self.env['hr.contract'].search([('employee_id','=',employee.id)],limit=1)
                for benifit_line in Hr_rent.benefit_line_ids:
                    if benifit_line.input_type_id.code == 'AS01':
                        House_rent = benifit_line.amount 
                       
                        
                        
                Pf_Loan_Inst = 0
                Hr_rent = self.env['hr.contract'].search([('employee_id','=',employee.id)],limit=1)
                for benifit_line in Hr_rent.benefit_line_ids:
                    if benifit_line.input_type_id.code == 'PFI01':
                        Adv_Sala = benifit_line.amount
     
                        
                Pf_Loan_Markup = 0
                       
                        
                        
                        
                Incentive = 0
                Hr_rent = self.env['hr.contract'].search([('employee_id','=',employee.id)],limit=1)
                for benifit_line in Hr_rent.benefit_line_ids:
                    if benifit_line.input_type_id.code == 'IN01':
                        Incentive = benifit_line.amount 
                     
                        
                Other = 0
                Hr_rent = self.env['hr.contract'].search([('employee_id','=',employee.id)],limit=1)
                for benifit_line in Hr_rent.benefit_line_ids:
                    if benifit_line.input_type_id.code == 'OR01':
                        Other = benifit_line.amount         
                   
                           
                        
                        
                Shutdown_Allowance = 0
                Hr_rent = self.env['hr.contract'].search([('employee_id','=',employee.id)],limit=1)
                for benifit_line in Hr_rent.benefit_line_ids:
                    if benifit_line.input_type_id.code == 'SHU01':
                        Shutdown_Allowance = benifit_line.amount         
                 
                        
                Variable_Pay = 0
                Hr_rent = self.env['hr.contract'].search([('employee_id','=',employee.id)],limit=1)
                for benifit_line in Hr_rent.benefit_line_ids:
                    if benifit_line.input_type_id.code == 'VP01':
                        Variable_Pay = benifit_line.amount 
                 
                        
                        
                Variable_Pay_Adj = 0
                Hr_rent = self.env['hr.contract'].search([('employee_id','=',employee.id)],limit=1)
                for benifit_line in Hr_rent.benefit_line_ids:
                    if benifit_line.input_type_id.code == 'VPA01':
                        Variable_Pay_Adj = benifit_line.amount         
                    
                        
                Mobile_All = 0
                Hr_rent = self.env['hr.contract'].search([('employee_id','=',employee.id)],limit=1)
                for benifit_line in Hr_rent.benefit_line_ids:
                    if benifit_line.input_type_id.code == 'MOB01':
                        Mobile_All = benifit_line.amount 
                        

                        
                        
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
                        
                        
                Off_Site_All = 0
                car_all = self.env['hr.contract'].search([('employee_id','=',employee.id)],limit=1)
                for car in car_all.benefit_line_ids:
                    if car.input_type_id.code == 'OTA01':
                        Off_Site_All = car.amount 
                                
                        
                        
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
                        
                    
                total_ded = PF + EOBI + Prof + Income_tax + Srchrg_On_ITax + Pf_Loan_Inst + Pf_Loan_Markup + Adv_Sala + Spcl_Loan + Tele_Comm + Fac + Variable_Pay_Deductions + Variable_Pay_Adj_Ded + Misc_Deduct + total + PF + EOBI + Prof + Income_tax + Pf_Loan_Inst
                
                
                over_all = basic_salry + House_rent + Conv_allown + Utilities_bills + Car_allown + special_allown + gross_sal + accomadation_allwn + salry_allown + salry_allown + washing + Shift_bills + Bonus + Arrears + Overtime + Site_All + Variable_Pay + Variable_Pay_Adj + Shutdown_Allowance + Other + gross_payable + Srchrg_On_ITax + Pf_Loan_Inst + Pf_Loan_Markup + Adv_Sala + Spcl_Loan + Tele_Comm + Fac + Variable_Pay_Deductions + Variable_Pay_Adj_Ded + Misc_Deduct + total_ded + Net_Payable
            
                
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
                sheet.write(row, 30, accomadation_allwn, format2)
                sheet.write(row, 31, salry_allown, format2)
                sheet.write(row, 32, washing, format2)
                sheet.write(row, 33, Shift_bills, format2)
                sheet.write(row, 34, Bonus, format2)
                sheet.write(row, 35, Arrears, format2)
                sheet.write(row, 36, Overtime, format2)
                sheet.write(row, 37, Site_All, format2)
                sheet.write(row, 38, Food_Acc_Allowance, format2)
                sheet.write(row, 39, Mobile_All, format2)
                sheet.write(row, 40, Incentive, format2)
                sheet.write(row, 41, Off_Site_All, format2)
                sheet.write(row, 42, Variable_Pay, format2)
                sheet.write(row, 43, Variable_Pay_Adj, format2)
                sheet.write(row, 44, Shutdown_Allowance, format2)
                sheet.write(row, 45, Other, format2)
                sheet.write(row, 46, gross_payable, format2)
                sheet.write(row, 47, total, format2)
                sheet.write(row, 48, PF, format2)
                sheet.write(row, 49, EOBI, format2)
                sheet.write(row, 50, Prof, format2)
                sheet.write(row, 51, Income_tax, format2)
                sheet.write(row, 52, Srchrg_On_ITax, format2)
                sheet.write(row, 53, Pf_Loan_Inst, format2)
                sheet.write(row, 54, Pf_Loan_Markup, format2)
                sheet.write(row, 55, Adv_Sala, format2)
                sheet.write(row, 56, Spcl_Loan, format2)
                sheet.write(row, 57, Tele_Comm, format2)
                sheet.write(row, 58, Fac, format2)
                sheet.write(row, 59, Variable_Pay_Deductions, format2)
                sheet.write(row, 60, Variable_Pay_Adj_Ded, format2)
                sheet.write(row, 61, Misc_Deduct, format2)
                sheet.write(row, 62, total_ded, format2)
                sheet.write(row, 63, Net_Payable, format2)
                sheet.write(row, 64, over_all, format2)
                row = row + 1
            sheet.write(row, 0,  str(),format2)
            sheet.write(row, 1,  str(),format2)
            sheet.write(row, 2,  str(),format2)
            sheet.write(row, 3,  str(),format2)
            sheet.write(row, 4,  str(),format2)
            sheet.write(row, 5,  str(),format2)
            sheet.write(row, 6,  str(),format2)
            sheet.write(row, 7,  str(),format2)
            sheet.write(row, 8,  str(),format2)
            sheet.write(row, 9,  str(),format2)
            sheet.write(row, 10, str(),format2)
            sheet.write(row, 11, str(),format2)
            sheet.write(row, 12, str(),format2)
            sheet.write(row, 13, str(),format2)
            sheet.write(row, 14, str(),format2)
            sheet.write(row, 15, str(),format2)
            sheet.write(row, 16, str(),format2)
            sheet.write(row, 17, str(),format2)
            sheet.write(row, 18, str(),format2)
            sheet.write(row, 19, str(),format2)
            sheet.write(row, 20, str(),format2)
            sheet.write(row, 21, str(),format2)
            sheet.write(row, 22, str(),format2)
            sheet.write(row, 23, tot_basic_salry,)
            sheet.write(row, 24, tot_House_rent, format2)
            sheet.write(row, 25, Conv_allown, format2)
            sheet.write(row, 26, Utilities_bills, format2)
            sheet.write(row, 27, Car_allown, format2)
            sheet.write(row, 28, special_allown, format2)
            sheet.write(row, 29, gross_sal, format2)
            sheet.write(row, 30, accomadation_allwn, format2)
            sheet.write(row, 31, salry_allown, format2)
            sheet.write(row, 32, washing, format2)
            sheet.write(row, 33, Shift_bills, format2)
            sheet.write(row, 34, Bonus, format2)
            sheet.write(row, 35, Arrears, format2)
            sheet.write(row, 36, Overtime, format2)
            sheet.write(row, 37, Site_All, format2)
            sheet.write(row, 38, Food_Acc_Allowance, format2)
            sheet.write(row, 39, Mobile_All, format2)
            sheet.write(row, 40, Incentive, format2)
            sheet.write(row, 41, Off_Site_All, format2)
            sheet.write(row, 42, Variable_Pay, format2)
            sheet.write(row, 43, Variable_Pay_Adj, format2)
            sheet.write(row, 44, Shutdown_Allowance, format2)
            sheet.write(row, 45, Other, format2)
            sheet.write(row, 46, gross_payable, format2)
            sheet.write(row, 47, total, format2)
            sheet.write(row, 48, PF, format2)
            sheet.write(row, 49, EOBI, format2)
            sheet.write(row, 50, Prof, format2)
            sheet.write(row, 51, Income_tax, format2)
            sheet.write(row, 52, Srchrg_On_ITax, format2)
            sheet.write(row, 53, Pf_Loan_Inst, format2)
            sheet.write(row, 54, Pf_Loan_Markup, format2)
            sheet.write(row, 55, Adv_Sala, format2)
            sheet.write(row, 56, Spcl_Loan, format2)
            sheet.write(row, 57, Tele_Comm, format2)
            sheet.write(row, 58, Fac, format2)
            sheet.write(row, 59, Variable_Pay_Deductions, format2)
            sheet.write(row, 60, Variable_Pay_Adj_Ded, format2)
            sheet.write(row, 61, Misc_Deduct, format2)
            sheet.write(row, 62, total_ded, format2)
            sheet.write(row, 63, Net_Payable, format2)    


               
                
                
                    