# -*- coding: utf-8 -*-
# Copyright 2009-TODAY Tech-Receptives(<http://www.techreceptives.com>)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html)

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class EducationBatch(models.Model):
    _name = 'education.batch'

    code = fields.Char('Code', size=8, required=True)
    name = fields.Char('Name', size=32, required=True)
    start_date = fields.Date(
        'Start Date', required=True, default=fields.Date.today())
    end_date = fields.Date('End Date', required=True)
    course_id = fields.Many2one('education.course', 'Course', required=True)

    faculty_id = fields.Many2one(
        comodel_name='education.faculty',
        string='Teacher in charge')
    state = fields.Selection([
        ('pending', 'Pending'),
        ('active', 'Active'),
        ('finished', 'Finished'),
        ('cancel', 'Cancelled'),
    ], string='Status', readonly=True, index=True, track_visibility='onchange',
        default='pending')

    active = fields.Boolean(
        string='Active', default=True)

    subject_registration_ids = fields.One2many(
        comodel_name='education.subject.registration',
        inverse_name='batch_id',
        string='Subject Registration')

    education_student_course_ids = fields.One2many(
        comodel_name='education.student.course',
        inverse_name='batch_id',
        string='Education Student Course')




    @api.multi
    @api.constrains('start_date', 'end_date')
    def check_dates(self):
        for record in self:
            start_date = fields.Date.from_string(record.start_date)
            end_date = fields.Date.from_string(record.end_date)
            if start_date > end_date:
                raise ValidationError(_("End Date cannot be set before \
                Start Date."))

    @api.model
    def name_search(self, name, args=None, operator='ilike', limit=100):
        if self.env.context.get('get_parent_batch', False):
            lst = []
            lst.append(self.env.context.get('course_id'))
            courses = self.env['education.course'].browse(lst)
            while courses.parent_id:
                lst.append(courses.parent_id.id)
                courses = courses.parent_id
            batches = self.env['education.batch'].search(
                [('course_id', 'in', lst)])
            return batches.name_get()
        return super(EducationBatch, self).name_search(
            name, args, operator=operator, limit=limit)

    @api.multi
    def set_active(self):
        self.state = 'active'
