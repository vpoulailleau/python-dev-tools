Python Dev Tools
================

Needed and up-to-date tools to develop in Python (*WORK IN PROGRESS*)


.. image:: https://img.shields.io/pypi/v/python_dev_tools.svg
        :target: https://pypi.python.org/pypi/python_dev_tools

.. image:: https://img.shields.io/pypi/l/python_dev_tools.svg
        :target: https://github.com/vpoulailleau/python_dev_tools/blob/master/LICENSE

.. image:: https://travis-ci.com/vpoulailleau/python-dev-tools.svg?branch=master
        :target: https://travis-ci.com/vpoulailleau/python-dev-tools

.. image:: https://readthedocs.org/projects/python-dev-tools/badge/?version=latest
        :target: https://python-dev-tools.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pepy.tech/badge/python-dev-tools
        :target: https://pepy.tech/project/python-dev-tools
        :alt: Downloads

.. image:: https://coveralls.io/repos/github/vpoulailleau/python-dev-tools/badge.svg?branch=HEAD
        :target: https://coveralls.io/github/vpoulailleau/python-dev-tools?branch=HEAD
        :alt: Coverage Status

.. image:: https://api.codeclimate.com/v1/badges/282fcd71714dabd6a847/maintainability
        :target: https://codeclimate.com/github/vpoulailleau/python-dev-tools/maintainability
        :alt: Maintainability

.. image:: https://bettercodehub.com/edge/badge/vpoulailleau/python-dev-tools?branch=master
        :target: https://bettercodehub.com/results/vpoulailleau/python-dev-tools
        :alt: Maintainability

.. image:: https://img.shields.io/lgtm/grade/python/g/vpoulailleau/python-dev-tools.svg?logo=lgtm&logoWidth=1
        :target: https://lgtm.com/projects/g/vpoulailleau/python-dev-tools/context:python
        :alt: Maintainability

Documentation
-------------

The full documentation can be read at https://python-dev-tools.readthedocs.io.

Installation
------------

* Short version: ``pip install --user --upgrade python-dev-tools``
* Long version: https://python-dev-tools.readthedocs.io/en/latest/installation.html
* Use the provided linter, formatter and precommit hook where applicable

Installation with Visual Studio Code
------------------------------------

* ``pip install --user --upgrade python-dev-tools``
* Be sure to have the official Python extension installed in VS Code
* In VS Code, open settings (F1 key, then type "Open Settings (JSON)",
  then enter)
* Add in the opened JSON file:

.. code:: javascript

    "python.linting.enabled": true,
    "python.linting.flake8Enabled": true,
    "python.linting.flake8Path": "/home/vincent/.local/bin/whatalinter",

* Adapt the previous path according to your installation.

Features
--------

Integrate features of commonly used tools. This package provides usual
dependencies to develop Python software.

* Simple linter

  * ``whatalinter a_python_file.py`` lints a_python_file.py
  * output is compatible with the one of pycodestyle (formerly named pep8) for
    easy integration in text editors and IDE
  * based on

    * pycodestyle: https://github.com/PyCQA/pycodestyle
    * pyflakes: https://github.com/PyCQA/pyflakes
    * mccabe: https://github.com/pycqa/mccabe
    * pydocstyle: https://github.com/PyCQA/pydocstyle
    * flake8 and plugins: https://gitlab.com/pycqa/flake8

      * flake8-isort: https://github.com/gforcada/flake8-isort
      * pep8-naming: https://github.com/PyCQA/pep8-naming
      * flake8-comprehensions: https://github.com/adamchainz/flake8-comprehensions
      * flake8-logging-format: https://github.com/globality-corp/flake8-logging-format
      * flake8-bugbear: https://github.com/PyCQA/flake8-bugbear
      * flake8-builtins: https://github.com/gforcada/flake8-builtins
      * flake8-broken-line: https://github.com/sobolevn/flake8-broken-line
      * flake8-fixme: https://github.com/tommilligan/flake8-fixme
      * flake8-mutable: https://github.com/ebeweber/flake8-mutable
      * flake8-debugger: https://github.com/JBKahn/flake8-debugger
      * flake8-variables-names: https://github.com/best-doctor/flake8-variables-names
      * flake8-bandit: https://github.com/tylerwince/flake8-bandit

* Simple formatter

  * TODO

* Simple precommit hook

  * TODO

License
-------

BSD 3-Clause license, feel free to contribute: https://python-dev-tools.readthedocs.io/en/latest/contributing.html.

TODO
----

* documentation
* linter

  * add more linters

* formatter
* precommit

Credits
-------

This package was created with Cookiecutter_ and the
`audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
