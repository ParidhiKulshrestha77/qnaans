from odoo import http
from odoo.http import request

class StackItForum(http.Controller):

    @http.route('/stackit', auth='public', website=True)
    def forum_home(self, **kw):
        questions = request.env['stack.question'].sudo().search([], order="id desc")
        return request.render('stackit_qaforum.forum_home', {
            'questions': questions
        })

    @http.route('/stackit/question/<int:question_id>', auth='public', website=True)
    def view_question(self, question_id):
        question = request.env['stack.question'].sudo().browse(question_id)
        return request.render('stackit_qaforum.question_page', {
            'question': question
        })
