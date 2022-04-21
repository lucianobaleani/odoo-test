from odoo import models, fields, api

from datetime import date 
from dateutil import relativedelta

class Vehicle(models.Model):
    _name = "fleet.vehicle"
    _description = "Model of a vehicle"

    brand_model = fields.Char(string="vehicle Brand/Model")
    sale_price = fields.Float()
    sale_date = fields.Date(default=fields.Date.today)
    quantity_service = fields.Integer(string="Total of Services",
                                        compute="_compute_service",
                                        store=True)

    measurement_unit = fields.Selection(
        selection=[("kilometers", "Kilometers (Km)"), ("mileage", "Mileage(Mi)")],
        copy=False,
    )
    distance = fields.Integer()
    current_price = fields.Float(compute="_compute_current_price",
                                store=True)

    
    @api.depends("sale_price","measurement_unit","distance") 
    def _compute_current_price(self) -> None:
        """
        Compute the current price of the vehicle.
        :param sale_price, measurement_unit, distance: "fleet.vehicle" record.
        :writes current_: A float as result based on the sale_price, the distance and the measurement_unit(Km o Mi).
        """
        self.ensure_one()
        if self.measurement_unit == "kilometers":
            reduction = self.distance // 10000
            self.current_price = self.sale_price - (self.sale_price * (0.05 * reduction))
        else:
            reduction = self.distance // 6213.712
            self.current_price = self.sale_price - (self.sale_price * (0.05 * reduction))


    @api.onchange("sale_date")
    def _compute_service(self) ->None :
        """
        Compute the number of services that the vehicle has recieved, 1 every 6 months.
        :param sale_date: "fleet.vehicle record.
        :writes: An int as a result base on the calculation between today and sale_date.
        """
        self.ensure_one()
        today = date.today()
        for record in self:
            month = relativedelta.relativedelta(today, record.sale_date)
            record.quantity_service= (month.months + (12*month.years))//6