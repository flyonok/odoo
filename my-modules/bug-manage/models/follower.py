# -*- coding: utf-8 -*-

from odoo import models, fields, api


class follower(models.Model):
    _inherit = 'res.partner'
    _name = 'bm.followers'
    bug_ids = fields.Many2many('bm.bug', string='bug')
