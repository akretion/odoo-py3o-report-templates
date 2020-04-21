# Copyright 2020 Akretion France (http://www.akretion.com/)
# @author: Alexis de Lattre <alexis.delattre@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Invoice Overdue Reminder Py3o',
    'version': '12.0.1.0.0',
    'category': 'Accounting',
    'license': 'AGPL-3',
    'summary': 'Sample py3o overdue reminder letter report',
    'description': """
Invoice Overdue Reminder Py3o
=============================

This module adds a sample py3o overdue reminder letter in French and English.

This module has been written by Alexis de Lattre from Akretion
<alexis.delattre@akretion.com>.
    """,
    'author': 'Akretion',
    'depends': [
        'report_py3o',
        'base_usability',  # for header
        'account_invoice_overdue_reminder',
        ],
    'data': ['report.xml'],
    'installable': True,
}
