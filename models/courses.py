# -*- coding: utf-8 -*-
from datetime import timedelta
from odoo import models, fields, api, exceptions
class Courses(models.Model):
    _name = 'academy.courses'
    _description = 'This is the model assigned for courses.'

    name = fields.Char(string = 'Title', required = True)
    description = fields.Text(string = 'Description', placeholder = "Short description")
    responsable_id = fields.Many2one('res.users', ondelete = 'set null', string = "Responsable", index = True)
    session_ids = fields.One2many('academy.sessions', 'course_id', string="Sessions")
    def copy(self, default=None):
        default = dict(default or {})
        copied_count = self.search_count(
            [('name', '=like', u"Copy of {}%".format(self.name))])
        if not copied_count:
            new_name = u"Copy of {}".format(self.name)
        else:
            new_name = u"Copy of {} ({})".format(self.name, copied_count)
        default['name'] = new_name
        return super(Courses, self).copy(default)
    _sql_constraints = [
        ('name_description_check', 'CHECK(name != description)', "The title of the course should not be the description"),

        ('name_unique', 'UNIQUE(name)', "The course title must be unique"),
    ]
