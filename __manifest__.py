{
    'name': 'Student Management',
    'version': '1.0',
    'sequence': 0,
    'category': '',
    'summary': 'Student Management Module',
    'description': """A student management module built by Md. Ashikuzzaman""",
    'depends': [],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/views_menu.xml'
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'assets': {
        'web.assets_backend': [
            'student_management/static/src/css/styles.css',
        ],
    },
    'license': 'LGPL-3',
}
