# Working with dates in python.
# import datetime module.
# to make a date, use date() function of datetime module and pass year,mnth, date aas args.
import datetime

d = datetime.date(2019, 10, 23)
d1 = datetime.date(2003, 2, 22)
print(d, '\n', d1)

# to get the todays date automatically, can use today() mthod.

import datetime

today = datetime.date.today()
print(today)

# to get mpre details like year, month, day.
# use attributes like year, day, month of datetime.
import datetime

today = datetime.date.today()
print(f"""year: {today.year}\nday: {today.day}
      \nmonth: {today.month}""")

# to get the week day,
# ie 0 - Monday, 1 -Tuesday.....,6-Sunday
import datetime

d = datetime.date.today()
print(d.weekday())
# output is 5 since today is saturday and it corresponds to number 5.

# to get the weekday of a given input date.
import datetime

d = datetime.date(2017, 3, 22)
print(d.weekday())

################################################################################################333

# Timedeltas
# timedeltas can be used to do operations on two diff dates.
# adding two dates, subtracting a date from another.
# thus we can find out what wud be the date after 7 days, or 7 days before from todays date.


import datetime

tday = datetime.date.today()
tdelta = datetime.timedelta(days=10)
print(tday - tdelta)

# here prgm prints the 10 days bfore todays date.

tday = datetime.date.today()
tdelta = datetime.timedelta(days=10)
print(tday + tdelta)

# here prgm prints 10 days after the todays date.

d = datetime.date(2017, 12, 23)
tdelta = datetime.timedelta(days=365)
print(d + tdelta)

# here prgm prints 365 days after the inputed date.

# NOTE: WHEN V ADD OR SUBTRACT A DATE AND TIMEDELTA, WE GET A NEW DATE,
# BT WHILE V ADD OR SUBTRACT TWO DIFFERENT WE GNA GET A TIMEDELTA VALUE AS OUTPUT,
# DATE + DATE = TIMEDELTA
# DATE + TIMEDELTA = DATE

# Example
# So to get the no of days b/1 today and my birthday
import datetime

tday = datetime.date.today()
bday = datetime.date(2019, 7, 4)
print(tday - bday)

# to get only the exact days use days attribute of timedeltas
import datetime

tday = datetime.date.today()
bday = datetime.date(2019, 7, 4)
print((tday - bday).days)

# in above two cases the output will be a timedelta value.

# Sample Program

import datetime

dt1 = datetime.date(2022, 7, 19)
dt2 = datetime.date(2019, 5, 23)
print((dt1 - dt2).days)

################################

# datetime method
# suppose to get the both the date and time v use datetime method of datetime module.
import datetime

dt = datetime.datetime(2017, 9, 23, 7, 30, 50, 300000)
print(dt)
# so here v get the date and also the time(hour, minute, second, microseconds).

# to accesc the date and time separately.

dt = datetime.datetime(2019, 3, 23, 3, 45, 50, 340000)
print(type(dt))
print(dt.date())
print(dt.time())
# use the date and time method of datetime.

# we can further more access the items.
# use datetime attributes like year, motn, day .................
import datetime

dt = datetime.datetime(2019, 3, 23, 3, 45, 50, 340000)
print(type(dt))
print(f"""year: {dt.year}\nmoth: {dt.month}\nday: {dt.day}
        \nhour:{dt.hour}\nminute: {dt.minute}\nseconds: {dt.second}\nmicroseconds: {dt.microsecond}""")

# usin time delta with datetime
# doiung operations b/w datetime and timedelta objects
import datetime

dt = datetime.datetime(2018, 12, 23, 8, 50, 20, 150000)
delta = datetime.timedelta(days=20, seconds=20, microseconds=300000, hours=5, minutes=34)
current = dt - delta
print(type(delta))
print(delta)
print(type(dt))
print(dt)
print(type(current))
print(current)

# DATETIME - TIMEDELTA = DATETIME
# DATETIME + TIMEDELTA = DATETIME
# here, datetime - timedelta gives a datetime object
# always keep the keyword arguments of timedelta in this specific order.
# if changed may not get the required output.


# Example
import datetime

dt = datetime.datetime(2019, 3, 4, 5, 30, 2, 120000)
delta = datetime.timedelta(days=35, seconds=12, microseconds=400000, hours=6, minutes=50)
new_datetime = dt + delta
print(new_datetime)

# Operations on two Datetime objects.

import datetime

dt1 = datetime.datetime(2022, 7, 19, 10, 20, 30, 200000)
dt2 = datetime.datetime(2019, 5, 23, 5, 30, 10, 300000)
print(dt1 - dt2)


import datetime

dt1 = datetime.datetime(2022, 7, 19, 10, 20, 30, 200000)
dt2 = datetime.datetime(2019, 5, 23, 5, 30, 10, 300000)
print((dt1 - dt2).days)

# here we get different b/w these two datetime objects in the form of timedelta.




