RAKE
====

About
-----

A Python implementation of the Rapid Automatic Keyword Extraction (RAKE) algorithm as described in:
Rose, S., Engel, D., Cramer, N., & Cowley, W. (2010). Automatic Keyword Extraction from Individual Documents.
In M. W. Berry & J. Kogan (Eds.), Text Mining: Theory and Applications: John Wiley & Sons.

Getting Started
------
To set up virtualenv:

.. code-block:: bash

    make env
    . env/bin/activate

To start a REPL shell where you can enter text and see Rake results:

.. code-block:: bash

    python -m rake.repl

For more information, pass `--verbose` argument to the `rake.repl` script.

License
-------
The source code is released under the MIT License.
