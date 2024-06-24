from odoo import api, fields, models

class Student(models.Model):
    _name = 'stm.student'
    _description = 'stm.student.description'

    name = fields.Char(string='Name')
    age = fields.Integer(string='Age', default=0)