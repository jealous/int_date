from datetime import datetime, timedelta, date
import time

__author__ = 'Cedric Zhuang'
__version__ = '0.0.1'


def get_date_from_int(int_date):
    date_str = "%s" % int(int_date)
    return datetime.strptime(date_str, "%Y%m%d").date()


def get_int_day_interval(int_left, int_right):
    left_date = get_date_from_int(int_left)
    right_date = get_date_from_int(int_right)
    delta = right_date - left_date
    return delta.days


def get_date_from_diff(i_date, delta_day):
    d = get_date_from_int(i_date)
    d += timedelta(delta_day)
    return date_to_int(d)


def date_to_int(the_day):
    return the_day.year * 10000 + the_day.month * 100 + the_day.day


def get_today():
    the_day = date.today()
    return date_to_int(the_day)


def convert_date(data_str):
    """
    convert string '2015-01-30' to int 20150130
    :return: int format of date
    """
    ret = None

    if '-' in data_str:
        ret = int(data_str.replace('-', ''))
    elif '/' in data_str:
        ret = int(data_str.replace('/', ''))

    return ret


def in_month(day, months):
    """
    check if day is in months list
    :param day: date
    :param months: list of months
    :return: true if in, otherwise false
    """
    month = int(day % 10000 / 100)
    return month in months


def today():
    """
    get today in ints, example: Jan 12, 2015 is 20150112
    :return: ints of date today
    """
    return int(time.strftime("%Y%m%d"))
