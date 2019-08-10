# --strftime

# Formating the datetime object to a new string using strftime method.
# to format v use a directive for month, day ,year.
# ie. %B -- month,
#     %d -- two digit date
#      %Y -- year

# NOTE:
# the output of strftime() method IS A  string object not a datetime objebt

import datetime

date1 = datetime.date.today()
date2 = date1.strftime('%B %d, %Y')
print(date2)

# printing the formatted string for a given date.

import datetime

date1 = datetime.date(2013, 4, 1)
format_dt = date1.strftime('%B %d, %Y')
print(format_dt)
print(type(format_dt))

# --strptime()
# Sometime we want to do the viceversa
# ie convert this formated string to a datetime object.
# for that purpose v use, strptime() method of datetime


import datetime

fmt_date = 'April 01, 2013'
date = datetime.datetime.strptime(fmt_date, '%B %d, %Y')
print(type(date))
print(date.date())

# Exercise -- strftime and strptime
# Converting to a string

import datetime


def convert_me(y, m, d):
    date = datetime.date(y, m, d)
    return date.strftime('%B %d, %Y')


print(convert_me(2017, 4, 12))

#
import datetime


def convert_me(fmt_date):
    return datetime.datetime.strptime(fmt_date, '%B %d, %Y').date()


print(convert_me('April 12, 2017'))


# Using Classes

class Date:
    def convert_me(self, y, m, d):
        date = datetime.date(y, m, d)
        return date.strftime('%B %d, %Y')

    def convert_meee(self, fmt_date):
        new_dt = datetime.datetime.strptime(fmt_date, '%B %d, %Y').date()
        print(new_dt)


d1 = Date()
