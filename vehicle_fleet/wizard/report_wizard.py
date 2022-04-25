from odoo import models, fields, api

from datetime import date 


class ReportWizard(models.TransientModel):
    _name="fleet.vehicle.wizard"
    _description="Wizard: Quick report of vehicles filtering sale date"

    def _default_vehicles(self):
        return self.env['fleet.vehicle'].browse(self._context.get("brand_model"))
    
    
    purchase_date=fields.Date(default=fields.Date.today())
    vehicle=fields.Many2many(comodel_name="fleet.vehicle",
                            string="Vehicles",
                            default=_default_vehicles)

    
    def create_fleet_report(self):
        for record in self:
            if self.purchase_date == self.vehicle.sale_date:
                report_id = self.env["fleet.vehicle"].create({
                    "brand_model" : self.vehicle_brand_model,
                    "current_price": self.vehicle_current_price,
                    "vehicle_line": [{"vehicle.brand_model" : self.vehicle.brand_model}]
                })