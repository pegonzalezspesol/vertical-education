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


class OpFaculty(models.Model):
    _name = "op.faculty"
    _description = "Faculty"
    _inherits = {"res.partner": "partner_id"}

    partner_id = fields.Many2one(
        comodel_name="res.partner", string="Partner", required=True, ondelete="cascade"
    )
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
        selection=[("male", "Male"), ("female", "Female")], required=True
    )
    nationality = fields.Many2one(comodel_name="res.country")
    emergency_contact = fields.Many2one(comodel_name="res.partner")
    visa_info = fields.Char(size=64)
    id_number = fields.Char(string="ID Card Number", size=64)
    photo = fields.Binary()
    login = fields.Char(related="partner_id.user_id.login", readonly=1)
    last_login = fields.Datetime(
        string="Latest Connection", related="partner_id.user_id.login_date", readonly=1
    )
    faculty_subject_ids = fields.Many2many(
        comodel_name="op.subject", string="Subject(s)"
    )
    emp_id = fields.Many2one(comodel_name="hr.employee", string="Employee")

    @api.constrains("birth_date")
    def _check_birthdate(self):
        for record in self:
            if record.birth_date > fields.Date.today():
                raise ValidationError(
                    _("Birth Date can't be greater than current date!")
                )

    def create_employee(self):
        for record in self:
            vals = {
                "name": record.name
                + " "
                + (record.middle_name or "")
                + " "
                + record.last_name,
                "country_id": record.nationality.id,
                "gender": record.gender,
                "address_home_id": record.partner_id.id,
            }
            emp_id = self.env["hr.employee"].create([vals])
            record.write({"emp_id": emp_id.id})
            record.partner_id.write({"employee": True})
