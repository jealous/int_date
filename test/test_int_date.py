from unittest import TestCase
from hamcrest import assert_that, equal_to, greater_than
import int_date

__author__ = 'Cedric Zhuang'


class TestIntDate(TestCase):
    def test_get_date_from_int(self):
        date = int_date.get_date_from_int(20120515)
        assert_that(date.year, equal_to(2012))
        assert_that(date.month, equal_to(5))
        assert_that(date.day, equal_to(15))

    def test_get_day_interval(self):
        interval = int_date.get_int_day_interval(20120530, 20120602)
        assert_that(interval, equal_to(3))

    def test_get_date_from_diff_before(self):
        assert_that(int_date.get_date_from_diff(20120503, -40),
                    equal_to(20120324))

    def test_get_date_from_diff_zero(self):
        assert_that(int_date.get_date_from_diff(20120503, 0),
                    equal_to(20120503))

    def test_get_date_from_diff_next(self):
        assert_that(int_date.get_date_from_diff(20120228, 2),
                    equal_to(20120301))

    def test_in_month(self):
        assert_that(int_date.in_month(20140503, [3, 5, 7]), equal_to(True))
        assert_that(int_date.in_month(20140131, [3, 5, 7]), equal_to(False))

    def test_get_today(self):
        today = int_date.get_today()
        assert_that(today, greater_than(20150504))
