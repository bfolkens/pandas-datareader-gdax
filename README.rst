========
Overview
========

A library to retrieve GDAX historical data into a Pandas DataFrame, in a similar style to Pandas DataReader.


* Free software: BSD license

Installation
============

::

    pip install pandas-datareader-gdax

Example
=======

  import pytz
  from datetime import datetime
  from pandas_datareader_gdax import get_data_gdax

  # Retrieve the GDAX data into a dataframe
  df = get_data_gdax(
     'BTC-USD',
     granularity=5*60,
     start=datetime(2016, 6, 1, 7, 0, 0, tzinfo=pytz.timezone('UTC')),
     end=datetime(2017, 9, 1, 6, 59, 59, tzinfo=pytz.timezone('UTC'))
  )
