from odoo import api, fields, models, _
from odoo.exceptions import UserError

class HrAppraisalObjective(models.Model):
    _name = 'hr.appraisal.objective'
    _inherit = ['portal.mixin', 'mail.thread', 'mail.activity.mixin']
    _description='Appraisal Objective'
    _rec_name = 'employee_id'
    
    employee_id = fields.Many2one('hr.employee',string='Employee')
    emploee_code = fields.Char(related='employee_id.emp_number')
    emploee_type = fields.Selection(related='employee_id.emp_type')
    grade_type_id = fields.Many2one(related='employee_id.grade_type')
    department_id = fields.Many2one(related='employee_id.department_id')
    job_id = fields.Many2one(related='employee_id.job_id')
    description = fields.Char('Description')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('waiting', "Sent for Manager's review"),
        ('confirm', 'Confirmed'),
    ], string='State', index=True, copy=False, default='draft', track_visibility='onchange')
    
    objective_year = fields.Selection([('2020', 'FY 2020-21'), ('2021', 'FY 2021-22'), ('2022', 'FY 2022-23'), ('2023', 'FY 2023-24')
                                   , ('2024', 'FY 2024-25'), ('2025', 'FY 2025-26'), ('2026', 'FY 2026-27'), ('2027', 'FY 2027-28')
                                   , ('2028', 'FY 2028-29'), ('2029', 'FY 2029-30'), ('2030', 'FY 2030-31'), ('2032', 'FY 2032-33')
                                   , ('2033', 'FY 2023-34'), ('2034', 'FY 2034-35'), ('2035', 'FY 2035-36'), ('2036', 'FY 2036-37')
                                   , ('2037', 'FY 2037-38'), ('2038', 'FY 2038-39'), ('2039', 'FY 2039-40'), ('2040', 'FY 2040-41')],
                               string="Objective Year", default='2021', required = 'True')
    
    objective_lines = fields.One2many('hr.appraisal.objective.line', 'objective_id')
    traing_need = fields.Boolean(string='Training Need')
    total_weightage = fields.Float("Total Weightage", compute = 'limit_weightage')
    note = fields.Text(string='Achivements')
    readonly_status = fields.Selection([
        ('make_readonly', 'Readonly'),
        ('make_editable', 'Editable')], compute = 'compute_readonly')
    
#     def unlink(self):
#         for rec in self:
#             if rec.state in ['confirm']:
#                 raise UserError(('Deletion is Not Allowed!'))
#             return super(HrAppraisalObjective, self).unlink()
    
     
    @api.constrains('employee_id')
    def compute_readonly(self):
        for rec in self:
            if rec.state == 'confirm' and rec.env.user.has_group('de_appraisal_enhancement.group_allow_edit_objectives'):
                rec.readonly_status = 'make_editable'
            if rec.state == 'confirm' and not rec.env.user.has_group('de_appraisal_enhancement.group_allow_edit_objectives'):
                rec.readonly_status = 'make_readonly'
            else:
                rec.readonly_status = 'make_editable'
    
    @api.constrains('objective_year')
    def onchange_objective_year(self):
        if self.objective_year:
            if self.employee_id.id:
                appraisal_exists = self.search([('employee_id','=',self.employee_id.id),('objective_year','=',self.objective_year),('state','!=','draft')])
                if appraisal_exists:
                    raise UserError(('Objective Already exist for this year'))
            else:
                raise UserError(('First select the employee'))

    
    @api.model
    def create(self,vals):
        if vals['objective_year']:
            appraisal_exists = self.search([('state', 'not in', ['cancel','draft']),('employee_id','=',vals['employee_id']),('objective_year','=',vals['objective_year'])])
            if appraisal_exists:
                raise UserError(('Objective Already Exist for Selected Year'))
        result = super(HrAppraisalObjective, self).create(vals)
        return result


    
    @api.constrains('weightage')
    def limit_weightage(self):
        for rec in self:
            count = 0
            for line in rec.objective_lines:
                count = count + line.weightage
         
            rec.total_weightage = count

    @api.model
    def create(self,vals):
        res = super(HrAppraisalObjective, self).create(vals)
        if res.total_weightage != 100:
            raise UserError('Total Weightage must be equal 100')
        return res
    
    def write(self, vals):
        res = super(HrAppraisalObjective, self).write(vals)
        if self.total_weightage != 100:
            raise UserError('Total Weightage must be equal 100')
        return res
    
    
    def action_sent_review(self):
        self.state = 'waiting'
        
    def action_submit(self):
        self.state = 'confirm'    
        
    
class HrAppraisalObjectiveline(models.Model):
    _name = 'hr.appraisal.objective.line'
    _description = 'Appraisal Objective Line'
    
    objective_id = fields.Many2one('hr.appraisal.objective')
    objective = fields.Char('Objective')
    description = fields.Char('Description')
    date_from = fields.Date(string='Date From')
    date_to = fields.Date(string='Date To')
    priority = fields.Selection([
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('very_high', 'Very High'),
    ], string='Priority', index=True, copy=False, default='low',required = True)
    rating_level = fields.Selection([
        ('Outstanding Performance', 'Outstanding Performance'),
        ('Excellent Performance', 'Excellent Performance'),
        ('Strong Performance', 'Strong Performance'),
        ('Needs Improvement', 'Needs Improvement'),
        ('Unsatisfactory', 'Unsatisfactory'),
    ], string='Rating Level', index=True, copy=False, compute='compute_rating_level')
    rating_score = fields.Float(string='Rating Score')
    weightage = fields.Float(string='Weightage')
    category_id = fields.Many2one('hr.objective.category', string='Category')
    status_id = fields.Many2one('hr.objective.status',  string='Status')
    
    @api.depends('rating_score')
    def compute_rating_level(self):
        for line in self:
            if line.rating_score >= 1 and line.rating_score <= 1.4:
                line.update({
                    'rating_level': 'Unsatisfactory'
                })
            elif line.rating_score >= 1.5 and line.rating_score <= 2.4:
                line.update({
                    'rating_level': 'Needs Improvement'
                })   
            elif line.rating_score >= 2.5 and line.rating_score <= 3.4:
                line.update({
                    'rating_level': 'Strong Performance'
                })   
            elif line.rating_score >= 3.5 and line.rating_score <= 4.4:
                line.update({
                    'rating_level': 'Excellent Performance'
                })
            elif line.rating_score >= 4.5 and line.rating_score <= 5:
                line.update({
                    'rating_level': 'Outstanding Performance'
                }) 
            else:
                line.update({
                    'rating_level': False
                }) 
        
    
    @api.onchange('weightage')
    def limit_weightage(self):
        if self.weightage:
            for rec in self:
                if rec.weightage > 100 or rec.weightage <1:
                    raise UserError('Weightage Cannot be greater than 100 or less than 1')
                
        
    
class ObjectiveCategories(models.Model):
    _name = 'hr.objective.category'
    _description= 'HR Objective Category'
    
    name = fields.Char(string='Description', required=True)
    
class ObjectiveStatus(models.Model):
    _name = 'hr.objective.status'
    _description= 'HR Objective Status'
    
    name = fields.Char(string='Description', required=True)    
    