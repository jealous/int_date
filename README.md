# Integer Date utilities

[![build & test](https://github.com/jealous/int_date/actions/workflows/build-test.yml/badge.svg)](https://github.com/jealous/int_date/actions/workflows/build-test.yml)
[![coverage](https://codecov.io/gh/jealous/int_date/branch/master/graph/badge.svg?token=GBRWXbRgYm)](https://codecov.io/gh/jealous/int_date)
[![pypi](https://img.shields.io/pypi/v/int_date.svg)](https://pypi.python.org/pypi/int_date)

    
VERSION: 0.2.0

This module contains the utilities for operating integer date, such as: 20150301

#### Issues

We use [Github Issues](https://github.com/jealous/int_date) to manage the issues.

#### Contact author:

cedric.zhuang@gmail.com

## LICENSE

[BSD License](./LICENSE.txt)

## API Document

### `int_date`

Converts the input to an integer that represents a date.

* Parameter: a `str`, `datetime.datetime`, `datetime.date` or number
* Exception: `ValueError` if the input could not be converted
* Return: an integer represents a date

Examples:
``` python
>>> int_date(10121015.0)
10121015

>>> int_date('2012/10/15')
10121015

>>> int_date('2012-10-15')
10121015

>>> int_date(datetime.date(2015, 5, 21))
20150521
```

### `to_date`

Converts the input to `datetime.date`

* Parameter: a `str` or number
* Exception: `ValueError` if the input could not be converted
* Return: a `datetime.date` object

Examples:
``` python
>>> to_date(20151205)
datetime.date(2015, 12, 5)

>>> to_date('2015-12-05')
datetime.date(2015, 12, 5)
```

### `get_interval`

Retrieve the days between two dates.
* Parameter: 2 inputs that represents valid dates
* Exception: `ValueError` if any of the input is not valid
* Return: the days in between

Examples:
``` python
>>> get_interval(20120530, '2012-06-02')
3

>>> get_interval('2012/6/6', '2012-06-02')
-4                                        
```

### `from_diff`

Retrieve the int date from a start date and a delta.

* Parameter: a start date and a delta
* Exception: `ValueError` if start date is not valid
* Return: the result date

Examples:
``` python
>>> from_diff('2012-7-31', 5)
20120805

>>> from_diff('2012/8/3', -10)
20120724
```

### `in_month`, `in_date` & `in_year`

Check whether the int date matches the specified month, date or year.

* Parameter: an int date and multiple value to match
* Exception: `ValueError` if the int date is not valid
* Return: true if it matches, false if not

Examples:
``` python
>>> in_date(20140503, *[3, 5, 7])      
True
                                   
>>> in_month('2014-05-03', *{3, 5, 7}) 
True
                                   
>>> in_month(20140131, *[3, 5, 7])     
False    

>>> in_date('2014-01-31', 30)
False                              
```

### `today`

Retrieve the int date that represents today.

### `get_workdays`

Retrieve the work days (Monday~Friday) between two dates

* Parameter: two int dates mark the start and end, both ends are inclusive
* Exception: `ValueError` if the input date is not valid
* Return: number of workdays

Example:
``` python
# Note: 2022-01-03 is Monday
>>> get_workdays(20220102, 20220108)
5

>>> get_workdays(20220102, 20220107)
5

>>> get_workdays(20220102, 20220106)
4
```