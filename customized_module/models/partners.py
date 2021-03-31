# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import api, fields, models, tools, _
from odoo.exceptions import ValidationError
import logging
from odoo.addons.website.tools import get_video_embed_code
_logger = logging.getLogger(__name__)

class PartnerInherited(models.Model):

    _inherit = 'res.partner'


    partner_pictures = fields.One2many('partner.images','partner_id',string="Attachment")


class PartnerImage(models.Model):
    
    _name = 'partner.images'

    _inherit = ['image.mixin']
    
    name = fields.Char(string="name")
    video_url = fields.Char('Video URL',
                            help='URL of a video for showcasing your partner.')
    partner_id = fields.Many2one('res.partner',string="partner")
    # partner_image = fields.Binary('Documents')
    image_1920 = fields.Image(required=True)

    embed_code = fields.Char(compute="_compute_embed_code")

    can_image_1024_be_zoomed = fields.Boolean("Can Image 1024 be zoomed", compute='_compute_can_image_1024_be_zoomed', store=True)

    @api.depends('image_1920', 'image_1024')
    def _compute_can_image_1024_be_zoomed(self):
        for image in self:
            image.can_image_1024_be_zoomed = image.image_1920 and tools.is_image_size_above(image.image_1920, image.image_1024)

    @api.depends('video_url')
    def _compute_embed_code(self):
        for image in self:
            image.embed_code = get_video_embed_code(image.video_url)

    @api.constrains('video_url')
    def _check_valid_video_url(self):
        for image in self:
            if image.video_url and not image.embed_code:
                raise ValidationError(_("Provided video URL for '%s' is not valid. Please enter a valid video URL.", image.name))
