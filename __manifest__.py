# -*- coding: utf-8 -*-
{
    'name': "vente",

    'summary': """                                         
Apllication de gestion des ventes""",

    'description': """
Cette apllication vous permet de gèrer vos ventes
    """,

    'author': "King BA",
    'website': "https://www.kingba.com",
    'application': True,

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        # 'views/views.xml',
        # 'views/templates.xml',
        'views/client.xml',
        'views/produit.xml',
        'views/categorie.xml',
        'views/commande.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

