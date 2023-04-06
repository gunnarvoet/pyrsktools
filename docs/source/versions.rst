############################
Versions
############################

Supported RSK versions
======================

RSK files have different types and versions,
either of which may lead to differences in the underlying dataset structure.
pyRSKtools currently supports RSKs that are:

* "full" version from 2.0.0 to 2.18.2
* "EPdesktop" version from 1.13.4 to 2.18.2 

.. Note::

    The version of an RSK file can be easily upgraded using RBR's `Ruskin software <RUSKIN_>`_.
    Upon installing Ruskin, simply:

    * Open your RSK file with Ruskin.

    * Go to the ``File info`` tab, which presents the current version and structure type.

    * Ruskin will detect whether there is a new version of the RSK file format is available. If so, there will be an ``Update`` button for you to upgrade your RSK file.

    * After clicking the ``Update`` button, a new RSK file of the latest version will be created in your specified directory. 

pyRSKtools legacy versions
==========================

The legacy versions of pyRSKtools (v0.1.9 and before) are no longer maintained moving forward. But the legacy version (v0.1.9) is available in `PyPI`_. 
Users with existing codes based on pyRSKtools (v0.1.8) may install the legacy version by specifying the version number:

.. code-block:: bash

    python -m pip install pyrsktools == 0.1.9

.. _RUSKIN: https://rbr-global.com/products/software/
.. _PyPI: https://pypi.org/project/pyRSKtools/0.1.9/