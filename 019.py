"""
You are given the following information, but you may prefer to do some research for yourself.
- 1 Jan 1900 was a Monday.
- Thirty days has September, April, June and November.
- All the rest have thirty-one, Saving February alone, Which has twenty-eight, rain or shine. And on leap years, twenty-nine.
- A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

def is_leap_year(year):
    if year % 4 != 0:
        return False
    if year % 100 == 0 and year % 400 != 0:
        return False
    return True

month_lengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

year = 1901
month = 0
day = 2
sundays_on_first = 0

while year < 2001:
    if day == 0:
        sundays_on_first = sundays_on_first + 1

    if is_leap_year(year) and month == 1:
        day_increment = 29
    else:
        day_increment = month_lengths[month]

    if month == 11:
        year = year + 1

    month = (month + 1) % 12
    day = (day + day_increment) % 7

print(sundays_on_first)

