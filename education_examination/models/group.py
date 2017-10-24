# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from openerp import models, api, fields, _


class EducationGroup(models.Model):
    _inherit = 'education.group'

    examination_ids = fields.One2many(
        comodel_name='education.examination',
        inverse_name='group_id',
        string='Examinations')

    session_ids = fields.One2many(
        comodel_name='education.session',
        inverse_name='group_id',
        string='Sessions')
