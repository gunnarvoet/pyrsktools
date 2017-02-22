############
Introduction
############

pyRSKtools is the official Python port of the MATLAB-based `RSKtools`_ toolbox. It provides the same functionality
for users to access, process, visualize, and export data given in the RSK format from RBR loggers.

The RSK format that all `Logger2 and Logger3 instruments`_ (RBR *solo*, RBR *virtuoso*, RBR *duo*, RBR *concerto*, RBR *maestro*, etc)
generate is not just another proprietary file format. Rather, it is a widely-used single file database called `SQLite`_ that
allows for very large files with high-speed access to any part of the dataset. As a result, you can read
RSKs from any programming language that supports SQLite. All you need to know is the schema of our table structure.

The organization of pyRSKtools revolves around a `Python class`_ referred to as the :class:`.RSK` class which,
upon instantiation, will load deployment metadata of the given RSK, and may then later be used
to load, process, visualize, or export data. The RSK class supports two data formats: a continuous time series, or a
collection of profiles. After loading the data into the class, it is easy to plot and process the data using only the default
input arguments. All optional input arguments are name-value pair arguments which make the class methods customizable and flexible.

To learn how to install pyRSKtools, please click `installation`_. You may then wish to refer to our
`getting started`_ guide and `API overview`_ for further usage information. A `"sample.rsk"`_ file is available for testing purpose.

.. _RSKtools: https://rbr-global.com/support/matlab-tools
.. _Logger2 and Logger3 instruments: https://rbr-global.com/products/standard-loggers
.. _SQLite: https://sqlite.org/about.html
.. _Python class: https://docs.python.org/3/tutorial/classes.html
.. _installation: installation.html
.. _getting started: getting-started.html
.. _API overview: api-overview.html
.. _"sample.rsk": https://bitbucket.org/rbr/pyrsktools/raw/master/sample.rsk