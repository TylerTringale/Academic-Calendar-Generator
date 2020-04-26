import calendar
import datetime
from InstructionalDays import *


# SUN = 6
# MON = 0
# TUE = 1
# WED = 2
# THR = 3
# FRI = 4
# SAT = 5


# Several holidays are the xth day of the week in a certain month, so this function will calculate that.
def num_day_in_month(year, month, dayOfWeek, numDays):
    i = 1
    x = datetime.datetime(year, month, i)
    d = 0
    while d < numDays:
        i += 1
        x = datetime.datetime(year, month, i)
        if calendar.weekday(x.year, x.month, x.day) == dayOfWeek:
            d += 1
    return x


# Labor Day is first Monday in September, so it starts on the first day of September and iterates until we reach the
# first Monday.
def labor_day(y):
    return num_day_in_month(y, 9, 0, 1)


# Columbus Day is the second Monday in October, so we iterate through October in the given year until we hit Monday
# twice
def columbus_day(y):
    return num_day_in_month(y, 10, 0, 2)


# Halloween takes place on October 31
def halloween(y):
    x = datetime.datetime(y, 10, 31)
    return x


# Veterans Day takes place on  November 11
def veterans_day(y):
    x = datetime.datetime(y, 11, 11)
    return x


# calculates observed days for any given date
# if the date is a weekend, gives that. If a sat, gives friday. If sun, gives monday.
def observed_date(holiday):
    if calendar.weekday(holiday.year, holiday.month, holiday.day) == 5:  # if it falls on a Saturday
        observed = previous_day(holiday)
    elif calendar.weekday(holiday.year, holiday.month, holiday.day) == 6:  # if it falls on a Sunday
        observed = next_day(holiday)
    else:  # if it falls on neither a Saturday or a Sunday
        observed = holiday

    return observed


# Thanksgiving is on the fourth Thursday in November
def thanksgiving_day(y):
    return num_day_in_month(y, 11, 3, 4)


def thanksgiving_day_recess(y):
    turkey_day = thanksgiving_day(y)
    return datetime.datetime(turkey_day.year, turkey_day.month, turkey_day.day + 1)


# Christmas falls on the 25th
def christmas_day(y):
    x = datetime.datetime(y, 12, 25)
    return x


# New Year's Day is always the 1st of January
def new_years_day(y):
    x = datetime.datetime(y, 1, 1)
    return x


# MLK day is on the third monday in January
def martin_luther_king_day(y):
    return num_day_in_month(y, 1, 0, 3)


# Washington's Birthday, aka Presidents Day, falls on the third Monday in February
def presidents_day(y):
    return num_day_in_month(y, 2, 0, 3)


def patriots_day(y):
    return num_day_in_month(y, 4, 0, 3)


# Memorial day is on the last Monday in May
def memorial_day(y):
    x = num_day_in_month(y, 5, 0, 4)  # this returns a date that is the 4th monday in May
    # checks to see if there is less then a week left in the month from the 4th monday, indicating that it would be the
    # last monday of the month.  If it is, it will return the 4th monday.  If there is a week or more left, it will
    # return the 5th monday.  A month can't have more than 5 of a specific day in it, so this will be the last monday.
    if 31 - x.day < 7:
        return x
    else:
        return datetime.datetime(x.year, x.month, x.day + 7)


# Independence day falls on July 4th every year.
def independence_day(y):
    x = datetime.datetime(y, 7, 4)
    return x


def generate_holidays(year):
    # Labor Day, Columbus Day, Halloween, Veterans Day, Thanksgiving Day, Martin Luther King Day,
    # Washington's Birthday, Patriot's Day, Memorial Day, Independence Day, Christmas Day, New years Day
    x = []
    x.append(["Labor Day Holiday", labor_day(year)])
    x.append(["Columbus Day Holiday", columbus_day(year)])
    # x.append(["Halloween", halloween(year)])
    x.append(["Veteran's Day Holiday", veterans_day(year)])
    # x.append(["Veteran's Day Observed", veterans_day_observed(year)])
    if veterans_day(year) != observed_date(veterans_day(year)):
        x.append(["Veteran's Day Observed", observed_date(veterans_day(year))])
    x.append(["Thanksgiving Day", thanksgiving_day(year)])
    x.append(["Thanksgiving Day Recess", thanksgiving_day_recess(year)])
    x.append(["Christmas Day Holiday", christmas_day(year)])
    christmas_obv = observed_date(christmas_day(year))
    if christmas_obv != christmas_day(year):
        x.append(["Christmas Day Observed", christmas_obv])
    # rest of observed holidays are in the next year, so year will be year+1
    x.append(["New Year's Day", new_years_day(year + 1)])
    new_observed = observed_date(new_years_day(year + 1))
    if new_observed != new_years_day(year + 1):
        x.append(["New Years Day Observed", new_observed])
    x.append(["Martin Luther King, Jr. Day", martin_luther_king_day(year + 1)])
    x.append(["President's  Day", presidents_day(year + 1)])
    x.append(["Patriot's  Day", patriots_day(year + 1)])
    x.append(["Memorial  Day", memorial_day(year + 1)])
    x.append(["Independence  Day", independence_day(year + 1)])
    independence_observed = observed_date(independence_day(year + 1))
    if independence_observed != independence_day(year + 1):
        x.append(["Independence Day Observed", independence_observed])
    return x
