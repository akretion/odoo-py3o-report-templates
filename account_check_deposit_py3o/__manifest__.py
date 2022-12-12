# Copyright 2016-2021 Akretion France (http://www.akretion.com/)
# @author: Alexis de Lattre <alexis.delattre@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Check Deposit Py3o',
    'version': '14.0.1.0.0',
    'category': 'Accounting',
    'license': 'AGPL-3',
    'summary': 'Sample py3o check deposit report',
    'description': """
Check Deposit Py3o
==================

This module adds a sample py3o check deposit report in French.

This module has been written by Alexis de Lattre from Akretion
<alexis.delattre@akretion.com>.
    """,
    'author': 'Akretion',
    'depends': [
        'report_py3o',
        'base_company_extension',  # for header
        'account_check_deposit',
        ],
    'data': ['report.xml'],
    'installable': True,
}
