from odoo import models, fields, api

class VisitWiz(models.TransientModel):
    _name = "hospiatal.visit.wizard"

    start_date = fields.Datetime("Start")
    end_date = fields.Datetime("End")

    def show_visit(self):
        paitents = self.env.get("hospital.paitent").search([('last_visit', '>=',self.start_date), ('last_visit', '<=', self.end_date)])
        res = paitents.ids 
        return {
            'type' : "ir.actions.act_window",
            'res_model' : "hospital.paitent",
            'domain' : [('id', 'in', res)],
            'view_mode' : 'tree,form'
        }