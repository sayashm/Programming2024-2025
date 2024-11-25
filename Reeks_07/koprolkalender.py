# https://dodona.be/nl/courses/4157/series/46296/activities/279985369
from datetime import date, timedelta


def rollover_date (day=None, month=None , year = None):
    '''
    >>> rollover_date(month=4, day=31)
    datetime.date(2024, 5, 1)
    >>> rollover_date(year=2016, month=15, day=43)
    datetime.date(2017, 4, 12)
    >>> rollover_date(year=2016, month=3, day=16)
    datetime.date(2016, 3, 16)
    >>> rollover_date(year=2016, month=12, day=64)
    datetime.date(2017, 2, 2)
    >>> rollover_date(year=2016, month=19, day=99)
    datetime.date(2017, 10, 7)
    >>> rollover_date(year=2016, month=19, day=2)
    datetime.date(2017, 7, 2)
    >>> rollover_date(year=2016, month=1, day=99999)
    datetime.date(2289, 10, 14)
    >>> rollover_date(year=2016, month=9999, day=10)
    datetime.date(2849, 3, 10)
    >>> rollover_date(day=30, year=2544, month=38)
    datetime.date(2547, 3, 2)
    '''
    if year is None:
        today  = date.today()
        year = today.year
    if month is None:
        today = date.today()
        month = today.month
    if day is None:
        today = date.today()
        day = today.day

    if month > 12:
        year += month //12
        month = month % 12

    if day > 29:
        delta = timedelta(day-1)

        return date(year,month, 1) + delta

    return date(year,month,day)