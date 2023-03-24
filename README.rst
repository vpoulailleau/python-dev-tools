Python Dev Tools
================

Needed and up-to-date tools to develop in Python (*WORK IN PROGRESS*)


.. image:: https://img.shields.io/pypi/v/python_dev_tools.svg
        :target: https://pypi.python.org/pypi/python_dev_tools

.. image:: https://img.shields.io/pypi/l/python_dev_tools.svg
        :target: https://github.com/vpoulailleau/python_dev_tools/blob/master/LICENSE

.. image:: https://img.shields.io/pypi/pyversions/python_dev_tools.svg?logo=python&amp;logoColor=fff
        :target: https://pypi.python.org/pypi/python_dev_tools

.. image:: https://github.com/vpoulailleau/python-dev-tools/actions/workflows/tests.yml/badge.svg
        :target: https://github.com/vpoulailleau/python-dev-tools/actions/workflows/tests.yml

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

Supported Python versions: the same as the classic Python interpreter (CPython)

Documentation
-------------

The full documentation can be read at https://python-dev-tools.readthedocs.io.

Installation
------------

In a terminal, run:

.. code-block:: console

    $ python3 -m pip install python-dev-tools --user --upgrade

Full documentation on installation: https://python-dev-tools.readthedocs.io/en/latest/installation.html

That's it! Use the provided linter (``flake8``), formatter (``whataformatter``) and
precommit hook (TODO) where applicable.

Installation with Visual Studio Code
------------------------------------

* Follow the installation procedure for python-dev-tools
* Be sure to have the official Python extension installed in VS Code
* Open VS Code from within your activated virtual environment (in fact, make sure that 
  ``flake8`` from python-dev-tools is in your ``PYTHON_PATH``)
* In VS Code, open settings (F1 key, then type "Open Settings (JSON)",
  then enter)
* Add in the opened JSON file (before the closing ``}``):

.. code:: javascript

    "python.linting.enabled": true,
    "python.linting.flake8Enabled": true,
    "python.linting.flake8Path": "flake8",
    "python.formatting.provider": "black",
    "python.formatting.blackPath": "whataformatter",
    "python.formatting.blackArgs": [],

Features
--------

Integrate features of commonly used tools. This package provides usual
dependencies to develop Python software.

* Simple linter

  * ``flake8 a_python_file.py`` lints a_python_file.py
  * based on flake8 and plugins: https://gitlab.com/pycqa/flake8

    * darglint: https://github.com/terrencepreilly/darglint
    * dlint: https://github.com/dlint-py/dlint
    * flake8-2020: https://github.com/asottile/flake8-2020
    * flake8-aaa: https://github.com/jamescooke/flake8-aaa
    * flake8-annotations: https://github.com/sco1/flake8-annotations
    * flake8-annotations-complexity: https://github.com/best-doctor/flake8-annotations-complexity
    * flake8-annotations-coverage: https://github.com/best-doctor/flake8-annotations-coverage
    * flake8-bandit: https://github.com/tylerwince/flake8-bandit
    * flake8-blind-except: https://github.com/elijahandrews/flake8-blind-except
    * flake8-breakpoint: https://github.com/afonasev/flake8-breakpoint
    * flake8-broken-line: https://github.com/sobolevn/flake8-broken-line
    * flake8-bugbear: https://github.com/PyCQA/flake8-bugbear
    * flake8-builtins: https://github.com/gforcada/flake8-builtins
    * flake8-class-attributes-order: https://github.com/best-doctor/flake8-class-attributes-order
    * flake8-coding: https://github.com/tk0miya/flake8-coding
    * flake8-cognitive-complexity: https://github.com/Melevir/flake8-cognitive-complexity
    * flake8-comments: https://github.com/orsinium-labs/flake8-comments
    * flake8-comprehensions: https://github.com/adamchainz/flake8-comprehensions
    * flake8-debugger: https://github.com/JBKahn/flake8-debugger
    * flake8-django: https://github.com/rocioar/flake8-django
    * flake8-docstrings: https://gitlab.com/pycqa/flake8-docstrings
    * flake8-encoding: https://github.com/python-formate/flake8-encodings
    * flake8-eradicate: https://github.com/sobolevn/flake8-eradicate
    * flake8-executable: https://github.com/xuhdev/flake8-executable
    * flake8-expression-complexity: https://pypi.org/project/flake8-expression-complexity/
    * flake8-fastapi: https://pypi.org/project/flake8-fastapi/
    * flake8-fixme: https://github.com/tommilligan/flake8-fixme
    * flake8-functions: https://github.com/best-doctor/flake8-functions
    * flake8-functions-names: https://github.com/Melevir/flake8-functions-names
    * flake8-future-annotations: https://github.com/tyleryep/flake8-future-annotations
    * flake8-isort: https://github.com/gforcada/flake8-isort
    * flake8-literal: https://github.com/plinss/flake8-literal
    * flake8-logging-format: https://github.com/globality-corp/flake8-logging-format
    * flake8-markdown: https://github.com/johnfraney/flake8-markdown
    * flake8-mutable: https://github.com/ebeweber/flake8-mutable
    * flake8-no-pep420: https://github.com/adamchainz/flake8-no-pep420
    * flake8-noqa: https://pypi.org/project/flake8-noqa/
    * flake8-pie: https://github.com/sbdchd/flake8-pie
    * flake8-pylint: https://github.com/orsinium-labs/flake8-pylint
    * flake8-pyi: https://github.com/PyCQA/flake8-pyi
    * flake8-pytest-style: https://github.com/m-burst/flake8-pytest-style
    * flake8-quotes: https://github.com/zheller/flake8-quotes/
    * flake8-rst-docstrings: https://github.com/peterjc/flake8-rst-docstrings
    * flake8-secure-coding-standard: https://github.com/Takishima/flake8-secure-coding-standard
    * flake8-simplify: https://github.com/MartinThoma/flake8-simplify
    * flake8-slots: https://github.com/python-formate/flake8-slots
    * flake8-string-format: https://github.com/xZise/flake8-string-format
    * flake8-tidy-imports: https://github.com/adamchainz/flake8-tidy-imports
    * flake8-typing-imports: https://github.com/asottile/flake8-typing-imports
    * flake8-use-fstring: https://github.com/MichaelKim0407/flake8-use-fstring
    * flake8-use-pathlib: https://gitlab.com/RoPP/flake8-use-pathlib
    * flake8-useless-assert: https://github.com/decorator-factory/flake8-useless-assert
    * flake8-variables-names: https://github.com/best-doctor/flake8-variables-names
    * flake8-warnings: https://github.com/orsinium-labs/flake8-warnings
    * pandas-vet: https://github.com/deppen8/pandas-vet
    * pep8-naming: https://github.com/PyCQA/pep8-naming
    * wemake-python-styleguide: https://github.com/wemake-services/wemake-python-styleguide

* Simple formatter

  * ``whataformatter a_python_file.py`` formats a_python_file.py
  * based on

    * autoflake: https://github.com/myint/autoflake
    * black: https://github.com/python/black
    * docformatter: https://github.com/PyCQA/docformatter
    * isort: https://github.com/PyCQA/isort
    * pybetter: https://github.com/lensvol/pybetter
    * pycln: https://github.com/hadialqattan/pycln
    * pyupgrade: https://github.com/asottile/pyupgrade
    * removestar: https://github.com/asmeurer/removestar
    * ssort: https://github.com/bwhmather/ssort

* Simple precommit hook

  * TODO

License
-------

BSD 3-Clause license, feel free to contribute: https://python-dev-tools.readthedocs.io/en/latest/contributing.html.

TODO
----

* flake8 formatter to add URL to information on a warning
* documentation
* precommit (flake8, mypy)

Changelog
---------

2023.3.24
^^^^^^^^^

* Require Python3.8.1+
* Upgrade to ``flake8`` 5 (most plugins not available for ``flake8`` 6 yet)
* Add ``flake8-fastapi`` linter

2022.5.27
^^^^^^^^^

* Add ``flake8-aaa`` linter
* Add ``flake8-blind-except`` linter
* Add ``flake8-breakpoint`` linter
* Add ``flake8-class-attributes-order`` linter
* Add ``flake8-cognitive-complexity`` linter
* Add ``flake8-coding`` linter
* Add ``flake8-comments`` linter
* Add ``flake8-django`` linter
* Add ``flake8-encoding`` linter
* Add ``flake8-executable`` linter
* Add ``flake8-functions-names`` linter
* Add ``flake8-future-annotations`` linter
* Add ``flake8-literal`` linter
* Add ``flake8-markdown`` linter
* Add ``flake8-noqa`` linter
* Add ``flake8-no-pep420`` linter
* Add ``flake8-pie`` linter
* Add ``flake8-pyi`` linter
* Add ``flake8-pylint`` linter
* Add ``flake8-secure-coding-standard`` linter
* Add ``flake8-slots`` linter
* Add ``flake8-use-pathlib`` linter
* Add ``flake8-useless-assert`` linter
* Add ``flake8-warnings`` linter
* Add ``pandas-vet`` linter

2022.5.26
^^^^^^^^^

* Add ``docformatter`` formatter
* Add ``isort`` formatter
* Add ``pybetter`` formatter
* Add ``pycln`` formatter
* Add ``removestar`` formatter
* Add ``ssort`` formatter
* Remove ``cohesion`` linter (false warnings on pure data classes such as ``NamedTuple``)

2022.5.20
^^^^^^^^^

* Add ``cohesion`` linter
* Add ``dlint`` linter
* Add ``flake8-annotations`` linter
* Add ``flake8-annotations-complexity`` linter
* Add ``flake8-annotations-coverage`` linter
* Add ``flake8-black`` linter
* Add ``flake8-expression-complexity`` linter
* Add ``flake8-functions`` linter
* Add ``flake8-pytest-style`` linter
* Add ``flake8-simplify`` linter
* Add ``flake8-tidy-imports`` linter
* Add ``flake8-typing-imports`` linter
* Add ``flake8-use-fstring`` linter
* Remove ``flake8-commas`` linter that is deprecated
* Fix ``whataformatter`` and add ``--target-version`` option for VS Code compatibility

2020.9.10
^^^^^^^^^

* The path provided to ``whatalinter`` can be the one of a directory
  (recursive search of Python files)

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
