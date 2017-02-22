############
Installation
############

Download and install the current stable version of pyRSKtools with `pip`_:

.. code-block:: bash

    python -m pip install pyrsktools

.. NOTE::

    * `Python 3.8`_ or later is required.

    * The `TEOS-10 GSW`_ toolkit is a dependency installed automatically with pyRSKtools and may require a C compiler on some versions of the Windows and macOS operating systems (depending upon the availability/compatibility of `precompiled build distributions <https://pypi.org/project/gsw/#files>`_ provided by GSW). If you run into errors relating to this during installation, please install a compiler for your system before trying again.
        
        - For Windows, you may get a compiler by downloading `Microsoft Build Tools`_.
        - For macOS, you may get a compiler by downloading `Xcode`_.


After pyRSKtools has been installed, you may refer to the `getting started`_ guide or `API reference`_ for usage information.

For development and previous versions, browse the `Bitbucket repository`_.
For information on how to clone, install, and edit the source code directly, please see the `contributors guide`_.


.. _Python 3.8: https://www.python.org/downloads/
.. _pip: https://pip.pypa.io/en/stable/
.. _TEOS-10 GSW: https://github.com/TEOS-10/GSW-Python>
.. _RBR website: https://rbr-global.com/products/software
.. _getting started: guides/getting-started-guide.html
.. _API reference: rsk.html
.. _Bitbucket repository: https://bitbucket.org/rbr/pyrsktools
.. _contributors guide: contributing.html
.. _Microsoft Build Tools: https://visualstudio.microsoft.com/visual-cpp-build-tools/
.. _Xcode: https://developer.apple.com/xcode/