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
        ('delivered','Delivered'),
        ('rejected','Rejected'),
        ], string='Status', readonly=True, copy=False, index=True, tracking=3, default='draft')

    def action_confirm(self):
        res = super(SaleOrderInherited, self).action_confirm()
        for pick in self.picking_ids:
            pick.write({'total_cost_order': self.amount_total})
        return res

    def multi_action_confirm(self):
        for rec in self:
            rec.action_confirm()