# -*- coding: utf-8 -*-
# Copyright 2017 Grant Thornton Spain - Ismael Calvo <ismael.calvo@es.gt.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models


class HrDepartment(models.Model):
    _name = 'hr.department'
    _inherit = ['hr.department', 'website.published.mixin']
