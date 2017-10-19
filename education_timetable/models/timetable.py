# -*- coding: utf-8 -*-
# Copyright 2017 Pesol (<http://pesol.es>)
#                Angel Moya <angel.moya@pesol.es>
#                Luis Adan Jimenez Hernandez <luis.jimenez@pesol.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

from openerp import models, api, fields, _


class EducationTimetable(models.Model):
    _name = 'education.timetable'

    name = fields.Char(
        string='Name')

    timetable_line_ids = fields.One2many(
        comodel_name='education.timetable.line',
        inverse_name='timetable_id',
        string='Timetable Lines')


class EducationTimetableLine(models.Model):
    _name = 'education.timetable.line'

    timetable_id = fields.Many2one(
        comodel_name='education.timetable',
        string='Timetable')

    course_id = fields.Many2one(
        comodel_name='education.course',
        string='Course')

    group_id = fields.Many2one(
        comodel_name='education.group',
        string='Group')

    teacher_id = fields.Many2one(
        comodel_name='education.teacher',
        string='Teacher')

    days = fields.Selection(
        [('monday', 'Monday'),
         ('tuesday', 'Tuesday'),
         ('wednesday', 'Wednesday'),
         ('thursday', 'Thursday'),
         ('friday', 'Friday')],
        string='Days')

    timerange_id = fields.Many2one(
        comodel_name='education.timerange',
        string='Time Range')
