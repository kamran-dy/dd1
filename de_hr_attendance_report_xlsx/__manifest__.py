# -*- coding: utf-8 -*-
{
    'name': "Attendance Report Excel",

    'summary': """
        Hr Attendance Report Excel
        """,

    'description': """
        Hr Attendance Report Excel 
    """,

    'author': "Dynexcel",
    'website': "http://www.dynexcel.com",
    'category': 'Attendance',
    'version': '14.0.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','hr_attendance'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'wizards/hr_attendance_report_wizard.xml',
        'views/hr_attendance_report_menu.xml',
        'reports/hr_attendance_report_xlsx.xml',
#         'views/hr_leave_type_views.xml',   
#         'report/hr_attendance_report_template.xml',
        
    ],
    # only loaded in demonstration mode
}
