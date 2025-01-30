import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo12-addons-akretion-odoo-py3o-report-templates",
    description="Meta package for akretion-odoo-py3o-report-templates Odoo addons",
    version=version,
    install_requires=[
        'odoo12-addon-account_banking_sepa_direct_debit_py3o',
        'odoo12-addon-account_check_deposit_py3o',
        'odoo12-addon-account_invoice_overdue_reminder_py3o',
        'odoo12-addon-account_invoice_report_py3o',
        'odoo12-addon-purchase_report_py3o',
        'odoo12-addon-sale_report_py3o',
        'odoo12-addon-stock_report_py3o',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 12.0',
    ]
)
