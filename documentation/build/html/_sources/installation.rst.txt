Installation
============

This documentation site is built with Sphinx and reStructuredText.
Follow the steps below to install the docs toolchain and generate HTML output.

Requirements
------------

- Python 3.11 or newer
- ``pip`` package manager

Install dependencies
--------------------

From the repository root:

.. code-block:: console

   python -m pip install -r documentation/requirements.txt

Build the documentation
-----------------------

From the ``documentation`` folder:

.. code-block:: console

   make html

On Windows, run:

.. code-block:: console

   make.bat html

Output location
---------------

The generated HTML site is written to:

- ``documentation/build/html``

Open ``documentation/build/html/index.html`` in your browser to preview the site.
