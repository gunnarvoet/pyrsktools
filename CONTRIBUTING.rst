####################################
Code contributions
####################################

This documentation is for those interested in helping in
the development/improvement of pyRSKtools. If you are only looking 
to use pyRSKtools as a library, please see the standard `installation instructions`_.

Development of pyRSKtools requires the use of `Git <https://git-scm.com/>`_ for source code version control.
The official remote public repository for pyRSKtools is hosted on Bitbucket at `<https://bitbucket.org/rbr/pyrsktools>`_.

Setting up a development environment
==============================================

The steps below outline how to set up a basic development environment from a UNIX-like command line interface (CLI).

1. Cloning pyRSKtools:

.. code-block:: bash

    git clone https://bitbucket.org/rbr/pyrsktools.git

2. Setting up a virtual environment:

.. code-block:: bash

    cd pyrsktools
    python -m venv env
    source env/bin/activate

3. Installing pyRSKtools' standard and development dependencies:

.. code-block:: bash

    pip install -e .[dev]


You may now freely edit and import/run pyRSKtools to your liking.
For information on style guidelines and running tests, see below.

Style guidelines
==============================================

pyRSKtools uses `Black <https://black.readthedocs.io>`_ and `mypy <http://mypy-lang.org/>`_ to ensure
code remains consistent in style and type hinting. Style and type hinting are enforced
over code pushed to Bitbucket (see `bitbucket-pipelines.yml`_). It is highly recommended you run these tools
against any changes you make before pushing them.

If you have already setup your `development environment`_, you may:

Run black against the entire code base with:

.. code-block:: bash

    black --check pyrsktools


Run mypy using pyRSKtools' custom configuration with:

.. code-block:: bash

    mypy --config mypy.ini pyrsktools


Running tests
==============================================

Tests are located in the ``tests`` directory at the base of the repository.
Assuming you have already setup your `development environment`_, you may run
all tests with:

.. code-block:: bash

    python -m unittest discover tests


See the official Python `unittest`_ documentation for more information.

.. Submitting pull requests
.. ==============================================

####################################
Documentation contributions
####################################

The full source code for this documentation is located
at the base of the repository in the ``docs`` directory.
All documentation is built and generated using `Sphinx`_.

Viewing/compiling locally
==============================================

To generate the HTML you are viewing currently, you may use
the provided ``Makefile`` in the ``docs`` directory:

.. code-block:: bash

    make html

This command will create the ``build`` directory in
``docs``, the generated HTML will be stored in ``build/html``.
To view the documentation, you may open ``build/html/index.html`` with your
browser directly or, alternatively, you may run the ``make`` command below:

.. code-block:: bash

    make serve

This will generate the HTML documentation and serve it locally 
on port ``8000``. Type `<http://0.0.0.0:8000>`_ in your browser to access it.

.. ####################################
.. Reporting issues
.. ####################################

.. Bugs
.. ==============================================

.. TODO

.. Enhancements/feature requests
.. ==============================================

.. TODO

.. _installation instructions: installation.html
.. _bitbucket-pipelines.yml: https://bitbucket.org/rbr/pyrsktools/src/master/bitbucket-pipelines.yml
.. _development environment: #setting-up-a-development-environment
.. _unittest: https://docs.python.org/3/library/unittest.html
.. _Sphinx: https://www.sphinx-doc.org