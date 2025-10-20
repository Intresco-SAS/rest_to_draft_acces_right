# -*- coding: utf-8 -*-
{
    'name': "Reset To Darft Acess Rights",
    "version" : "17.0.0.0",
    "category" : "Accounting",
    "summary": "Prevent Spesifice users to reset to draft Inovices & Bills & Journal Entries & Payments",
    'description': """
       Prevent Spesifice users to reset to draft Inovices & Bills & Journal Entries & Payments.
    """,
    'author': "Abdulghani Fawzi",
    "license": "OPL-1",
    'email': "this@abdulghanifawzi.com ",
    'website': "https://abdulghanifawzi.com",
    'category': 'accounting',
    'version': '0.1',
    'price': 0,
    'currency': 'USD',
    'license': 'AGPL-3',
    'images': ['static/description/main_screenshot.png'],
    'depends': ['base', 'account'],
    'data': [
        'security/security_group.xml',
        'views/account_move.xml',
    ],
}
