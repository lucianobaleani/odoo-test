from odoo import models, fields, api

from datetime import date 


class ReportWizard(models.TransientModel):
    _name="fleet.vehicle.wizard"
    _description="Wizard: Quick report of vehicles filtering sale date"

    def _default_vehicles(self):
        return self.env['fleet.vehicle'].browse(self._context.get("brand_model"))
    
    
    vehicle=fields.Many2many(comodel_name="fleet.vehicle",
                            string="Vehicles",
                            default=_default_vehicles)



    purchase_date=fields.Date(required=True)

    vehicle_brand_model = fields.Char(related="vehicle.brand_model")
    vehicle_sale_price = fields.Float(related="vehicle.sale_price")
    vehicle_quantity_service = fields.Integer(related="vehicle.quantity_service")
    vehicle_measurement_unit = fields.Selection(related="vehicle.measurement_unit")
    vehicle_distance = fields.Integer(related="vehicle.distance")
    vehicle_current_price = fields.Float(related="vehicle.current_price")

    
    def create_fleet_report(self):
        for record in self:
            if self.purchase_date == self.vehicle.sale_date:
                report_id = self.env["fleet.vehicle"].create({
                    "brand_model" : self.vehicle_brand_model,
                    "current_price": self.vehicle_current_price,
                    "vehicle_line": [{"vehicle.brand_model" : self.vehicle.brand_model}]
                })