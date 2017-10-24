# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from openerp import models, api, fields, _


class EducationExamination(models.Model):
    _name = 'education.examination'

    name = fields.Char(
        string='Name')

    state = fields.Selection(
        [('draft', 'Draft'),
         ('planned', 'Planned'),
         ('done', 'Done')],
        string='Status',
        default="draft")

    group_id = fields.Many2one(
        comodel_name='education.group',
        string='Group')

    subject_id = fields.Many2one(
        comodel_name='education.subject',
        string='Subject')

    result_ids = fields.One2many(
        comodel_name='education.result',
        inverse_name='examination_id',
        string='Results')

    date = fields.Date(
        string='Date')
