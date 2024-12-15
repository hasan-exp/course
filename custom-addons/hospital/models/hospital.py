from odoo import models, fields


class HospitalPaitent(models.Model):
    _name = "hospital.paitent"

    name = fields.Char("Paitent Name")
    phone = fields.Char("Phone")
    last_visit = fields.Datetime("Last Visit")
    visit_count = fields.Float("Visit Times")
    note = fields.Text("Notes")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')])
    visit_ids = fields.One2many("hospital.visit", "paitent_id", string="Visits")
    sick_ids = fields.Many2many("hospital.sick", string="Sick History")


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
    visit_date = fields.Date("Visit")
    paitent_id = fields.Many2one("hospital.paitent" , "Paitent")

    
class Sick(models.Model):
    _name = "hospital.sick"

    name = fields.Char("Name")
