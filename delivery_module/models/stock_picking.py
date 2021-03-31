# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


from odoo import api, fields, models, SUPERUSER_ID, _


class StockPickingInherited(models.Model):
    _inherit = 'stock.picking'

    order_description = fields.Char(string='Order description')
    total_cost_order = fields.Float(string='Total order cost')
    state_deliv = fields.Selection([
        ('pending', 'Pending Delivery'),
        ('delivered', 'Delivered'),
        ('rejected', 'Rejected'),
    ], string='Status Delivery', readonly=True, default="pending")

    def delivered_action(self):
        for picking in self:
            if picking.state == 'done' and picking.origin != False :
                sale = self.env['sale.order'].search([('name', '=', picking.origin)])
                sale.write({'state': 'delivered'})
        self.write({'state_deliv': 'delivered'})

    def rejected_action(self):
        for picking in self:
            if picking.state == 'done' and picking.origin != False :
                sale = self.env['sale.order'].search([('name', '=', picking.origin)])
                sale.write({'state': 'rejected'})
        self.write({'state_deliv': 'rejected'})
