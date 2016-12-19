# -*- coding: utf-8 -*-
# © 2016 Akretion (Alexis de Lattre <alexis.delattre@akretion.com>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Stock Report Py3o',
    'version': '10.0.1.0.0',
    'category': 'Warehouse',
    'license': 'AGPL-3',
    'summary': 'Sample py3o stock report',
    'description': """
Stock Report Py3o
=================

This module adds sample py3o reports for stock.

This module has been written by Alexis de Lattre from Akretion
<alexis.delattre@akretion.com>.
    """,
    'author': 'Akretion',
    'depends': [
        'report_py3o',
        'sale_stock',
        'sale_commercial_partner',
        'base_company_extension',
        'base_usability',  # to have res_partner.name_title
        ],
    'data': ['report.xml'],
    'installable': True,
}
