# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import api, fields, models, SUPERUSER_ID, _
import logging

_logger = logging.getLogger(__name__)

class InventoryInherited(models.Model):

    _inherit = ['stock.picking']

    @api.depends('state')
    def _compute_show_validate(self):
        for picking in self:
            if picking.state == 'done' and picking.origin != False :
                sale = self.env['sale.order'].search([('name', '=', picking.origin)])
                sale.write({'state': 'delivered'})
        return super(InventoryInherited, self)._compute_show_validate()