from odoo import models, fields, api


class SaleReport(models.Model):
    _name="fleet.vehicle.report"
    _description="Template for the sales report"

    vehicle=fields.Many2many(comodel_name="fleet.vehicle")
    
    reportid=fields.Integer(string="Report N°:")
    