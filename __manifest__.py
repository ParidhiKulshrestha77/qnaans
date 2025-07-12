{
    'name': 'StackIt Q&A Forum',
    'version': '1.0',
    'summary': 'Minimal Q&A forum platform built for Odoo',
    'author': 'Paridhi Kulshrestha',
    'category': 'Tools',
    'depends': ['base', 'web'],
    'data': [
        'security/ir.model.access.csv',
        'views/question_views.xml',
        'views/answer_views.xml',
        'templates/forum_templates.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False
}