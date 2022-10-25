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


class OpSubjectRegistration(models.Model):
    _name = "op.subject.registration"
    _description = "Subject Registration"
    _inherit = ["mail.thread"]

    name = fields.Char(readonly=True, default="New")
    student_id = fields.Many2one(
        comodel_name="op.student",
        string="Student",
        required=True,
        tracking=True,
    )
    course_id = fields.Many2one(
        comodel_name="op.course",
        string="Course",
        required=True,
        tracking=True,
    )
    batch_id = fields.Many2one(
        comodel_name="op.batch",
        string="Batch",
        required=True,
        tracking=True,
    )
    compulsory_subject_ids = fields.Many2many(
        comodel_name="op.subject",
        relation="subject_compulsory_rel",
        column1="register_id",
        column2="subject_id",
        string="Compulsory Subjects",
        readonly=True,
    )
    elective_subject_ids = fields.Many2many(
        comodel_name="op.subject", string="Elective Subjects"
    )
    state = fields.Selection(
        selection=[
            ("draft", "Draft"),
            ("submitted", "Submitted"),
            ("approved", "Approved"),
            ("rejected", "Rejected"),
        ],
        default="draft",
        string="state",
        copy=False,
        tracking=True,
    )
    max_unit_load = fields.Float(string="Maximum Unit Load", tracking=True)
    min_unit_load = fields.Float(string="Minimum Unit Load", tracking=True)

    def action_reset_draft(self):
        for rec in self:
            rec.state = "draft"

    def action_reject(self):
        for rec in self:
            rec.state = "rejected"

    def action_approve(self):
        for record in self:
            subject_ids = []
            for sub in record.compulsory_subject_ids:
                subject_ids.append(sub.id)
            for sub in record.elective_subject_ids:
                subject_ids.append(sub.id)
            course_id = self.env["op.student.course"].search(
                [
                    ("student_id", "=", record.student_id.id),
                    ("course_id", "=", record.course_id.id),
                ],
                limit=1,
            )
            if course_id:
                course_id.write({"subject_ids": [[6, 0, list(set(subject_ids))]]})
                record.state = "approved"
            else:
                raise ValidationError(_("Course not found on student's admission!"))

    def action_submitted(self):
        for rec in self:
            rec.state = "submitted"

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get("name", "New") == "New":
                vals["name"] = (
                    self.env["ir.sequence"].next_by_code("op.subject.registration")
                    or "/"
                )
        return super(OpSubjectRegistration, self).create(vals_list)

    def get_subjects(self):
        for record in self:
            subject_ids = []
            if record.course_id and record.course_id.subject_ids:
                for subject in record.course_id.subject_ids:
                    if subject.subject_type == "compulsory":
                        subject_ids.append(subject.id)
            record.compulsory_subject_ids = [(6, 0, subject_ids)]
