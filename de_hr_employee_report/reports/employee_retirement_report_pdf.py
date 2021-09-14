# -*- coding: utf-8 -*-

import time
from odoo import api, models, _
from odoo.exceptions import UserError
from dateutil.relativedelta import relativedelta
from datetime import datetime
from datetime import date, datetime, timedelta
from itertools import groupby


class EmployeeRetirementPDF(models.AbstractModel):
    _name = 'report.de_hr_employee_report.employee_retirement_pdf'
    _description = 'Employee Retirement PDF Report'

    def _get_report_values(self, docids, data):
        type_employee = self.env['employee.type'].search([('id', 'in', data['employee_type_ids'])])
        employee_type = []
        for rec in type_employee:
            employee_type.append(rec.name)
        #raise UserError(employee_type)
        em_type = ','.join(employee_type)
        department = self.env['hr.department'].search([('id', 'in', data['department_ids'])])
        departments = []
        for rec in department:
            departments.append(rec.name)
        
        #raise UserError(departments)
        dep = ','.join(departments)
        
        location = self.env['hr.work.location'].search([('id', 'in', data['location_ids'])])
        locations = []
        for rec in location:
            locations.append(rec.name)
        loc = ','.join(locations)
        
        grade_type = self.env['grade.type'].search([('id', 'in', data['grade_type_ids'])])
        g_type = []
        for rec in grade_type:
            g_type.append(rec.name)

        gr_type = ','.join(g_type)
        
        company_ids = self.env['res.company'].search([('id', 'in', data['company_ids'])])
        companyids = []
        for rec in company_ids:
            companyids.append(rec.name)
        company = ','.join(companyids)
        
        
        if employee_type and departments and locations and g_type and companyids:
            active_contract = self.env['hr.contract'].search(['|',
                                                              '|',
                                                             ('employee_id.resigned_date','>=',data['start_date']),
                                                             ('employee_id.resigned_date','<=',data['end_date']),
                                                              '|',
                                                              ('employee_id.emp_type', 'in', employee_type),
                                                              ('employee_id.work_location_id', 'in',locations),
                                                              ('employee_id.department_id', 'in',departments),
                                                              ('employee_id.grade_type', 'in', g_type),
                                                              ('employee_id.company_id', 'in', companyids)
                                                              ])
        
        
        elif employee_type and departments and companyids:
            active_contract = self.env['hr.contract'].search(['|',
                                                              '|',
                                                             ('employee_id.resigned_date','>=',data['start_date']),
                                                             ('employee_id.resigned_date','<=',data['end_date']),
                                                              '|',
                                                              ('employee_id.emp_type', 'in', employee_type),
                                                              ('employee_id.department_id', 'in',departments),
                                                              ('employee_id.company_id', 'in', companyids)
                                                              ])
        elif employee_type and locations and companyids:
            active_contract = self.env['hr.contract'].search(['|',
                                                              '|',
                                                             ('employee_id.resigned_date','>=',data['start_date']),
                                                             ('employee_id.resigned_date','<=',data['end_date']),
                                                              '|',
                                                              ('employee_id.emp_type', 'in', employee_type),
                                                              ('employee_id.work_location_id', 'in',locations),
                                                              ('employee_id.company_id', 'in', companyids)
                                                              ])
        elif employee_type and cost_centers and companyids:
            active_contract = self.env['hr.contract'].search(['|',
                                                              '|',
                                                             ('employee_id.resigned_date','>=',data['start_date']),
                                                             ('employee_id.resigned_date','<=',data['end_date']),
                                                              '|',
                                                              ('employee_id.emp_type', 'in', employee_type),
                                                              ('cost_center_information_line.cost_center', 'in',cost_centers),
                                                              ('employee_id.company_id', 'in', companyids)
                                                              ])
        elif employee_type and departments and locations and companyids:
            active_contract = self.env['hr.contract'].search(['|',
                                                              '|',
                                                             ('employee_id.resigned_date','>=',data['start_date']),
                                                             ('employee_id.resigned_date','<=',data['end_date']),
                                                              '|',
                                                              ('employee_id.emp_type', 'in', employee_type),
                                                              ('employee_id.work_location_id', 'in',locations),
                                                              ('employee_id.department_id', 'in',departments),
                                                              ('employee_id.company_id', 'in', companyids)
                                                              ])
        elif employee_type and departments and cost_centers and companyids:
            active_contract = self.env['hr.contract'].search(['|',
                                                              '|',
                                                             ('employee_id.resigned_date','>=',data['start_date']),
                                                             ('employee_id.resigned_date','<=',data['end_date']),
                                                              '|',
                                                              ('employee_id.emp_type', 'in', employee_type),
                                                              ('employee_id.department_id', 'in',departments),
                                                              ('cost_center_information_line.cost_center', 'in',cost_centers),
                                                              ('employee_id.company_id', 'in', companyids)
                                                              ])
        elif employee_type and locations and cost_centers and companyids:
           active_contract = self.env['hr.contract'].search(['|',
                                                              '|',
                                                             ('employee_id.resigned_date','>=',data['start_date']),
                                                             ('employee_id.resigned_date','<=',data['end_date']),
                                                              '|',
                                                              ('employee_id.emp_type', 'in', employee_type),
                                                              ('employee_id.work_location_id', 'in',locations),
                                                              ('cost_center_information_line.cost_center', 'in',cost_centers),
                                                              ('employee_id.company_id', 'in', companyids)
                                                              ])
        elif departments and locations and cost_centers and companyids:
            active_contract = self.env['hr.contract'].search(['|',
                                                              '|',
                                                             ('employee_id.resigned_date','>=',data['start_date']),
                                                             ('employee_id.resigned_date','<=',data['end_date']),
                                                              '|',
                                                              ('employee_id.work_location_id', 'in',locations),
                                                              ('employee_id.department_id', 'in',departments),
                                                              ('cost_center_information_line.cost_center', 'in',cost_centers),
                                                              ('employee_id.company_id', 'in', companyids)
                                                              ])
        elif departments and locations and companyids:
            active_contract = self.env['hr.contract'].search(['|',
                                                              '|',
                                                             ('employee_id.resigned_date','>=',data['start_date']),
                                                             ('employee_id.resigned_date','<=',data['end_date']),
                                                              '|',
                                                              ('employee_id.work_location_id', 'in',locations),
                                                              ('employee_id.department_id', 'in',departments),
                                                              ('employee_id.company_id', 'in', companyids)
                                                              ])
        elif departments and cost_centers and companyids:
            active_contract = self.env['hr.contract'].search(['|',
                                                              '|',
                                                             ('employee_id.resigned_date','>=',data['start_date']),
                                                             ('employee_id.resigned_date','<=',data['end_date']),
                                                              '|',
                                                              ('employee_id.department_id', 'in',departments),
                                                              ('cost_center_information_line.cost_center', 'in',cost_centers),
                                                              ('employee_id.company_id', 'in', companyids)
                                                              ])
        elif locations and cost_centers and companyids:
            active_contract = self.env['hr.contract'].search(['|',
                                                              '|',
                                                             ('employee_id.resigned_date','>=',data['start_date']),
                                                             ('employee_id.resigned_date','<=',data['end_date']),
                                                              '|',
                                                              ('employee_id.work_location_id', 'in',locations),
                                                              ('cost_center_information_line.cost_center', 'in',cost_centers),
                                                              ('employee_id.company_id', 'in', companyids)
                                                              ])
        elif employee_type and companyids:
            active_contract = self.env['hr.contract'].search(['|',
                                                              '|',
                                                             ('employee_id.resigned_date','>=',data['start_date']),
                                                             ('employee_id.resigned_date','<=',data['end_date']),
                                                              '|',
                                                              ('employee_id.emp_type', 'in', employee_type),
                                                              ('employee_id.company_id', 'in', companyids)
                                                              ])
        elif locations and companyids:
            active_contract = self.env['hr.contract'].search(['|',
                                                              '|',
                                                             ('employee_id.resigned_date','>=',data['start_date']),
                                                             ('employee_id.resigned_date','<=',data['end_date']),
                                                              '|',
                                                              ('employee_id.work_location_id', 'in',locations),
                                                              ('employee_id.company_id', 'in', companyids)
                                                              ])
        
        elif departments and companyids:
           active_contract = self.env['hr.contract'].search(['|',
                                                              '|',
                                                             ('employee_id.resigned_date','>=',data['start_date']),
                                                             ('employee_id.resigned_date','<=',data['end_date']),
                                                              '|',
                                                              ('employee_id.department_id', 'in',departments),
                                                              ('employee_id.company_id', 'in', companyids)
                                                              ])
        elif cost_centers and companyids:
            active_contract = self.env['hr.contract'].search(['|',
                                                              '|',
                                                             ('employee_id.resigned_date','>=',data['start_date']),
                                                             ('employee_id.resigned_date','<=',data['end_date']),
                                                              '|',
                                                              ('cost_center_information_line.cost_center', 'in',cost_centers),
                                                              ('employee_id.company_id', 'in', companyids)
                                                              ])
        
        #raise UserError(active_contract.ids)
            
        return {
            'doc_ids': self.ids,
            'doc_model': 'employee.status',
            'data': data,
            'location': loc,
            'employee_type': em_type,
            'department': dep,
            'cost_center': cost_center,
            'active_contract': active_contract,
            'company_name':company,
            'start_date':data['start_date'],
            'end_date':data['end_date'],
        }
