# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Partner with multiple pictures',
    # 'version': '1.1',
    # 'category': 'Sales/Sales',
    'summary': 'Zoom and multiple pictures in partner and new state in sale order',
    'description': """
    Zoom and multiple pictures in partner and new state in sale order
    """,
    'depends': ['sale','stock','sale_management','website','swipe_images_backend','field_image_preview'
        ],
    'data': [
            'security/ir.model.access.csv',
            'views/partner_view.xml',
            'views/order_views.xml',
              ],

    'installable': True,
    # 'auto_install': False
}

