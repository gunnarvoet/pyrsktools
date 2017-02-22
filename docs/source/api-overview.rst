############
API overview
############

The entire organization of pyRSKtools revolves around the :class:`.RSK` class.
In fact, most (if not all) ancillary classes you will find later in this API reference,
like those documented in the `Channels <channels.html>`_ and `Datatypes <datatypes.html>`_ sections,
are used by the :class:`.RSK` class internally.
This section serves to provide insight into the inner workings of the :class:`.RSK` class.

RSK attributes
================================

The :class:`.RSK` class has several instance attributes that we have split into three logical
groups. Logically grouping attributes allows us to explain how those within a group
relate to one another and how each group differs in utility. Below, we summarize
each grouping, if you are looking for information about attributes within each group,
please refer to the :class:`.RSK` class documentation.

**Internal state:**

Internal state attributes hold metadata relating to the :class:`.RSK` class itself.
For example, :obj:`.RSK.version` holds the current
pyRSKtools version, while :obj:`.RSK.logs` is used to log information about the
actions/methods conducted/invoked during the lifetime of an :class:`.RSK` class instance.

**Informational:**

Informational attributes hold metadata relating to an RSK file.
They are populated with (meta)data read in from the opened RSK file you are dealing with.
For example, :obj:`.RSK.dbInfo` and :obj:`.RSK.instrument` are populated when you invoke
:meth:`.RSK.open`, they respectively contain information about the RSK database (e.g., version and type)
and the instrument (e.g., serialID and model) the RSK file pertains to.

It is worth noting that, although these attributes contain a large amount of
information about an RSK file, they primarily will be used internally by
methods already provided by the :class:`.RSK` class. Despite this, we keep them
accessible to the curious user or for any potential advanced/custom development.

**Computational:**

Computational attributes hold the sample/channel data contained within an RSK.
For example, the :obj:`.RSK.data` and :obj:`.RSK.channelNames` computational attributes
are populated by the :meth:`.RSK.readdata` method, they respectively contain data of
the RSK file and the channel names used to index into said data.

Importantly, computational fields such as :obj:`.RSK.data` are exposed
as `NumPY <NP_>`_ `structured arrays <SA_>`_. Below we provide a brief overview of
a few key NumPY concepts to help pyRSKtools users get started, we recommend
checking out the official `NumPY reference documentation <NRD_>`_ for more information.

A brief NumPY review
======================

The two key NumPY concepts pyRSKtools users should get familiar with are
`structured arrays <SA_>`_ and `datetime64 <DT_>`_ objects. 

**Structured arrays:**

The NumPY `structured array <SA_>`_ is a convenient datatype that allows
users to efficiently store heterogeneous compound/composite data in a way
that can be easily accessed/indexed via named labels. 

To manually create a structured array, users must specify
a properly formed `dtype <DTYPE_>`_ argument when creating a standard
NumPY `array <ARR_>`_ type.

.. code-block:: python

    import numpy as np

    data = np.array(
        [
            (1660571192060, 42.784, 22.93, 9.96),
            (1660571192065, 42.785, 22.92, 9.95),
        ],
        dtype=[
            ("timestamp", "datetime64[ms]"),
            ("conductivity", "float64"),
            ("temperature", "float64"),
            ("pressure", "float64"),
        ],
    )

The above example creates a structured array with four labeled columns
and two rows of data. The values along a given column may now be accessed
by their respective labels, as shown below: 

.. code-block:: python

    timestamps = data["timestamp"] # = ['2022-08-15T13:46:32.060', '2022-08-15T13:46:32.065']
    c = data["conductivity"]       # = [42.784, 42.785]
    t = data["temperature"]        # = [22.93, 22.92]
    d = data["pressure"]           # = [9.96, 9.95]


**Important**: indexing a structured array by number
will yield the entire row (starting from index 0), not a column.
To access a specific value of a row from a given column, simply specify
the row and column name. See the examples below:

.. code-block:: python

    data[0]                                 # = ('2022-08-15T13:46:32.060', 42.784, 22.93, 9.96)
    data[0]['conductivity']                 # = 42.784
    data["conductivity"][0]                 # = 42.784 (equivalent to above)
    data[0][["conductivity", "pressure"]]   # = (42.784, 9.96)
    data.dtype.names                        # = ('timestamp', 'conductivity', 'temperature', 'pressure')

Given that RSK data consists of multiple samples, each of which havs a fixed number of channels,
structured arrays become and convenient way to store data in pyRSKtools.
If you were to refer back to our `getting started guide <guides/getting-started-guide.html>`_, 
you may find it more apparent that a structured array underpins :obj:`.RSK.data` and
:obj:`.RSK.channelNames` simply returns all the channel (dtype) names of :obj:`.RSK.data`
(excluding the `"timestamp"` column).


**Datetime64 objects:**

In the code examples above, you may have noticed that the `"timestamp"` field
was given the type `datetime64[ms]`; a NumPY `datetime64 <DT_>`_ object. The
NumPY `datetime64` is used throughout pyRSKtools for representation, conversion, 
and processing of any date/time related fields, including the timestamp of each
sample in :obj:`.RSK.data`.

Examples of manually creating `datetime64` objects are given below:

.. code-block:: python

    # Using the standard ISO 8601 format (precision of seconds in this example)
    dt = np.datetime64("2022-08-15T11:18:34")
    # Convert to a 64-bit unsigned integer
    seconds = dt.astype(np.uint64)
    # Using milliseconds
    np.datetime64(1660562314000, "ms")

.. _NP: https://numpy.org/
.. _SA: https://numpy.org/doc/stable/user/basics.rec.html
.. _ARR: https://numpy.org/doc/stable/reference/generated/numpy.array.html?highlight=array#numpy.array
.. _DTYPE: https://numpy.org/doc/stable/reference/generated/numpy.dtype.html?highlight=dtype#numpy.dtype
.. _NRD: https://numpy.org/doc/stable/reference/index.html
.. _DT: https://numpy.org/doc/stable/reference/arrays.scalars.html?highlight=datetime#numpy.datetime64