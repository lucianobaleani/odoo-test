from odoo import models, fields, api

from datetime import date 


class ReportWizard(models.TransientModel):
    #THE _name must be representavie in this case should be: "vehicle.purchases.report.wizard"
    _name = "fleet.vehicle.wizard"
    _description = "Wizard: Quick report of vehicles filtering sale date"    
    
    vehicle = fields.Many2many(comodel_name="fleet.vehicle",
                            string="Vehicles")
    
    purchase_date = fields.Date(default=fields.Date.today())
    
    def create_fleet_report(self):
        vehicles = self.env['fleet.vehicle'].search([('sale_date','=', self.purchase_date)])
        data = {
            "vehicles": vehicles
        }
        report = self.env["ir.actions.report"].search([("report_name","=","vehicle_fleet.fleet_vehicle_document")])
        return report.report_action(self, data=data)