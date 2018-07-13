"""
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""
sundays = 0
year = 1900
day = 1
month = 0
i = 0
day_max = 31
year_max = 365
days = []
for x in range(40000):
    tmp = []
    if i == 7:
        i == 0
    if i == 0:
        tmp.append('Mo')
    elif i == 1:
        tmp.append('Tu')
    elif i == 2:
        tmp.append('We')
    elif i == 3:
        tmp.append('Th')
    elif i == 4:
        tmp.append('Fr')
    elif i == 5:
        tmp.append('Sa')
    elif i == 6:
        tmp.append('Su')
    if month == 0:
        tmp.append('Jan')
    elif month == 1:
        tmp.append('Feb')
    elif month == 2:
        tmp.append('Mar')
    elif month == 3:
        tmp.append('Apr')
    elif month == 4:
        tmp.append('May')
    elif month == 5:
        tmp.append('Jun')
    elif month == 6:
        tmp.append('Jul')
    elif month == 7:
        tmp.append('Aug')
    elif month == 8:
        tmp.append('Sep')
    elif month == 9:
        tmp.append('Oct')
    elif month == 10:
        tmp.append('Nov')
    elif month == 11:
        tmp.append('Dec')
    tmp.append(day)
    tmp.append(year)
    days.append(tmp)
    i += 1
    day += 1
    if month == 0 or month == 2 or month == 4 or month == 6 or month == 7 or month == 9 or month == 11:
        day_max = 31
    elif month == 3 or month == 5 or month == 8 or month == 10:
        day_max = 30
    else:
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            day_max = 29
            year_max = 366
        else:
            day_max = 28
            year_max = 365
    if day > day_max:
        day = 1
        month += 1
    if month > 11:
        month = 0
        year += 1
    if i > 6:
        i = 0

print(days)

for d in days:
    if d[0] == 'Su' and d[2] == 1 and 1901 <= d[3] <= 2000:
        sundays += 1

print(sundays)