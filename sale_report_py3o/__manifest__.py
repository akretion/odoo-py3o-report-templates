# Copyright 2016-2019 Akretion France (https://akretion.com/)
# @author: Alexis de Lattre <alexis.delattre@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Sale Reports Py3o',
    'version': '12.0.1.0.0',
    'category': 'Sales',
    'license': 'AGPL-3',
    'summary': 'Sample py3o sale reports',
    'description': """
Sale Reports Py3o
=================

This module adds a sample py3o sale reports.

This module has been written by Alexis de Lattre from Akretion
<alexis.delattre@akretion.com>.
    """,
    'author': 'Akretion',
    'depends': [
        'report_py3o',
        'sale_commercial_partner',
        'base_company_extension',
        'base_usability',  # to have res_partner.name_title
        'sale_usability',  # for layout
        'account_payment_sale',
        ],
    'data': ['report.xml'],
    'installable': True,
}
