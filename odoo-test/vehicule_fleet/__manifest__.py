# -*- coding utf-8 -*-

{
    'name' : 'Vehicule Fleet Module',

    'summary' :'Module app for vehicules fleet ',

    'description': """
        This module allows you to control the vehicule's fleet management.
        """,

    'author': 'Luciano Baleani',

    'website' : '',

    'category' : 'Odoo-Test',
    'version' : '0.1',

    'depends' : ['base'],

    'data' : [
        "security/vehicule_security.xml",
        "security/ir.model.access.csv",
        "views/vehicule_menuitems.xml",
        "views/vehicule_views.xml",
    ],

    'demo': [
        'demo/vehicule_demo.xml',
    ]

}
