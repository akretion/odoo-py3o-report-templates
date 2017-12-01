# odoo-py3o-sample-report

This repository group modules that provide *py3o templates* for basic Odoo reports.

Dependencies:
=============
The py3o templates in this repository use the module [report_py3o](https://github.com/OCA/reporting-engine/tree/10.0/report_py3o) from the OCA [report-engine](https://github.com/OCA/reporting-engine) repository.

It requires the following Python dependencies:
````
pip install py3o.template
pip install py3o.formats
````
Templating with LibreOffice :
=============
[py3o.template](https://bitbucket.org/faide/py3o.template/overview) allows to create templates directly on [LibreOffice](http://www.libreoffice.org/), following the syntax available on the [py3o.template documentation](http://py3otemplate.readthedocs.io/en/latest/templating.html).


Tracking .odt business document evolution :
=============
Three available options to track changes in your .odt template :

* Use the [Compare Document](https://help.libreoffice.org/Common/Compare_Document) native option in LibreOffice
* Extract the .xml of your two .odt documents and compare it with classic `git diff` or `gitk`. Be aware that the text on the header and the footer are located in a separate .xml file from the main text.
* Use classic `git diff` or `gitk` tools after converting the .odt binary files to plain text formats :
  1. Install [odt2txt](https://github.com/dstosberg/odt2txt)
      sudo apt-get update
      sudo apt-get install odt2txt
  2. Add `*.odt diff=odt` in your git attributes file `~/.config/git/attributes`, if you want to add this attribute on a global level configuration, creating a new `attributes` file if necessary.

  If you want to add this attributes only on a projetc level configuration, add it in `<your project dir>/.gitattributes`.
  3. In your global git config file `~/.gitconfig` add the reading option :
    ````
    [diff "odt"]
        textconv = odt2txt
        binary = true
    ````

Writing py3o Format Functions in LibreOffice input-fields
=============
It is possible to write py3o format functions like `py3o://function="lang== ' '"` or `py3o://function="format_multiline_value()"` in LibreOffice *input-fields* instead of using the *hyperlink* method, using this [patch](https://bitbucket.org/faide/py3o.template/pull-requests/32/allow-to-use-libreoffice-input-fields-for/diff).

Authors:
========
- Copyright (C) 2015-TODAY Akretion (http://www.akretion.com).
- Alexis de Lattre <alexis.delattre@akretion.com>


License:
========
AGPL-V3

(Work in progress)
