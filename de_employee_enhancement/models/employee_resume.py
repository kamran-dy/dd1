# -*- coding: utf-8 -*-

from odoo import models, fields, api
from dateutil.relativedelta import relativedelta


class HrResumeLineInh(models.Model):
    _inherit = 'hr.resume.line'

    institute = fields.Char(string='Institute')
    reason_to_leave = fields.Char(string='Reason To Leave')
    salary = fields.Float(string='Salary')
    cgpa = fields.Char(string='Division/CGPA')
    is_experience = fields.Boolean(string='Is Experience?', default=False)
    is_education = fields.Boolean(string='Is Education?', default=False)

    @api.onchange('line_type_id')
    def compute_experience(self):
        if self.line_type_id.name == 'Experience':
            self.is_experience = True
            self.is_education = False
        if self.line_type_id.name == 'Education':
            self.is_education = True
            self.is_experience = False
            print(self.line_type_id.name)

