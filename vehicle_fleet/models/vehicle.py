from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

from datetime import date 
from dateutil import relativedelta


class Vehicle(models.Model):
    _name = "fleet.vehicle"
    _description = "Model of a vehicle"

    brand_model = fields.Char(string="Vehicle Brand/Model")
    sale_price = fields.Float(help="Cannot be negative")
    purchase_date = fields.Date(default=fields.Date.today)
    quantity_service = fields.Integer(string="Total of Services",
                                        compute="_compute_service",
                                        store=True)

    measurement_unit = fields.Selection(
        selection=[("kilometers", "Kilometers (Km)"), ("miles", "Miles (Mi)")],
        copy=False,
        help="If Kilometers then %5 less of the current price every 10,000 Km / If Miles then %5 less of the current price every 6,213.712 Mi"
    )
    distance = fields.Integer()
    current_price = fields.Float(default=0,
                                compute="_compute_current_price",
                                store=True,
                                help="Minimum price = 1") 

    
    @api.depends("sale_price","measurement_unit","distance") 
    def _compute_current_price(self) -> None:
        """
        Compute the current price of the vehicle.
        :param sale_price, measurement_unit, distance: "fleet.vehicle" record.
        :writes current_: A float as result based on the sale_price, the distance and the measurement_unit(Km o Mi).
        """
        for record in self:
            price = record.sale_price
            if record.measurement_unit == "kilometers":
                reduction = record.distance // 10000
                while reduction != 0:
                    price = round(price * 0.95, 2)
                    reduction = reduction - 1
            else:
                reduction = record.distance // 6213.712
                while reduction != 0:
                    price = round(price * 0.95, 2)
                    reduction = reduction - 1
            if price <= 1:
                price = 1
            record.update({"current_price": price})  


    @api.depends("purchase_date")
    def _compute_service(self) ->None :
        """
        Compute the number of services that the vehicle has recieved, 1 every 6 months.
        :param purchase_date: "fleet.vehicle record.
        :writes: An int as a result base on the calculation between today and purchase_date.
        """
        today = date.today()
        for record in self:
            month = relativedelta.relativedelta(today, record.purchase_date)
            services = (month.months+(12*month.years))//6
            record.update({"quantity_service" : services})


    @api.onchange("sale_price","measurement_unit","distance") 
    def _onchange_current_price(self) -> None:
        """
        Compute the current price of the vehicle.
        :param sale_price, measurement_unit, distance: "fleet.vehicle" record.
        :writes current_: A float as result based on the sale_price, the distance and the measurement_unit(Km o Mi).
        """
        for record in self:
            if record.sale_price >= 0:
                price = record.sale_price
                if record.measurement_unit == "kilometers":
                    reduction = record.distance // 10000
                    while reduction != 0:
                        price = round(price * 0.95, 2)
                        reduction = reduction - 1
                else:
                    reduction = record.distance // 6213.712
                    while reduction != 0:
                        price = round(price * 0.95, 2)
                        reduction = reduction - 1
                if price <= 1:
                    price = 1
                record.update({"current_price": price})  
            else:
                raise ValidationError(_("The sale price cannot be negative"))

          

    @api.onchange("purchase_date")
    def _onchange_service(self) ->None :
        """
        Compute the number of services that the vehicle has recieved, 1 every 6 months.
        :param purchase_date: "fleet.vehicle record.
        :writes: An int as a result base on the calculation between today and purchase_date.
        """
        today = date.today()
        for record in self:
            month = relativedelta.relativedelta(today, record.purchase_date)
            services = (month.months+(12*month.years))//6
            record.update({"quantity_service" : services})