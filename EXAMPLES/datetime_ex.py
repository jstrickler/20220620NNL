#!/usr/bin/env python

from datetime import datetime, date, timedelta

today = date.today()
print("date.today():", today)  # <1>
print("today.day: {}".format(today.day))
print("today.month: {}".format(today.month))
print("today.year: {}".format(today.year))


now = datetime.now()  # <2>
print("now.day:", now.day)  # <3>
print("now.month:", now.month)
print("now.year:", now.year)
print("now.hour:", now.hour)
print("now.minute:", now.minute)
print("now.second:", now.second)

d1 = datetime(2018, 6, 13, 10, 31, 54)  # <4>
d2 = datetime(2018, 8, 24, 19, 1, 1)

d3 = d2 - d1  # <5>

print("raw time delta:", d3)
print("time delta days:", d3.days)  # <6>

interval = timedelta(10)  # <7>
print("interval:", interval)

d4 = d2 + interval  # <8>
d5 = d2 - interval
print("d2 + interval:", d4)
print("d2 - interval:", d5)
print()

t1 = datetime(2016, 8, 24, 10, 4, 34)  # <9>
t2 = datetime(2018, 8, 24, 22, 8, 1)
t3 = t2 - t1

print("datetime(2016, 8, 24, 10, 4, 34):", t1)
print("datetime(2018, 8, 24, 22, 8, 1):", t2)
print("time diff (t2 - t1):", t3)
