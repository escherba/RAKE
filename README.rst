RAKE
====

About
-----

A Python implementation of the Rapid Automatic Keyword Extraction (RAKE) algorithm as described in [RAKE2010]_.

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

Bibliography
------------

.. [RAKE2010]
   Rose, S., Engel, D., Cramer, N. and Cowley, W. (2010) Automatic Keyword Extraction from Individual Documents,
   in Text Mining: Applications and Theory (eds M. W. Berry and J. Kogan), John Wiley & Sons, Ltd, Chichester, UK.
   http://dx.doi.org/10.1002/9780470689646.ch1

License
-------
The source code is released under the MIT License.
