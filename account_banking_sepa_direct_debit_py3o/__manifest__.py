# © 2017 Akretion (Alexis de Lattre <alexis.delattre@akretion.com>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "SEPA Direct Debit Mandate Py3o Report",
    "version": "12.0.1.0.0",
    "category": "Banking",
    "license": "AGPL-3",
    "summary": "Sample py3o SEPA direct debit mandate report",
    "description": """
SEPA Direct Debit Mandate Py3o Report
=====================================

This module adds a sample Py3o SEPA direct debit mandate report.

This module has been written by Alexis de Lattre from Akretion
<alexis.delattre@akretion.com>.
    """,
    "author": "Akretion",
    "depends": ["report_py3o", "base_usability", "account_banking_sepa_direct_debit"],
    "data": ["report.xml"],
    "installable": True,
}
