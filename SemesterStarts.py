# import module
import calendar
from InstructionalDays import *
import InstructionalDays as IntDays
import datetime

import Holidays as Hol


# Start of September, not including Labor Day.  Will begin the tuesday after labor day.
# Labor day is always a Monday, so by default, this will be the following day, a Tuesday.
def fall_semester_first_day(y):
    x = Hol.labor_day(y)
    day = x.day + 1
    start_day = datetime.datetime(y, 9, day)
    return start_day


# Spring semester starts no earlier than 9 days, starting on Jan 3rd, not including holidays
def spring_semester_first_day(y, holidays):
    year = y + 1
    day = datetime.datetime(year, 1, 3)
    counter = 0
    while counter < 9:  # counts forward 9 business days from jan 3rd, so doesnt count holidays or weekend
        day = next_day(day)
        if is_ins_day(day, holidays):
            counter = counter + 1
    return day


# spring break will attempt to be as close to half way through semester as possible
# first day is first day of semester, last day is last day of semester
def spring_break_start(first_day, last_day):
    meet = True
    while meet:  # iterates through, pushing the first day up and the last day back until they meet in the middle
        first_day = next_day(first_day)
        if first_day == last_day:
            break
        last_day = previous_day(last_day)
        if first_day == last_day:
            break

    # ensures that spring break starts on a Saturday, so it goes back from the meet date to the previous saturday
    # this ensures that the middle day is included in the spring break  dates
    while calendar.weekday(first_day.year, first_day.month, first_day.day) != 5:
        first_day = previous_day(first_day)
    return first_day


# spring break starts on a saturday, ends on a friday
def spring_break_end(first_day):
    day = first_day
    # finds the next friday after spring break starts to end spring break
    while calendar.weekday(day.year, day.month, day.day) != 4:
        day = next_day(day)
    return day


# undergrad commencement is always the third Saturday in May
def undergrad_commencement(y):
    year = y + 1
    day = Hol.num_day_in_month(year, 5, 5, 3)
    return day


# grad commencement is thursday before undergrad commencement, which is always a saturday, thus 2 days prior
def graduate_commencement(undergrad):
    return previous_day(previous_day(undergrad))

1
# friday commencement is the friday before undergrad commencement, one day before
def friday_commencement(undergrad):
    return previous_day(undergrad)


# Commencement has to be a min of the 4th day after final exams
def end_spring_semester_exams(commencement):
    day = commencement
    for x in range(0, 3):
        day = previous_day(day)
    return day


# 1st Quarter Ends on the 35th instructional Day
# September has 30 days, so it will change to the 1st of Oct on that day
def first_quarter_end(first_day, holidays):
    last_day = first_day
    num_days = 0

    while num_days < 36:
        if last_day.day != 30:
            last_day = datetime.datetime(last_day.year, last_day.month, last_day.day + 1)
        else:
            last_day = datetime.datetime(last_day.year, 10, 1)

        num_days = IntDays.calculate_ins_days(first_day, last_day, holidays)

    return last_day


# 2nd quarter begins next instructional day after the first quarter ends
def second_quarter_begins(first_quarter_end_date, holidays):
    date = first_quarter_end_date;
    date = datetime.datetime(date.year, date.month, date.day + 1)
    while IntDays.calculate_ins_days(first_quarter_end_date, date, holidays) < 1:
        date = datetime.datetime(date.year, date.month, date.day + 1)
    return date


# fall 1 begins the first teaching day of the year
# takes in the first day of fall, which is convocation and thus not a teaching day
def fall_1_begins(first_day):
    fall1 = datetime.datetime(first_day.year, first_day.month, first_day.day + 1)
    return fall1


# six week sessions end on the sixth week of the semester, on a saturday
def six_week_session_ends(first_day):
    num_weeks = 0;
    iter_date = first_day;
    while num_weeks < 6:
        iter_date = next_day(iter_date)

        if calendar.weekday(iter_date.year, iter_date.month, iter_date.day) == 5:  # checks if current day  is Sat
            num_weeks = num_weeks + 1

    return iter_date


# skips spring break, so add on a week
def six_week_spring_session_ends(first_day):
    num_weeks = 0;
    iter_date = first_day;
    while num_weeks < 7:
        iter_date = next_day(iter_date)

        if calendar.weekday(iter_date.year, iter_date.month, iter_date.day) == 5:  # checks if current day  is Sat
            num_weeks = num_weeks + 1

    return iter_date


# fall 2 begins on the first business day after the end of Fall II
def fall_2_starts(fall1_end, holidays):
    days = 0
    start = fall1_end;
    while days < 1:
        start = next_day(start)
        days = IntDays.calculate_ins_days(fall1_end, start, holidays)
    # calculate_ins_days does not include the last day, so this will subtract 1 to give us the very next ins day
    start = datetime.datetime(start.year, start.month, start.day - 1)
    return start


# fall 2 ends at the sixth week on a saturday
def fall_2_ends(first_day):
    num_weeks = 0;
    iter_date = first_day;
    while num_weeks < 6:
        iter_date = next_day(iter_date)
        if calendar.weekday(iter_date.year, iter_date.month, iter_date.day) == 5:  # checks if current day  is Sat
            num_weeks = num_weeks + 1

    return iter_date


# full semester add drop period is the first five teaching days of the semester
def full_semester_add_drop(first_day, holidays):
    num_days = 0.
    last_day = first_day
    while num_days < 5:
        last_day = next_day(last_day)
        num_days = IntDays.calculate_ins_days(first_day, last_day, holidays)

    return last_day


# six week sessions have an add/drop period of one business day after the start date of the session
def six_week_add_drop(first_day):
    last_day = next_day(first_day)
    while last_day.weekday() > 5:
        last_day = next_day(last_day)

    return last_day


# 1st/3rd quarter exam periods last 3 days, 2nd/4th quater one goes with regular semester
def quarter_exam_period(last_day, holidays):
    first_day = last_day
    num_days = 0;
    while num_days < 3:
        first_day = previous_day(first_day)
        num_days = IntDays.calculate_ins_days(first_day, last_day, holidays)

    return first_day


# the absolute last day the make up exam can be is the 23rd, which is what this defaults it too.
def fall_last_day(year):
    last_day = datetime.datetime(year, 12, 23)
    return last_day


# full semester exam periods is 7 days total, including the make up day(last day)
def full_semester_exam_period_start(last_day, holidays):
    first_day = last_day
    num_days = 0;
    while num_days < 7:
        first_day = previous_day(first_day)
        num_days = IntDays.calculate_ins_days(first_day, last_day, holidays)

    return first_day


# next weekday from classes end
def full_semester_exam_reading_day(last_day, holidays):
    day = next_day(last_day)
    while not IntDays.is_ins_day(day, holidays):
        day = next_day(day)

    return day


# cpsg make up days are the next friday
def cpsg_make_up_day(holiday):
    while calendar.weekday(holiday.year, holiday.month, holiday.day) != 4:
        holiday = next_day(holiday)

    return holiday


# six week withrdraw periods is the end of 3rd week of classes
def six_week_withdraw(first_day, holidays):
    last_day = first_day
    for x in range(14):
        last_day = next_day(last_day)
    while calendar.weekday(last_day.year, last_day.month, last_day.day) != 4:
        last_day = next_day(last_day)
    if in_holidays(last_day, holidays):  # if it's a holiday, changes it to Monday from Friday
        for x in range(3):
            last_day = next_day(last_day)
    return last_day


# quarter courses have a withdraw period up to the fifth week of classes
def quarter_withdraw(first_day, holidays):
    last_day = first_day
    for x in range(28):
        last_day = next_day(last_day)
    while calendar.weekday(last_day.year, last_day.month, last_day.day) != 4:
        last_day = next_day(last_day)
    if in_holidays(last_day, holidays):  # if it's a holiday, changes it to Monday from Friday
        for x in range(3):
            last_day = next_day(last_day)
    return last_day


# full semester withdraw goes to the end of the 1wth week of classes
def full_semester_withdraw(first_day, holidays):
    last_day = first_day
    for x in range(77):
        last_day = next_day(last_day)
    while calendar.weekday(last_day.year, last_day.month, last_day.day) != 4:
        last_day = next_day(last_day)
    if in_holidays(last_day, holidays):  # if it's a holiday, changes it to Monday from Friday
        for x in range(3):
            last_day = next_day(last_day)

    return last_day


# given the start of the examp period, theres one reading day, so 2 days before the start of exams is the last
# day of classes
def full_semester_classes_end(exam_start):
    last_day = exam_start
    for x in range(2):
        last_day = previous_day(last_day)
    while calendar.weekday(last_day.year, last_day.month, last_day.day) > 4:
        last_day = previous_day(last_day)

    return last_day


# 3rd quarter ends day before spring recess
def third_quarter_end(spring_break_start_day):
    return previous_day(spring_break_start_day)


# first business day after Dec 26
def winter_session_online_start(year, holidays):
    day = datetime.datetime(year, 12, 27)
    while not IntDays.is_ins_day(day, holidays):
        day = next_day(day)

    return day


# first weekday of January after new years day
def winter_session_begins(holidays):
    day = next_day(holidays[7][1])
    while not IntDays.is_ins_day(day, holidays):
        day = next_day(day)

    return day


# third class meeting is the withdrawal date for week long courses
def weeklong_withdraw(start_date, holidays):
    day = start_date
    days = 1
    while days < 3:
        if IntDays.is_ins_day(day, holidays):
            days = days + 1
        day = next_day(day)

    return day


# five days after start
def weeklong_end(start_date, holidays):
    day = start_date
    days = 1
    while days < 5:
        if IntDays.is_ins_day(day, holidays):
            days = days + 1
        day = next_day(day)

    return day


# spring 1 starts first business day after winter session online ends
def spring_1_start(winter_end, holidays):
    day = next_day(winter_end)
    while not IntDays.is_ins_day(day, holidays):
        day = next_day(day)

    return day


# 3rd quarter ends, including exam days, day before spring break, which is always saturday. So day before is Friday.
def third_quarter_end(spring_break_start_day):
    return previous_day(spring_break_start_day)


# 4th quarter starts day after spring break ends, which is always a Friday, so classes start next monday
def fourth_quarter_start(spring_break_end_day, holidays):
    day = next_day(spring_break_end_day)
    while not IntDays.is_ins_day(day, holidays):
        day = next_day(day)

    return day


# spring 2 begins first business day after spring 1 ends
def spring_2_begin(spring_1_end, holidays):
    day = next_day(spring_1_end)
    while not IntDays.is_ins_day(day, holidays):
        day = next_day(day)

    return day


# classes end in a quarter the instructional day before exams start
def quarter_classes_end(class_end, holidays):
    day = previous_day(class_end)
    while not IntDays.is_ins_day(day, holidays):
        day = previous_day(day)

    return day


# summer session starts monday after commencement, which is a Sat, so 2 days after
def summer_session_start(commencement):
    return next_day(next_day(commencement))


# summer 2 starts monday after july 4th, unless 4th is saturday, then 1 week from 4th
def summer_2_start(year):
    independence_day = Hol.independence_day(year)
    day = next_day(independence_day)
    # checks if 4th of july is on a saturday, if so, adds one week to day
    if calendar.weekday(independence_day.year, independence_day.month, independence_day.day) == 6:
        day = datetime.datetime(day.year, day.month, day.day + 7)

    # loops next day after july 4th, or a week from july 4th, until we find the next monday
    while calendar.weekday(day.year, day.month, day.day) != 0:
        day = next_day(day)

    return day  # returns the day, which should be a Monday


# checks if the passed day is a holiday or not
def in_holidays(day, holidays):
    for i in range(len(holidays)):  # iterate through the holidays, checking if the day is one.
        if holidays[i][1] == day:
            return True

    return False
