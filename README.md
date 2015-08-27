# Integer Date utilities

[![Build Status](https://travis-ci.org/jealous/int_date.svg?branch=master)](https://travis-ci.org/jealous/int_date)
[![Coverage Status](https://coveralls.io/repos/jealous/int_date/badge.svg?branch=master&service=github)](https://coveralls.io/github/jealous/int_date?branch=master)

Utilities to process the integer format date like: 20150301
First four digits are year.  Next two are month.  Last two are date.

To file issue, please visit:

https://github.com/jealous/int_date

Documentation for the package is available at:

http://int-date.readthedocs.org/en/latest/int_date.html

Contact author:

cedric.zhuang@gmail.com

# Example

```
>>> to_int_date('2015-11-02')
20151102

>>> get_int_day_interval(19831102, 20141225)
11376

>>> get_date_from_int(19831102)
datetime.date(1983, 11, 2)

>>> today()
20150827

>>> in_year(20150412, 2013, 2012)
False

>>> in_month(20150412, 4, 3, 10)
True

>>> in_date(20150412, 2)
False
```