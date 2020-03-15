Getting started with cryptocompsdk
**********************************

Install
=======

Install via::

    pip install cryptocompsdk


API Key
=========

If you don't already have an API key, sign up at https://min-api.cryptocompare.com/pricing


Usage
=========

This is a simple example::

    from cryptocompsdk import CryptoCompare
    API_KEY = 'my-api-key'
    cc = CryptoCompare(API_KEY)

    data = cc.history.get(from_symbol='BTC', to_symbol='USD', exchange='Kraken')
    df = data.to_df()


More details on usage coming later. There is also an SDK for the social, coins,
exchange symbols, and exchange info, blockchain available symbols, and
blockchain history APIs. Access them via attributes of the main
:class:`.CryptoCompare` class.