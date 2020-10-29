# -*- coding: utf-8 -*-
{
    'name': "bug管理",

    'summary': """
       用于软件开发中的bug管理""",

    'description': """
        用于软件开发中的bug管理
    """,

    'author': "xiaowy",
    'website': "http://www.y0y1.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['website'],
    'installable': True,
    'application': True,

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/bugs.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
