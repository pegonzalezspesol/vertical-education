# -*- coding: utf-8 -*-
# Copyright 2017 Pesol (<http://pesol.es>)
#                Angel Moya <angel.moya@pesol.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)
"""This model test the functionality of groups objects"""
from odoo.tests.common import TransactionCase


class TestEducationGroup(TransactionCase):
    """this class is the main of all test in groups"""

    def setUp(self):
        """This is the main method"""
        super(TestEducationGroup, self).setUp()

        # group data
        self.group_id = self.env.ref('education.education_group_1')

        # Set active
    def test_set_active(self):
        """this method exec activation functionality"""
        self.group_id.set_active()

        # create group
    def test_create(self):
        """This method create a new group"""
        group_obj = self.env['education.group']
        group_obj.create({
            'name': 'group_test',
            'course_id': self.env.ref('education.education_course_1').id
        })
