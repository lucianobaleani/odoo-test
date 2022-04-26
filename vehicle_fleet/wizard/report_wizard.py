from odoo import models, fields, api

from datetime import date 


class ReportWizard(models.TransientModel):
    _name="fleet.vehicle.wizard"
    _description="Wizard: Quick report of vehicles filtering sale date"    
    
    vehicle=fields.Many2many(comodel_name="fleet.vehicle",
                            string="Vehicles")
    
    purchase_date=fields.Date(default=fields.Date.today())

    

    v_brand_model = fields.Char(related="vehicle.brand_model")
    v_sale_price = fields.Float(related="vehicle.sale_price")
    v_quantity_service = fields.Integer(related="vehicle.quantity_service")
    v_measurement_unit = fields.Selection(related="vehicle.measurement_unit")
    v_distance = fields.Integer(related="vehicle.distance")
    v_current_price = fields.Float(related="vehicle.current_price")
    
    def create_fleet_report(self):

        self.purchase_date == self.env['fleet.vehicle'].search([('sale_date','=', "self.purchase_date")])
        for record in self:
                if self.purchase_date == record.vehicle.sale_date:
                    vehicle= self.env["fleet.vehicle.report"].create({
                        "vehicle_line": [(0,0,{"v_brand_model" : record.vehicle.brand_model,
                                               "v_sale_price" : record.vehicle.brand_model,
                                               "v_quantity_service" : record.vehicle.brand_model,
                                               "v_measurement_unit" : record.vehicle.brand_model,
                                               "v_distance" : record.vehicle.brand_model,
                                               "v_current_price" : record.vehicle.brand_model, })]
                })