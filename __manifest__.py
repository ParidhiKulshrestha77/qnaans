{
    'name': 'StackIt Q&A Forum',
    'version': '1.0',
    'summary': 'Minimal Q&A forum platform built for Odoo',
    'author': 'Paridhi Kulshrestha',
    'category': 'Tools',
    'depends': ['base', 'web'],
    'data': [
        'security/ir.model.access.csv',
        'question_views.xml',
        'answer_views.xml',
        'forum_templates.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False
}