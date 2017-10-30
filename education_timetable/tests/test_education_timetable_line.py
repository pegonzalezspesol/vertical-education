# -*- coding: utf-8 -*-
# Copyright 2017 Pesol (<http://pesol.es>)
#                Angel Moya <angel.moya@pesol.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)
"""All the tests about object timetable_line"""
from datetime import datetime
from odoo.tests.common import TransactionCase
from odoo import fields


class TestEducationTimetableLine(TransactionCase):
    """The main class of the tests"""

    def setUp(self):
        """Main function for tests"""
        super(TestEducationTimetableLine, self).setUp()

        # TimeRange data
        timerange_obj = self.env['education.timerange']
        timerange_id = timerange_obj.create({
            'name': '08:15-09:10',
            'start_time': 08.15,
            'end_time': 09.10
        })

        # Timetable Line data
        education_timetable_obj = self.env['education.timetable.line']
        course_id = self.env.ref('education.education_course_1')
        group_id = self.env.ref('education.education_group_1')
        subject_id = self.env.ref('education.education_subject_1')
        teacher_id = self.env.ref('education.education_teacher_1')
        day = fields.Selection([('0', 'Monday')])
        start_date = datetime.now()
        end_date = datetime.now()

        # Create Timetable Line
        self.education_timetable_id = education_timetable_obj.create({
            'course_id': course_id.id,
            'group_id': group_id.id,
            'subject_id': subject_id.id,
            'teacher_id': teacher_id.id,
            'timerange_id': timerange_id.id,
            'day': day,
            'start_date': start_date,
            'end_date': end_date,
        })

        # Generate New Sessions
    def test_generate_new_sessions(self):
        """This function generate all the sessions"""
        self.education_timetable_id.generate_new_sessions()
