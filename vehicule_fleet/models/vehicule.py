from datetime import timedelta
from dateutil import relativedelta

from odoo import models, fields, api


class Vehicule(models.Model):
    _name = "fleet.vehicule"
    _description = "Model of a vehicule"

    brand_model = fields.Char(string="Vehicule Brand/Model")
    sale_price = fields.Float()
    sale_date = fields.Date(default=fields.Date.today)
    quantity_service = fields.Integer(string="Total of Services")
    measurement_unit = fields.Selection(
        selection=[("kilometers", "Kilometers(KM)"), ("mileage", "Mileage(Mi)")],
        copy=False,
    )
    distance = fields.Integer()
    current_price = fields.Float()

    @api.onchange("measurement_unit", "distance", "sale_price")
    def _compute_current_price(self):
        if self.measurement_unit == "kilometers":
            reduction = self.distance / 10000
            current_price = self.distance * (0, 5 * reduction)
        else:
            reduction = self.distance / 6214
            current_price = self.distance * (0, 5 * reduction)

    @api.depends("sale_date", "quantity_service")
    def _compute_services(self):
        months = relativedelta.relativedelta(-self.sale_date)
