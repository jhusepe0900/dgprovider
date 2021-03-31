# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


from odoo import api, fields, models, SUPERUSER_ID, _


class SaleOrderInherited(models.Model):
    _inherit = ['sale.order']

    state = fields.Selection([
        ('draft', 'Quotation'),
        ('sent', 'Quotation Sent'),
        ('sale', 'Sales Order'),
        ('done', 'Locked'),
        ('cancel', 'Cancelled'),
        ('delivered', 'Delivered'),
        ('rejected', 'Rejected'),
    ], string='Status', readonly=True, copy=False, index=True, tracking=3, default='draft')

    def make_it_delivered(self):
        self.write({'state': 'delivered'})

    def make_it_rejected(self):
        self.write({'state': 'rejected'})
