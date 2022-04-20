# -*- coding utf-8 -*-

{
    'name' : 'Vehicle Fleet Module',

    'summary' :'Module app for vehicles fleet ',

    'description': """
        This module allows you to control the vehicle's fleet management.
        """,

    'author': 'Luciano Baleani',

    'website' : '',

    'category' : 'Odoo-Test',
    'version' : '0.1',

    'depends' : ['base'],

    'data' : [
        "security/vehicle_security.xml",
        "security/ir.model.access.csv",
        "views/vehicle_menuitems.xml",
        "views/vehicle_views.xml",
    ],

    'demo': [
        'demo/vehicle_demo.xml',
    ]

}
