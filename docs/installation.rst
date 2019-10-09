.. highlight:: shell

============
Installation
============


Stable release
--------------

Preferred installation method
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Install pipx if not yet installed: https://pipxproject.github.io/pipx/installation/

Then in a terminal, run:

.. code-block:: console

    $ pipx install python_dev_tools

Then add the new :code:`bin` directory to the path. On Linux for instance, run:

.. code-block:: console

    $ TOOLS_PATH=$(ls -l ~/.local/bin/whataformatter | sed -e "s/.*-> //" | sed -e "s#/bin.*#/bin#")
    $ userpath prepend $TOOLS_PATH

Standard installation method
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To install Python Dev Tools, run this command in your terminal:

.. code-block:: console

    $ pip install python-dev-tools

This is the preferred method to install Python Dev Tools, as it will always
install the most recent stable release.

If you don't have `pip`_ installed, this `Python installation guide`_ can guide
you through the process.

Then pay attention to update your PATH environment variable appropriately.

.. _pip: https://pip.pypa.io
.. _Python installation guide: http://docs.python-guide.org/en/latest/starting/installation/


From sources
------------

The sources for Python Dev Tools can be downloaded from the `Github repo`_.

You can either clone the public repository:

.. code-block:: console

    $ git clone git://github.com/vpoulailleau/python_dev_tools

Or download the `tarball`_:

.. code-block:: console

    $ curl  -OL https://github.com/vpoulailleau/python_dev_tools/tarball/master

Once you have a copy of the source, you can install it with:

.. code-block:: console

    $ python setup.py install


.. _Github repo: https://github.com/vpoulailleau/python_dev_tools
.. _tarball: https://github.com/vpoulailleau/python_dev_tools/tarball/master
