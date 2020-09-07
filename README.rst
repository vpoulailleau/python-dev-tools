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

.. image:: https://api.codeclimate.com/v1/badges/282fcd71714dabd6a847/test_coverage
        :target: https://codeclimate.com/github/vpoulailleau/python-dev-tools/test_coverage
        :alt: Test Coverage

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

In a terminal, run:

.. code-block:: console

    $ python3 -m pip install python-dev-tools --user --upgrade

Full documentation on installation: https://python-dev-tools.readthedocs.io/en/latest/installation.html

That's it! Use the provided linter (``whatalinter``), formatter (``whataformatter``) and
precommit hook (TODO) where applicable.

Installation with Visual Studio Code
------------------------------------

* Follow the installation procedure for python-dev-tools
* Be sure to have the official Python extension installed in VS Code
* Open VS Code from within your activated virtual environment (in fact, make sure that 
  ``whatalinter_vscode`` is in your ``PYTHON_PATH``)
* In VS Code, open settings (F1 key, then type "Open Settings (JSON)",
  then enter)
* Add in the opened JSON file (before the closing ``}``):

.. code:: javascript

    "python.linting.enabled": true,
    "python.linting.flake8Enabled": true,
    "python.linting.flake8Path": "whatalinter_vscode",
    "python.formatting.provider": "black",
    "python.formatting.blackPath": "black",
    "python.formatting.blackArgs": [],

Features
--------

Integrate features of commonly used tools. This package provides usual
dependencies to develop Python software.

* Simple linter

  * ``whatalinter a_python_file.py`` lints a_python_file.py
  * output is compatible with the one of flake8 for easy integration in text editors
    and IDE
  * based on flake8 and plugins: https://gitlab.com/pycqa/flake8

    * darglint: https://github.com/terrencepreilly/darglint
    * flake8-2020: https://github.com/asottile/flake8-2020
    * flake8-bandit: https://github.com/tylerwince/flake8-bandit
    * flake8-broken-line: https://github.com/sobolevn/flake8-broken-line
    * flake8-bugbear: https://github.com/PyCQA/flake8-bugbear
    * flake8-builtins: https://github.com/gforcada/flake8-builtins
    * flake8-commas: https://github.com/PyCQA/flake8-commas/
    * flake8-comprehensions: https://github.com/adamchainz/flake8-comprehensions
    * flake8-debugger: https://github.com/JBKahn/flake8-debugger
    * flake8-docstrings: https://gitlab.com/pycqa/flake8-docstrings
    * flake8-eradicate: https://github.com/sobolevn/flake8-eradicate
    * flake8-fixme: https://github.com/tommilligan/flake8-fixme
    * flake8-isort: https://github.com/gforcada/flake8-isort
    * flake8-logging-format: https://github.com/globality-corp/flake8-logging-format
    * flake8-mutable: https://github.com/ebeweber/flake8-mutable
    * flake8-quotes: https://github.com/zheller/flake8-quotes/
    * flake8-rst-docstrings: https://github.com/peterjc/flake8-rst-docstrings
    * flake8-string-format: https://github.com/xZise/flake8-string-format
    * flake8-variables-names: https://github.com/best-doctor/flake8-variables-names
    * pep8-naming: https://github.com/PyCQA/pep8-naming
    * wemake-python-styleguide: https://github.com/wemake-services/wemake-python-styleguide

* Simple formatter

  * ``whataformatter a_python_file.py`` formats a_python_file.py
  * based on

    * autoflake: https://github.com/myint/autoflake
    * black: https://github.com/python/black
    * pyupgrade: https://github.com/asottile/pyupgrade

* Simple precommit hook

  * TODO

License
-------

BSD 3-Clause license, feel free to contribute: https://python-dev-tools.readthedocs.io/en/latest/contributing.html.

TODO
----

* documentation
* precommit

Changelog
---------

2020.9.7
^^^^^^^^

* Remove E203 in ``flake8`` for ``black`` compatibility

2020.9.4
^^^^^^^^

* Add ``whatalinter_vscode`` for Visual Studio Code integration

2020.9.2
^^^^^^^^

* Remove some warnings of ``wemake-python-styleguide``, for instance allow f-strings

2020.9.1
^^^^^^^^

* Use ``poetry``
* Remove redundant linters
* Change max line length to 88 (default value of ``black``)
* Replace ``pydocstyle`` with ``flake8-docstrings``
* Add ``wemake-python-styleguide``

2019.10.22
^^^^^^^^^^

* Add ``flake8-2020`` linter

2019.07.21
^^^^^^^^^^

* Add ``--quiet`` and ``--diff`` flags to ``whataformatter`` for VS Code compatibility

2019.07.20
^^^^^^^^^^

* Add ``black`` formatter
* Add ``autoflake`` formatter
* Add ``pyupgrade`` formatter

2019.04.08
^^^^^^^^^^

* Add ``flake8`` linter
* Add ``flake8-isort`` linter
* Add ``pep8-naming`` linter
* Add ``flake8-comprehensions`` linter
* Add ``flake8-logging-format`` linter
* Add ``flake8-bugbear`` linter
* Add ``flake8-builtins`` linter
* Add ``flake8-broken-line`` linter
* Add ``flake8-fixme`` linter
* Add ``flake8-mutable`` linter
* Add ``flake8-debugger`` linter
* Add ``flake8-variables-names`` linter
* Add ``flake8-bandit`` linter

2019.03.02
^^^^^^^^^^

* Add ``pydocstyle`` linter

2019.03.01
^^^^^^^^^^

* Add McCabe complexity checker

2019.02.26
^^^^^^^^^^

* Add ``pyflakes`` linter
* Add ``pycodestyle`` linter

2019.02.23
^^^^^^^^^^

* First release on PyPI.
