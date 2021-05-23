# -*- coding: utf-8 -*-
{
    'name': "POS Customer List",

    'summary': """
        This Module allows to restrict customer loading to point of sale.
       """,

    'description': """
        The module will allow a customer to be displayed in the PoS, load through the check box 'Available in POS'
    """,

    'author': "Loyal IT Solutions Pvt Ltd",
    'website': "http://www.loyalitsolutions.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Point Of Sale',
    'version': "12.0.1.0.0",
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
