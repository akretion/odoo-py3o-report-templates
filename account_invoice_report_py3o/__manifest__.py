# Copyright 2016-2019 Akretion (Alexis de Lattre <alexis.delattre@akretion.com>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Invoice Report Py3o',
    'version': '12.0.1.0.0',
    'category': 'Accounting',
    'license': 'AGPL-3',
    'summary': 'Sample py3o invoice report',
    'description': """
Invoice Report Py3o
===================

This module adds a sample py3o invoice report.

This module has been written by Alexis de Lattre from Akretion
<alexis.delattre@akretion.com>.
    """,
    'author': 'Akretion',
    'depends': [
        'report_py3o',
        'base_company_extension',
        'base_usability',  # to have res_partner.name_title
        'account_usability',  # to have account_invoice.has_discount
        'account_payment_partner',
        ],
    'data': ['report.xml'],
    'installable': True,
}
