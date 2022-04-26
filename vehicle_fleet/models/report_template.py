from odoo import models, fields, api


class SaleReport(models.Model):
    _name="fleet.vehicle.report"
    _description="Template for the sales report"



    vehicles=fields.Many2many(comodel_name="fleet.vehicle")
