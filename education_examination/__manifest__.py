# -*- coding: utf-8 -*-
# Copyright <YEAR(S)> <AUTHOR(S)>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Education Examination",
    "summary": "Education Exam for Odoo",
    "version": "11.0.1.0.0",
    "category": "Education",
    "website": "https://github.com/OCA/vertical_education",
    "author": "PESOL, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": True,
    "installable": True,
    "depends": [
        "education",
    ],
    "data": [
        'views/examination_view.xml',
        'views/result_view.xml',
    ],
    "demo": [
    ],
}
