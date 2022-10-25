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


class OpCourse(models.Model):
    _name = "op.course"
    _description = "Course"

    name = fields.Char(size=32, required=True)
    code = fields.Char(size=8, required=True)
    parent_id = fields.Many2one(comodel_name="op.course", string="Parent Course")
    section = fields.Char(size=32, required=True)
    evaluation_type = fields.Selection(
        selection=[
            ("normal", "Normal"),
            ("GPA", "GPA"),
            ("CWA", "CWA"),
            ("CCE", "CCE"),
        ],
        default="normal",
        required=True,
    )
    subject_ids = fields.Many2many(comodel_name="op.subject", string="Subject(s)")
    max_unit_load = fields.Float(string="Maximum Unit Load")
    min_unit_load = fields.Float(string="Minimum Unit Load")
