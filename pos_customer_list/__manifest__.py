# -*- coding: utf-8 -*-
{
    'name': "POS Customer Restriction",

    'summary': """
        This Module allows to restrict customers from loading in point of sale.
       """,

    'description': """
        This Module allows to restrict customers from loading in point of sale. Customers's visibility can be controlled with a check box ' Available in POS'
    """,

    'author': "Loyal IT Solutions Pvt Ltd",
    'website': "https://www.loyalitsolutions.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Point Of Sale',
    'version': "13.0.1.0.0",
    'license': 'AGPL-3',
    'support': "support@loyalitsolutions.com",

    # any module necessary for this one to work correctly
    'depends': ['base','point_of_sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    'images': ['static/description/banner.png'],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
