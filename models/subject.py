from odoo import api, fields, models

class Subject(models.Model):
    _name = 'stm.subject'
    _description = 'stm.subject.description'

    name = fields.Char(string='Name')
    code = fields.Char(string='Code')