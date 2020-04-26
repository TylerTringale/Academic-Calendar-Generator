import calendar
import datetime


# calculate from start date to end date
# includes both start date and end date in calculation, if start and end date are instructional days
def calculate_ins_days(start_date, end_date, holidays):
    num_ins_days = 0
    iter_date = start_date
    iter_holiday = 0
    is_holiday = False

    while iter_date != end_date:  # iterates from the start date to the end date
        is_holiday = False
        if calendar.weekday(iter_date.year, iter_date.month, iter_date.day) in [0, 1, 2, 3,
                                                                                4]:  # checks if the current day is a weekday
            for i in range(len(holidays)):  # iterate through the holidays, checking if the day is one.
                if holidays[i][1] == iter_date:
                    is_holiday = True
                    # print(holidays[i][0])
            if not is_holiday:  # checks if the day is not a holiday
                num_ins_days = num_ins_days + 1  # if it's not a Holiday, and it is a weekday, increment

        if iter_date.day == calendar.monthrange(iter_date.year, iter_date.month)[1]:  # checks if current date is end
            # of the month
            if iter_date.month != 12:
                iter_date = datetime.datetime(iter_date.year, iter_date.month + 1, 1)  # proceeds to next month, if
                # current month is not december
            else:
                iter_date = datetime.datetime(iter_date.year + 1, 1, 1)  # if current month is december, makes next
                # day Jan 1st, of next year
        else:
            iter_date = datetime.datetime(iter_date.year, iter_date.month, iter_date.day + 1)

    if is_ins_day(end_date, holidays):
        num_ins_days = num_ins_days + 1
    return num_ins_days


def is_ins_day(day, holidays):
    is_holiday = False
    if calendar.weekday(day.year, day.month, day.day) in [5, 6]:  # checks if the current day is a weekend
        return False
    else:
        for i in range(len(holidays)):  # iterate through the holidays, checking if the day is one.
            if holidays[i][1] == day:
                return False
                # print(holidays[i][0])
        if not is_holiday:  # checks if the day is not a holiday
            return True


# takes a datetime object, and returns a datetime object of the next day compared to the given object
def next_day(day):
    iter_date = day
    if iter_date.day == calendar.monthrange(iter_date.year, iter_date.month)[1]:  # checks if current date is end
        # of the month
        if iter_date.month != 12:
            iter_date = datetime.datetime(iter_date.year, iter_date.month + 1, 1)  # proceeds to next month, if
            # current month is not december
        else:
            iter_date = datetime.datetime(iter_date.year + 1, 1, 1)  # if current month is december, makes next
            # day Jan 1st, of next year
    else:
        iter_date = datetime.datetime(iter_date.year, iter_date.month, iter_date.day + 1)

    return iter_date


# takes a datetime object, and returns a datetime object of the previous day compared to the given object
def previous_day(day):
    iter_date = day
    if iter_date.day == 1:  # checks if current date is the start of the month
        if iter_date.month != 1:
            iter_date = datetime.datetime(iter_date.year, iter_date.month - 1,
                                          calendar.monthrange(iter_date.year, iter_date.month - 1)[1])
            # proceeds to previous month, if current month is not January
        else:
            iter_date = datetime.datetime(iter_date.year - 1, 12, 31)  # if current month is Jan, makes next
            # day Dec 21st, of last year
    else:
        iter_date = datetime.datetime(iter_date.year, iter_date.month, iter_date.day - 1)

    return iter_date


# SUN = 6
# MON = 0
# TUE = 1
# WED = 2
# THR = 3
# FRI = 4
# SAT = 5
# counts the number of meeting patterns within a given start date and end date, including start but not end day
# pattern is a list containing the days of the week you want to count, in integer form
# this function will not take into account reading days, account for those when calling function
# uses num_week_days to count the number of each day within the list pattern
# returns the smallest number, as that will determine the total meeting patterns of that set
def num_meeting_pattern(start_date, end_date, pattern, holidays):
    x = []
    for i in pattern:
        x.append(num_week_days(start_date, end_date, i, holidays))
    return min(x)  # returns least number of pattern


# counts the number of a specific weekday within a range of date
# only counts the days that count as instructional days
def num_week_days(start_date, end_date, week_day, holidays):
    iter_date = start_date
    num_days = 0
    while iter_date != end_date:  # iterates from the start date to the end date
        if calendar.weekday(iter_date.year, iter_date.month, iter_date.day) == week_day:
            if is_ins_day(iter_date, holidays):
                num_days = num_days + 1
        # print("here: " + str(iter_date))
        iter_date = next_day(iter_date)
    return num_days



