# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class EducationCourseCategory(models.Model):
    _name = "education.course.category"

    name = fields.Char(string='Name', required=True)


class EducationSubject(models.Model):
    _name = "education.subject"

    name = fields.Char(string='Name', required=True)

    course_ids = fields.Many2many(
        comodel_name='education.course',
        relation='course_subject_rel',
        column1='subject_id',
        column2='course_id',
        string='Courses')


class EducationCourse(models.Model):
    _name = "education.course"

    name = fields.Char(string='Name', required=True)
    code = fields.Char(string='Code', required=True)
    category_id = fields.Many2one(
        comodel_name='education.course.category',
        string='Category')
    subject_ids = fields.Many2many(
        comodel_name='education.subject',
        relation='course_subject_rel',
        column1='course_id',
        column2='subject_id',
        string='Subjects')

    active = fields.Boolean(
        string='Active', default=True)
