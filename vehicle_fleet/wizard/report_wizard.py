from odoo import models, fields, api

from datetime import timedelta


class ReportWizard(models.TransientModel):
    #THE _name must be representavie in this case should be: "vehicle.purchases.report.wizard"
    _name = "fleet.vehicle.wizard"
    _description = "Wizard: Quick report of vehicles filtering sale date"    
    
    vehicle = fields.Many2many(comodel_name="fleet.vehicle",
                                string="Vehicles")

    purchase_date_from = fields.Date()
    purchase_date_to = fields.Date(default=fields.Date.today())


    def create_fleet_report(self):
        dates=[self.purchase_date_from +timedelta(days=x) for x in range((self.purchase_date_to - self.purchase_date_from ).days)]
        data = {}
        data["vehicles"] = []
        for date in dates:
            vehicles = self.env['fleet.vehicle'].search([('purchase_date','=', date)])
            for vehicle in vehicles:
                    data["vehicles"].append({
                    "brand_model":vehicle.brand_model,
                    "purchase_date":vehicle.purchase_date,
                    "quantity_service":vehicle.quantity_service,
                    "measurement_unit":vehicle.measurement_unit,
                    "distance":vehicle.distance,
                    "sale_price":vehicle.sale_price,
                    "current_price":vehicle.current_price}
                    )
                
        report = self.env["ir.actions.report"].search([("report_name","=","vehicle_fleet.fleet_vehicle_document")])
        return report.report_action(self, data=data) 
