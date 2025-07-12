from odoo import models, fields

class StackQuestion(models.Model):
    _name = 'stack.question'
    _description = 'StackIt Question'

    title = fields.Char(required=True)
    description = fields.Text()
    tags = fields.Char()
    user_id = fields.Many2one('res.users', default=lambda self: self.env.uid)
    answer_ids = fields.One2many('stack.answer', 'question_id', string='Answers')
    vote_count = fields.Integer(default=0)
    is_resolved = fields.Boolean(default=False)
