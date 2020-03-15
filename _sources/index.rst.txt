.. pypi-sphinx-quickstart documentation master file, created by
   pypi-sphinx-quickstart.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Cryptocompare-Py documentation!
*********************************************

To get started, look here.

.. toctree::

   tutorial


An overview
===========


cryptocompsdk
------------

This is a simple example::

    from cryptocompsdk import CryptoCompare
    API_KEY = 'my-api-key'
    cc = CryptoCompare(API_KEY)

    data = cc.history.get(from_symbol='BTC', to_symbol='USD', exchange='Kraken')
    df = data.to_df()

.. autosummary::

      cryptocompsdk.main.CryptoCompare

API Documentation
------------------

A full list of modules

.. toctree:: api/modules
   :maxdepth: 3

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
