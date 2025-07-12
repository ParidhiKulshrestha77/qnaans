from odoo import models, fields

class StackAnswer(models.Model):
    _name = 'stack.answer'
    _description = 'StackIt Answer'

    question_id = fields.Many2one('stack.question', required=True)
    content = fields.Text(required=True)
    user_id = fields.Many2one('res.users', default=lambda self: self.env.uid)
    is_accepted = fields.Boolean(default=False)
    vote_count = fields.Integer(default=0)
