# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from openerp import models, api, fields, _


class EducationResult(models.Model):
    _name = 'education.result'

    examination_id = fields.Many2one(
        comodel_name='education.examination',
        string='Examination')

    mark = fields.Float(
        string='Mark')

    student_id = fields.Many2one(
        comodel_name='education.student',
        string='Student')
