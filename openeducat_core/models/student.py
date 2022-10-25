###############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2009-TODAY Tech-Receptives(<http://www.techreceptives.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class OpStudentCourse(models.Model):
    _name = "op.student.course"
    _description = "Student Course Details"

    student_id = fields.Many2one(
        comodel_name="op.student", string="Student", ondelete="cascade"
    )
    course_id = fields.Many2one(
        comodel_name="op.course", string="Course", required=True
    )
    batch_id = fields.Many2one(comodel_name="op.batch", string="Batch", required=True)
    roll_number = fields.Char()
    subject_ids = fields.Many2many(comodel_name="op.subject", string="Subjects")

    _sql_constraints = [
        (
            "unique_name_roll_number_id",
            "unique(roll_number,course_id,batch_id,student_id)",
            "Roll Number & Student must be unique per Batch!",
        ),
        (
            "unique_name_roll_number_course_id",
            "unique(roll_number,course_id,batch_id)",
            "Roll Number must be unique per Batch!",
        ),
        (
            "unique_name_roll_number_student_id",
            "unique(student_id,course_id,batch_id)",
            "Student must be unique per Batch!",
        ),
    ]


class OpStudent(models.Model):
    _name = "op.student"
    _description = "Student"
    _inherits = {"res.partner": "partner_id"}

    middle_name = fields.Char(size=128)
    last_name = fields.Char(size=128, required=True)
    birth_date = fields.Date(required=True)
    blood_group = fields.Selection(
        selection=[
            ("A+", "A+ve"),
            ("B+", "B+ve"),
            ("O+", "O+ve"),
            ("AB+", "AB+ve"),
            ("A-", "A-ve"),
            ("B-", "B-ve"),
            ("O-", "O-ve"),
            ("AB-", "AB-ve"),
        ],
    )
    gender = fields.Selection(
        selection=[("m", "Male"), ("f", "Female"), ("o", "Other")], required=True
    )
    nationality = fields.Many2one(comodel_name="res.country")
    emergency_contact = fields.Many2one(comodel_name="res.partner")
    visa_info = fields.Char(size=64)
    id_number = fields.Char(string="ID Card Number", size=64)
    photo = fields.Binary()
    partner_id = fields.Many2one(
        comodel_name="res.partner", string="Partner", required=True, ondelete="cascade"
    )
    gr_no = fields.Char("GR Number", size=20)
    category_id = fields.Many2one(comodel_name="op.category", string="Category")
    course_detail_ids = fields.One2many(
        comodel_name="op.student.course",
        inverse_name="student_id",
        string="Course Details",
    )

    @api.constrains("birth_date")
    def _check_birthdate(self):
        for record in self:
            if record.birth_date > fields.Date.today():
                raise ValidationError(
                    _("Birth Date can't be greater than current date!")
                )
