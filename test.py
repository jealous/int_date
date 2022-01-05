""" this package verifies the function of the ``int_date`` module """
import datetime
from unittest import TestCase

from hamcrest import assert_that, equal_to, greater_than, none

from int_date import int_date, get_interval, from_diff, in_date, \
    in_year, in_month, get_workdays, today, to_date

__author__ = 'Cedric Zhuang'


class TestIntDate(TestCase):
    """ Tests for the int date utilities """

    @staticmethod
    def test_get_date_from_int():
        """ Get a date from an integer """
        date = to_date(20120515)
        assert_that(date.year, equal_to(2012))
        assert_that(date.month, equal_to(5))
        assert_that(date.day, equal_to(15))

    def test_get_date_from_int_error(self):
        """ Report error when the integer is an invalid date"""
        with self.assertRaises(ValueError):
            to_date(20120532)

    @staticmethod
    def test_string_to_date():
        """ Converts different format of strings to an int date """
        value = ('20120517', '2012/05/17', '2012-05-17')
        for date in value:
            date = to_date(date)
            assert_that(date.year, equal_to(2012))
            assert_that(date.month, equal_to(5))
            assert_that(date.day, equal_to(17))

    @staticmethod
    def test_get_day_interval():
        """ Get the days between two int dates """
        interval = get_interval(20120530, '2012-06-02')
        assert_that(interval, equal_to(3))

    @staticmethod
    def test_get_day_interval_negative():
        """ Interval from future to past returns negative days """
        interval = get_interval(20120503, 20120324)
        assert_that(interval, equal_to(-40))

    @staticmethod
    def test_get_date_from_diff_before():
        """ Get an int date from a start and an interval """
        assert_that(from_diff(20120503, -40), equal_to(20120324))

    @staticmethod
    def test_get_date_from_diff_zero():
        """ Get the date from zero diff """
        assert_that(from_diff(20120503, 0), equal_to(20120503))

    @staticmethod
    def test_get_date_from_diff_next():
        """ Get future date with a positive diff """
        assert_that(from_diff('2012/02/28', 2), equal_to(20120301))

    @staticmethod
    def test_to_int_date():
        """ Retrieve an int date from a datetime object """
        date = int_date(datetime.datetime(2015, 5, 21))
        assert_that(date, equal_to(20150521))

        date = int_date(datetime.date(2015, 5, 21))
        assert_that(date, equal_to(20150521))

    def test_new_with_invalid_str_date(self):
        """ Report value error when converting from an invalid date string """
        with self.assertRaises(ValueError):
            int_date('2015/11/31')

    def test_new_with_invalid_float_date(self):
        """ Report value error when converting an invalid float """
        with self.assertRaises(ValueError):
            int_date(20151131.0)

    @staticmethod
    def test_to_int_date_int_input():
        """ Retrieve an int date from an int date """
        date = int_date(19831102)
        assert_that(date, equal_to(19831102))

    @staticmethod
    def test_new_int_date():
        """ Retrieve an int date from a string sep. by - """
        date = int_date('2015-1-3')
        assert_that(date, equal_to(20150103))

    @staticmethod
    def test_to_int_date_none():
        """ Call new int date with None returns None """
        date = int_date(None)
        assert_that(date, none())

    @staticmethod
    def test_to_int_date_str_1():
        """ Retrieve an int date from a string without sep. """
        date = int_date('20151123')
        assert_that(date, equal_to(20151123))

    @staticmethod
    def test_to_int_date_str_2():
        """ Retrieve an int date from a string sep. by / """
        date = int_date('2015/11/23')
        assert_that(date, equal_to(20151123))

    @staticmethod
    def test_to_int_date_unicode():
        """ Retrieve an int date from a unicode string sep. by / """
        date = int_date(u'2015/11/23')
        assert_that(date, equal_to(20151123))

    def test_to_int_date_str_error(self):
        """ Report value error converting an invalid date string """
        value = ('20151301', '201512001')
        for date_str in value:
            with self.assertRaises(ValueError):
                int_date(date_str)

    @staticmethod
    def test_in_month():
        """ Use in_month to check the month of an int date """
        assert_that(in_month(20140503, *[3, 5, 7]), equal_to(True))
        assert_that(in_month('2014-05-03', *{3, 5, 7}), equal_to(True))
        assert_that(in_month('2014/05/03', *(3, 5, 7)), equal_to(True))
        assert_that(in_month(20140131, *[3, 5, 7]), equal_to(False))
        assert_that(in_month(20140131, 1), equal_to(True))
        assert_that(in_month(20140131, 3), equal_to(False))

    @staticmethod
    def test_in_date():
        """ Use in_date to check the date of an int date """
        assert_that(in_date(20140503, *[3, 5, 7]), equal_to(True))
        assert_that(in_date('20140503', *{1, 5, 7}), equal_to(False))
        assert_that(in_date('2014/01/31', 31), equal_to(True))
        assert_that(in_date('2014-01-31', 30), equal_to(False))

    @staticmethod
    def test_in_year():
        """ Use in_year to check the year of an int date """
        assert_that(in_year(20140503, *[2013, 2014]), equal_to(True))
        assert_that(in_year(20140503, *{2013, 2015}), equal_to(False))
        assert_that(in_year('2014/01/31', 2014), equal_to(True))
        assert_that(in_year(20140131, 2013), equal_to(False))

    @staticmethod
    def test_today():
        """ Use today to retrieve the current int date """
        day = today()
        assert_that(day, greater_than(20150504))

    @staticmethod
    def test_get_workdays():
        """ Retrieve workdays in a duration """
        assert_that(get_workdays(20151202, 20151213), equal_to(8))
        assert_that(get_workdays(20151213, '20151202'), equal_to(-8))
        assert_that(get_workdays('2015/12/23', 20160105), equal_to(10))
