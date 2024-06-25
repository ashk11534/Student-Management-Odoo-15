from odoo import api, fields, models

class Student(models.Model):
    _name = 'stm.student'
    _description = 'stm.student.description'

    name = fields.Char(string='Name')
    age = fields.Integer(string='Age', default=0)
    enrolled_class = fields.Selection([
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
    ], string='Class')
    roll = fields.Char(string='Roll')