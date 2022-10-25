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

from odoo import fields, models


class OpSubject(models.Model):
    _name = "op.subject"
    _description = "Subject"

    name = fields.Char(size=128, required=True)
    code = fields.Char(size=256, required=True)
    course_id = fields.Many2one(comodel_name="op.course", string="Course")
    grade_weightage = fields.Float()
    type = fields.Selection(
        selection=[
            ("theory", "Theory"),
            ("practical", "Practical"),
            ("both", "Both"),
            ("other", "Other"),
        ],
        default="theory",
        required=True,
    )
    subject_type = fields.Selection(
        selection=[("compulsory", "Compulsory"), ("elective", "Elective")],
        default="compulsory",
        required=True,
    )
