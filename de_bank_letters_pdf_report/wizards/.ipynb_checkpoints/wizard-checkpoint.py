from odoo import api, fields, models, _
from odoo.exceptions import UserError


class BankReport(models.TransientModel):

    _name = 'bank.model'
    _description = 'Model wizard'

    cheque_no = fields.Char(string='Cheque no', required=True)
    company = fields.Many2many('account.journal', string='Bank')
   

    def print_report(self):

        data = {}
        return self.env.ref('de_bank_letters_pdf_report.bank_report_data').report_action(self, data=data)
