# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from openerp import models, api, fields, _


class EducationSession(models.Model):
    _inherit = 'education.session'

    group_id = fields.Many2one(
        comodel_name='education.group',
        string='Group')
