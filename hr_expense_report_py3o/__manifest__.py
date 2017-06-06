# -*- coding: utf-8 -*-
# © 2017 Akretion (Alexis de Lattre <alexis.delattre@akretion.com>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'HR Expense Py3o',
    'version': '10.0.1.0.0',
    'category': 'Human Resources',
    'license': 'AGPL-3',
    'summary': 'Sample py3o expense reports',
    'description': """
HR Expense Report Py3o
======================

This module adds a sample py3o expense reports.

This module has been written by Alexis de Lattre from Akretion
<alexis.delattre@akretion.com>.
    """,
    'author': 'Akretion',
    'depends': [
        'report_py3o',
        'base_company_extension',
        'base_usability',  # to have res_partner.name_title
        'hr_expense',
        'hr_expense_sequence',
        ],
    'data': ['report.xml'],
    'installable': True,
}
