from odoo import models, fields, api

class Loan(models.Model):
    _name = "loan.loan"

    name =  fields.Char("Description", required=True)
    total_amount = fields.Float("Loan Amount", default=1)
    amount = fields.Float("Installment Amount", default=1)
    counts = fields.Integer("Installments Counts", default=1)

    @api.onchange('total_amount', 'counts')
    def on_change_total_amount(self):
        self.amount  = self.total_amount / self.counts

    @api.onchange('amount')
    def on_change_amount(self):
        self.counts  = self.total_amount / self.amount

class Partner(models.Model):
    _inherit = "res.partner"
    
    is_paitent = fields.Boolean("Mark as Paitent")
    sick_ids = fields.Many2many("hospital.sick", string="Sick History")

    
class HospitalPaitent(models.Model):
    _name = "hospital.paitent"

    name = fields.Char("Name", required=True)
    phone = fields.Char("Phone")
    last_visit = fields.Datetime("Last Visit")
    visit_count = fields.Float("Visit Times", default=1)
    note = fields.Text("Notes")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')])
    visit_ids = fields.One2many("hospital.visit", "paitent_id", string="Visits")
    sick_ids = fields.Many2many("hospital.sick", string="Sick History")
    partner_id = fields.Many2one('res.partner', string="Paitent")
    state = fields.Selection([('draft', 'Draft'), ('confirm', 'Confirmed')], string="Status", default='draft')

    def action_confirm(self):
       self.state = 'confirm'

    def create_visit(self):
        data = {
            'name' : '////',
            'paitent_id' : self.id,
            'visit_date' : fields.Datetime.now(),
        }
        obj = self.env.get('hospital.visit').create(data)


class Doctor(models.Model):
    _name = "hospital.doctor"

    name = fields.Char("Name")
    position_id = fields.Many2one('hospital.position', string="Position")


class Position(models.Model):
    _name = "hospital.position"

    name = fields.Char("Name")


class Visit(models.Model):
    _name = "hospital.visit"

    name = fields.Text("Description")
    visit_date = fields.Datetime("Visit")
    paitent_id = fields.Many2one("hospital.paitent" , "Paitent")

    
class Sick(models.Model):
    _name = "hospital.sick"

    name = fields.Char("Name")
