from odoo import models, field, api


class ReportWizard(models.TransientModel):
    _name="fleet.vehicle.wizard"
    _description="Wizard: Quick report of vehicles filtering sale date"