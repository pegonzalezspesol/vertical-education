# -*- coding: utf-8 -*-

from odoo import models, fields


class EducationEnrollment(models.Model):
    _name = "education.enrollment"
    _rec_name = 'code'

    code = fields.Char()
    student_id = fields.Many2one(
        comodel_name='education.student',
        string='Student')
    course_id = fields.Many2one(
        comodel_name='education.course',
        string='Course')
    group_id = fields.Many2one(
        comodel_name='education.group',
        string='Group')
