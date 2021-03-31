# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Delivery module',
    # 'version': '1.1',
    # 'category': 'Sales/Sales',
    'summary': 'Delivery module',
    'description': """
    Delivery
    """,
    'depends': ['sale','stock','customized_module'],
    'data': [
            'security/delivery_security.xml',
            'views/sale_order.xml',
            'views/delivery_menus.xml',
        ],
    # 'demo': [
    #     'data/product_product_demo.xml',
    #     'data/sale_demo.xml',
    # ],
    'installable': True,
    # 'auto_install': False
}

