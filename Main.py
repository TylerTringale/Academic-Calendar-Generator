# Academic Calendar Generator v 2.0
# Created by Tyler Tringale
# Capstone Project for Salem State University

# import module
import calendar
import datetime
import xlwt
import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import asksaveasfile
import Holidays as Hol
import SemesterStarts as Ss
import InstructionalDays as ID
import GUI as GUI

# print(calendar.weekday(x[1].year, x[1].month, x[1].day))
year = int(GUI.get_year())
holidays = Hol.generate_holidays(year)
academicCalendar = []
wb = xlwt.Workbook()
name = 'Academic Calendar ' + str(year) + '-' + str(year + 1)
ws = wb.add_sheet(name)


# holidays = 0
# print(holidays)

# fd = Ss.fall_semester_first_day(year)
# ld = Ss.first_quarter_end(fd, year, holidays)
# fd = datetime.datetime(year, 9, 6)
# ld = datetime.datetime(year, 12, 23)
# fallSemesterInsDays = ID.calculate_ins_days(fd, ld, holidays)
# fd2 = datetime.datetime(year+1, 1, 17)
# ld2 = datetime.datetime(year+1, 5, 17)
# springSemesterInsDays = ID.calculate_ins_days(fd2, ld2, holidays)
# print(fallSemesterInsDays)
# print(springSemesterInsDays)
# print(fallSemesterInsDays + springSemesterInsDays)

# fall semester
fall_semester_start = Ss.fall_semester_first_day(year)
fall_semester_start = GUI.input_date("Fall Semester Start", fall_semester_start)
# fall_semester_start = datetime.datetime(year, 9, 1)
fall_semester_end = Ss.fall_last_day(year)
fall_exam_start = Ss.full_semester_exam_period_start(fall_semester_end, holidays)
fall_exam_reading_day = Ss.previous_day(fall_exam_start)
thanksgiving_reading_day = Ss.previous_day(holidays[4][1])
fall_classes_end = Ss.full_semester_classes_end(fall_exam_start)
fall_ins_days = ID.calculate_ins_days(fall_semester_start, Ss.previous_day(fall_semester_end), holidays)
fall_semester_end = GUI.input_date("The final date for fall exams, with " + str(fall_ins_days) + " instructional days in fall,", fall_semester_end)
fall_ins_days = ID.calculate_ins_days(fall_semester_start, Ss.previous_day(fall_semester_end), holidays)
# exam make up day does not count as instructional day

fall_semester_add_drop = Ss.full_semester_add_drop(fall_semester_start, holidays)
first_quarter_end = Ss.first_quarter_end(fall_semester_start, holidays)
first_quarter_exam_start = Ss.quarter_exam_period(first_quarter_end, holidays)
first_quarter_class_end = Ss.quarter_classes_end(first_quarter_exam_start, holidays)
second_quarter_start = Ss.second_quarter_begins(first_quarter_end, holidays)
second_quarter_add = Ss.six_week_add_drop(second_quarter_start)
second_quarter_withdraw = Ss.quarter_withdraw(second_quarter_start, holidays)

fall1_start = Ss.fall_1_begins(fall_semester_start)
fall1_add_drop = Ss.six_week_add_drop(fall1_start)
fall1_end = Ss.six_week_session_ends(fall_semester_start)
fall2_start = Ss.fall_2_starts(fall1_end, holidays)
fall2_add_drop = Ss.six_week_add_drop(fall2_start)
fall2_end = Ss.fall_2_ends(fall2_start)

fall1_withdraw = Ss.six_week_withdraw(fall1_start, holidays)
first_quarter_withdraw = Ss.quarter_withdraw(fall_semester_start, holidays)
fall2_withdraw = Ss.six_week_withdraw(fall2_start, holidays)
fall_withdraw = Ss.full_semester_withdraw(fall_semester_start, holidays)

halloween = Hol.halloween(year)
halloween_make_up = Ss.cpsg_make_up_day(halloween)
columbus_day_make_up = Ss.cpsg_make_up_day(holidays[1][1])

# winter semester
winter_session_online_begins = Ss.winter_session_online_start(year, holidays)
winter_session_online_begins = GUI.input_date("Winter Session Online Start", winter_session_online_begins)
winter_session_day_begins = Ss.winter_session_begins(holidays)
winter_session_withdraw = Ss.weeklong_withdraw(winter_session_day_begins, holidays)
winter_session_day_end = Ss.weeklong_end(winter_session_day_begins, holidays)
winter_session_online_withdraw = Ss.six_week_withdraw(winter_session_online_begins, holidays)
winter_session_online_ends = Ss.six_week_session_ends(winter_session_online_begins)

# spring semester
spring_semester_start = Ss.spring_semester_first_day(year, holidays)
spring_semester_start = GUI.input_date("Spring Semester Start", spring_semester_start)
# spring_semester_start = datetime.datetime(year+1, 1, 18)
undergrad_commencement = Ss.undergrad_commencement(year)
friday_commencement = Ss.friday_commencement(undergrad_commencement)
grad_commencement = Ss.graduate_commencement(undergrad_commencement)
last_day_spring_exams = Ss.end_spring_semester_exams(undergrad_commencement)
spring_break_start = Ss.spring_break_start(spring_semester_start, last_day_spring_exams)
spring_break_end = Ss.spring_break_end(spring_break_start)
spring_ins_days = ID.calculate_ins_days(spring_semester_start, spring_break_start, holidays)
spring_ins_days = spring_ins_days + ID.calculate_ins_days(spring_break_end, Ss.previous_day(last_day_spring_exams), holidays)
last_day_spring_exams = GUI.input_date("The final date for spring exams, with " + str(spring_ins_days) + " instructional days in spring,", last_day_spring_exams)
spring_ins_days = ID.calculate_ins_days(spring_semester_start, spring_break_start, holidays) + ID.calculate_ins_days(spring_break_end, Ss.previous_day(last_day_spring_exams), holidays)

spring_semester_add_drop = Ss.full_semester_add_drop(spring_semester_start, holidays)
spring_1_start_date = Ss.spring_1_start(winter_session_online_ends, holidays)
spring_1_add_drop = Ss.six_week_add_drop(spring_1_start_date)
spring_1_withdraw = Ss.six_week_withdraw(spring_1_start_date, holidays)
spring_1_end_date = Ss.six_week_spring_session_ends(spring_1_start_date)
spring_2_start_date = Ss.spring_2_begin(spring_1_end_date, holidays)
spring_2_add_drop = Ss.six_week_add_drop(spring_2_start_date)
spring_2_withdraw = Ss.six_week_withdraw(spring_2_start_date, holidays)
spring_2_end_date = Ss.six_week_session_ends(spring_2_start_date)

spring_semester_withdraw = Ss.full_semester_withdraw(spring_semester_start, holidays)

quarter_3_withdraw = Ss.quarter_withdraw(spring_semester_start, holidays)
quarter_3_final_exam_end = Ss.third_quarter_end(spring_break_start)
quarter_3_final_exam_start = Ss.quarter_exam_period(quarter_3_final_exam_end, holidays)
quarter_3_classes_end = Ss.quarter_classes_end(quarter_3_final_exam_start, holidays)
quarter_4_start_day = Ss.fourth_quarter_start(spring_break_end, holidays)
quarter_4_add_drop = Ss.six_week_add_drop(quarter_4_start_day)
quarter_4_withdraw = Ss.six_week_withdraw(quarter_4_start_day, holidays)

spring_exam_start = Ss.full_semester_exam_period_start(last_day_spring_exams, holidays)
spring_classes_end = Ss.full_semester_classes_end(spring_exam_start)
spring_exam_reading_day = Ss.full_semester_exam_reading_day(spring_classes_end, holidays)
spring_exam_reading_day = Ss.previous_day(spring_exam_start)

# summer session
summer_start = Ss.summer_session_start(undergrad_commencement)
summer_1_add_drop = Ss.six_week_add_drop(summer_start)
summer_1_withdraw = Ss.six_week_withdraw(summer_start, holidays)
summer_1_last_day = Ss.six_week_session_ends(summer_start)

summer_2_start_day = Ss.summer_2_start(year+1)
summer_2_add_drop = Ss.six_week_add_drop(summer_2_start_day)
summer_2_withdraw = Ss.six_week_withdraw(summer_2_start_day, holidays)
summer_2_last_day = Ss.six_week_session_ends(summer_2_start_day)

# academicCalendar.append([])
# Fall Semester
# academicCalendar.append([holidays[0][0] + " Holiday:", holidays[0][1]])
for i in holidays:
    academicCalendar.append(i)

academicCalendar.append(["Make-up Day for Columbus Day Holiday (CPS/G*): ", Ss.cpsg_make_up_day(Hol.columbus_day(year))])
academicCalendar.append(["Make-up Day for Halloween (CPS/G*): ", Ss.cpsg_make_up_day(Hol.halloween(year))])
academicCalendar.append(["Make-up Day for Veterans Day Holiday (CPS/G*): ", Ss.cpsg_make_up_day(Hol.veterans_day(year))])
academicCalendar.append(["Make-up Day for Presidents Day Holiday (CPS/G*): ", Ss.cpsg_make_up_day(Hol.presidents_day(year))])
academicCalendar.append(["Make-up Day for Patriots Day Holiday (CPS/G*): ", Ss.cpsg_make_up_day(Hol.patriots_day(year))])
academicCalendar.append(["Make-up Day for Memorial Day Holiday (CPS/G*): ", Ss.cpsg_make_up_day(Hol.memorial_day(year))])

academicCalendar.append(["Opening the University/Advising Day & Convocation: ", fall_semester_start])
academicCalendar.append(["First Complete Teaching Day (Day &CPS/G), Fall I: ", fall1_start])
academicCalendar.append(["CPS/G Fall 1 Add/Drop period ends: ", fall1_add_drop])
academicCalendar.append(["Fall Semester Add/drop Period ends: ", fall_semester_add_drop])
academicCalendar.append(["CPS/G Fall 1 Last day to withdraw: ", fall1_withdraw])
academicCalendar.append(["Last day to withdraw from 1st Quarter courses: ", first_quarter_withdraw])
academicCalendar.append(["CPS/G Makeup Day for Columbus Day Holiday: ", columbus_day_make_up])
academicCalendar.append(["Fall 1 end: ", fall1_end])
academicCalendar.append(["Fall 2 starts: ", fall2_start])
academicCalendar.append(["CPS/G Fall 2 Add/Drop period ends: ", fall2_add_drop])
academicCalendar.append(["Classes End in Ist Quarter Courses: ", first_quarter_class_end])
academicCalendar.append(["First Quarter exam period starts: ", first_quarter_exam_start])
academicCalendar.append(["First Quarter exam period ends: ", first_quarter_end])
academicCalendar.append(["Second Quarter Starts: ", second_quarter_start])
academicCalendar.append(["Last day to add a 2nd Quarter Course: ", second_quarter_add])
academicCalendar.append(["Halloween -classes end at 4:30 pm: ", halloween])
academicCalendar.append(["Make-Up Day for Halloween: ", halloween_make_up])
academicCalendar.append(["CPS/G Fall II last day to withdraw: ", fall2_withdraw])
academicCalendar.append(["Reading Day (No Day or CPS/G Classes): ", thanksgiving_reading_day])
academicCalendar.append(["Last Day to Withdraw from Full Semester Courses: ", fall_withdraw])
academicCalendar.append(["Last Day to Withdraw from 2nd Quarter Courses: ", second_quarter_withdraw])
academicCalendar.append(["CPS/G Fall II Classes End: ", fall2_end])
academicCalendar.append(["Classes End in Day School: ", fall_classes_end])
academicCalendar.append(["Reading Day (No Day or CPS/G Classes): ", fall_exam_reading_day])
academicCalendar.append(["Fall Examinations Begin: ", fall_exam_start])
academicCalendar.append(["Fall Exam Make Up Day School: ", fall_semester_end])

# Winter Semester
academicCalendar.append(["Winter Session Online begins: ", winter_session_online_begins])
academicCalendar.append(["Winter Session Day begins: ", winter_session_day_begins])
academicCalendar.append(["Last day to withdraw from winter session courses: ", winter_session_withdraw])
academicCalendar.append(["Winter session Day Ends: ", winter_session_day_end])
academicCalendar.append(["Last day to withdraw from Winter Session online courses: ", winter_session_online_withdraw])
academicCalendar.append(["Winter Session Online Ends: ", winter_session_online_ends])

# Spring Semester
academicCalendar.append(["First day Spring Semester: ", spring_semester_start])
academicCalendar.append(["Add/Drop period Ends - Full semester Courses: ", spring_semester_add_drop])
academicCalendar.append(["CPS/G Spring 1 Classes begin: ", spring_1_start_date])
academicCalendar.append(["CPS/G Spring 1 Add/Drop ends: ", spring_1_add_drop])
academicCalendar.append(["Last Day to Withdraw from 3rd Quarter Courses: ", quarter_3_withdraw])
academicCalendar.append(["CPS/G Spring I Last Day to Withdraw: ", spring_1_withdraw])
academicCalendar.append(["Classes End in 3rd Quarter Courses: ", quarter_3_classes_end])
academicCalendar.append(["3rd Quarter Final Examinations Begin: ", quarter_3_final_exam_start])
academicCalendar.append(["3rd Quarter Final Examinations End: ", quarter_3_final_exam_end])

academicCalendar.append(["First day of Spring Recess: ", spring_break_start])
academicCalendar.append(["Last day of Spring Recess: ", spring_break_end])

academicCalendar.append(["Classes Begin 4th Quarter Courses: ", quarter_4_start_day])
academicCalendar.append(["Last Day to Add 4th Quarter Courses: ", quarter_4_add_drop])
academicCalendar.append(["CPS/G Spring I Classes End: ", spring_1_end_date])
academicCalendar.append(["CPS/G Spring II Classes Begin: ", spring_2_start_date])
academicCalendar.append(["CPS/G Spring II Add/Drop Period Ends: ", spring_2_add_drop])
academicCalendar.append(["CPS/G Spring II Last Day to Withdraw: ", spring_2_withdraw])
academicCalendar.append(["Last Day to Withdraw from Full Semester Courses: ", spring_semester_withdraw])
academicCalendar.append(["Last Day to Withdraw from 4th Quarter Courses: ", quarter_4_withdraw])

academicCalendar.append(["Day School Classes End: ", spring_classes_end])
academicCalendar.append(["Reading Day (No Day or CPS/G Classes)", spring_exam_reading_day])
academicCalendar.append(["CPS/G Spring II Classes End: ", spring_2_end_date])
academicCalendar.append(["Final Examinations Day School Courses: ", spring_exam_start])
academicCalendar.append(["Final Exam Make-Up Day School: ", last_day_spring_exams])

academicCalendar.append(["Graduate Commencement: ", grad_commencement])
academicCalendar.append(["Friday Commencement: ", friday_commencement])
academicCalendar.append(["Undergraduate Commencement: ", undergrad_commencement])

# Summer Semester
academicCalendar.append(["Full Summer and Summer Session I Classes Begin: ", summer_start])
academicCalendar.append(["Full Summer and Summer Session IAdd/Drop Period Ends: ", summer_1_add_drop])
academicCalendar.append(["Last Day for Withdrawal SSI: ", summer_1_withdraw])
academicCalendar.append(["Last Day of Classes Summer Session I: ", summer_1_last_day])
academicCalendar.append(["Summer Session II Classes Begin: ", summer_2_start_day])
academicCalendar.append(["Summer Session II Add/Drop Period Ends: ", summer_2_add_drop])
academicCalendar.append(["Last Day for Withdrawal SSII and Full Summer: ", summer_2_withdraw])

academicCalendar.sort(key=lambda x: x[1])


# instructional days
# print("The number of Instructional days in fall is: " + str(fall_ins_days))
# print("The number of instructional days in spring is: " + str(spring_ins_days))
# print("The total number of instructional days in both fall and spring is: " + str(fall_ins_days + spring_ins_days))
# day1 = datetime.datetime(2020, 4, 1)
# day2 = datetime.datetime(2020, 4, 25)
# print(ID.num_meeting_pattern(day1, day2, [0, 4], holidays))

# calculate meeting patterns and write into excel file
# fall
fall_M = ID.num_meeting_pattern(fall_semester_start, thanksgiving_reading_day, [0], holidays)
fall_M = fall_M + ID.num_meeting_pattern(holidays[4][1], fall_exam_reading_day, [0], holidays)

fall_T = ID.num_meeting_pattern(fall_semester_start, thanksgiving_reading_day, [1], holidays)
fall_T = fall_T + ID.num_meeting_pattern(holidays[4][1], fall_exam_reading_day, [1], holidays)

fall_W = ID.num_meeting_pattern(fall_semester_start, thanksgiving_reading_day, [2], holidays)
fall_W = fall_W + ID.num_meeting_pattern(holidays[4][1], fall_exam_reading_day, [2], holidays)

fall_R = ID.num_meeting_pattern(fall_semester_start, thanksgiving_reading_day, [3], holidays)
fall_R = fall_R + ID.num_meeting_pattern(holidays[4][1], fall_exam_reading_day, [3], holidays)

fall_F = ID.num_meeting_pattern(fall_semester_start, thanksgiving_reading_day, [4], holidays)
fall_F = fall_F + ID.num_meeting_pattern(holidays[4][1], fall_exam_reading_day, [4], holidays)

fall_WF = min([fall_W, fall_F])

fall_TR = min([fall_T, fall_R])

# spring
# spring_ins_days = ID.calculate_ins_days(spring_semester_start, spring_break_start, holidays) + ID.calculate_ins_days(spring_break_end, Ss.previous_day(last_day_spring_exams), holidays)
spring_M = ID.num_meeting_pattern(spring_semester_start, spring_break_start, [0], holidays)
spring_M = spring_M + ID.num_meeting_pattern(spring_break_end, spring_exam_reading_day, [0], holidays)

spring_T = ID.num_meeting_pattern(spring_semester_start, spring_break_start, [1], holidays)
spring_T = spring_T + ID.num_meeting_pattern(spring_break_end, spring_exam_reading_day, [1], holidays)

spring_W = ID.num_meeting_pattern(spring_semester_start, spring_break_start, [2], holidays)
spring_W = spring_W + ID.num_meeting_pattern(spring_break_end, spring_exam_reading_day, [2], holidays)

spring_R = ID.num_meeting_pattern(spring_semester_start, spring_break_start, [3], holidays)
spring_R = spring_R + ID.num_meeting_pattern(spring_break_end, spring_exam_reading_day, [3], holidays)

spring_F = ID.num_meeting_pattern(spring_semester_start, spring_break_start, [4], holidays)
spring_F = spring_F + ID.num_meeting_pattern(spring_break_end, spring_exam_reading_day, [4], holidays)

spring_WF = min([spring_W, spring_F])
spring_TR = min([spring_T, spring_R])

ws.write(0, 3, "Meeting Pattern ")
ws.write(0, 4, "Fall number of Pattern ")
ws.write(0, 5, "Spring number of Pattern ")
ws.write(1, 3, "Wed Fri patterns: ")
ws.write(2, 3, "Tue Thr patterns: ")
ws.write(3, 3, "Mondays: ")
ws.write(4, 3, "Tuesdays: ")
ws.write(5, 3, "Wednesdays: ")
ws.write(6, 3, "Thursdays: ")
ws.write(7, 3, "Fridays: ")

ws.write(1, 4, fall_WF)
ws.write(2, 4, fall_TR)
ws.write(3, 4, fall_M)
ws.write(4, 4, fall_T)
ws.write(5, 4, fall_W)
ws.write(6, 4, fall_R)
ws.write(7, 4, fall_F)

ws.write(1, 5, spring_WF)
ws.write(2, 5, spring_TR)
ws.write(3, 5, spring_M)
ws.write(4, 5, spring_T)
ws.write(5, 5, spring_W)
ws.write(6, 5, spring_R)
ws.write(7, 5, spring_F)


# write into excel instructional days
additional_ins_days = GUI.extra_ins_days()
ws.write(0, 0, "The number of Instructional days in fall is: ")
ws.write(0, 1, fall_ins_days)
ws.write(1, 0, "The number of Instructional days in spring is: ")
ws.write(1, 1, spring_ins_days)
ws.write(2, 0, "The number of additional Instructional days is: ")
ws.write(2, 1, additional_ins_days)
ws.write(3, 0, "The total number of instructional days in both fall and spring is: ")
ws.write(3, 1, fall_ins_days + spring_ins_days + additional_ins_days)

style1 = xlwt.easyxf(num_format_str='MMM-D-YY')
style2 = xlwt.easyxf(num_format_str='[$-en-US]mmmm D;@')
start = 4
for i in range(len(academicCalendar)):
    ws.write(start + i, 0, academicCalendar[i][0])
    ws.write(start + i, 1, academicCalendar[i][1], style1)
    ws.write(start + i, 2, academicCalendar[i][1], style2)

name = name + '.xls'
file_location = GUI.save(name)
wb.save(file_location)




# print(holidays[0][0] + " Holiday: " + str(holidays[0][1]))
# print("Fall semester start: " + str(fall_semester_start))
# print("Fall 1 start: " + str(fall1_start))
# print("CPS/G Fall 1 Add/Drop period ends: " + str(fall1_add_drop))
# print("Fall Semester Add/drop Period ends: " + str(fall_semester_add_drop))
# print("CPS/G Fall 1 Last day to withdraw: " + str(fall1_withdraw))
# print("")
# print("Last day to withdraw from 1st Quarter courses: " + str(first_quarter_withdraw))
# print(holidays[1][0] + " Holiday: " + str(holidays[1][1]))
# print("CPS/G Makeup Day for Columbus Day Holiday: " + str(columbus_day_make_up))
# print("Fall 1 end: " + str(fall1_end))
# print("Fall 2 starts: " + str(fall2_start))
# print("CPS/G Fall 2 Add/Drop period ends: " + str(fall2_add_drop))
# print("Classes End in Ist Quarter Courses: ")
# print("First Quarter exam period starts: " + str(first_quarter_exam_start))
# print("First Quarter exam period ends: " + str(first_quarter_end))
# print("Second Quarter Starts: " + str(second_quarter_start))
# print("Last day to add a 2nd Quarter Course: " + str(second_quarter_add))
# print("Halloween -classes end at 4:30 pm: " + str(halloween))
# print("Make-Up Day for Halloween: " + str(halloween_make_up))
# print("")
# print("")
# print("CPS/G Fall II last day to withdraw: " + str(fall2_withdraw))
# print(holidays[2][0] + " Holiday: " + str(holidays[2][1]))
# print(holidays[3][0] + ": " + str(holidays[3][1]))
# print("Reading Day (No Day or CPS/G Classes): " + str(thanksgiving_reading_day))
# print(holidays[4][0] + " Holiday: " + str(holidays[4][1]))
# print(holidays[5][0] + ": " + str(holidays[5][1]))
# print("Last Day to Withdraw from Full Semester Courses: " + str(fall_withdraw))
# print("Last Day to Withdraw from 2nd Quarter Courses: " + str(second_quarter_withdraw))
# print("CPS/G Fall II Classes End: " + str(fall2_end))
# print("")
# print("Classes End in Day School: " + str(fall_classes_end))
# print("Reading Day (No Day or CPS/G Classes): " + str(fall_exam_reading_day))
# print("Fall Examinations Begin: " + str(fall_exam_start))
# print("Fall Exam Make Up Day School: " + str(fall_semester_end))
# print("")


# print("Winter Session Online begins: " + str(winter_session_online_begins))
# print(holidays[7][0] + ": " + str(holidays[7][1]))  # New years Day
# print("Winter Session Day begins: " + str(winter_session_day_begins))
# print("Last day to withdraw from winter session courses: " + str(winter_session_withdraw))
# print("Winter session Day Ends: " + str(winter_session_day_end))
# print("Last day to withdraw from Winter Session online courses: " + str(winter_session_online_withdraw))
# print("Winter Session Online Ends: " + str(winter_session_online_ends))


# print(holidays[8][0] + ": " + str(holidays[8][1]))
# print("First day Spring Semester: " + str(spring_semester_start))
# print("Add/Drop period Ends - Full semester Courses: " + str(spring_semester_add_drop))
# print("CPS/G Spring 1 Classes begin: " + str(spring_1_start_date))
# print("CPS/G Spring 1 Add/Drop ends: " + str(spring_1_add_drop))
# print("Last Day to Withdraw from 3rd Quarter Courses: " + str(quarter_3_withdraw))
# print(holidays[9][0] + ": " + str(holidays[9][1]))
# print("CPS/G Spring I Last Day to Withdraw: " + str(spring_1_withdraw))
# print("Classes End in 3rd Quarter Courses: ")
# print("3rd Quarter Final Examinations Begin: " + str(quarter_3_final_exam_start))
# print("3rd Quarter Final Examinations End: " + str(quarter_3_final_exam_end))
#
# print("First day of Spring Recess: " + str(spring_break_start))
# print("Last day of Spring Recess: " + str(spring_break_end))
#
# print("Classes Begin 4th Quarter Courses: " + str(quarter_4_start_day))
# print("Last Day to Add 4th Quarter Courses: " + str(quarter_4_add_drop))
# print("CPS/G Spring I Classes End: " + str(spring_1_end_date))
# print("CPS/G Spring II Classes Begin: " + str(spring_2_start_date))
# print("CPS/G Spring II Add/Drop Period Ends: " + str(spring_2_add_drop))
# print("CPS/G Spring II Last Day to Withdraw: " + str(spring_2_withdraw))
# print("Last Day to Withdraw from Full Semester Courses: " + str(spring_semester_withdraw))
# print(holidays[10][0] + ": " + str(holidays[10][1]))
# print("Last Day to Withdraw from 4th Quarter Courses: " + str(quarter_4_withdraw))
#
# print("Day School Classes End: " + str(spring_classes_end))
# print("Reading Day (No Day or CPS/G Classes)" + str(spring_exam_reading_day))
# print("CPS/G Spring II Classes End: " + str(spring_2_end_date))
# print("Final Examinations Day School Courses: " + str(spring_exam_start))
# print("Final Exam Make-Up Day School: " + str(last_day_spring_exams))
#
# print("Graduate Commencement: " + str(grad_commencement))
# print("Undergraduate Commencement: " + str(undergrad_commencement))
# print(" ")


# print("Full Summer and Summer Session I Classes Begin: " + str(summer_start))
# print("Full Summer and Summer Session IAdd/Drop Period Ends: " + str(summer_1_add_drop))
# print(holidays[11][0] + ": " + str(holidays[11][1]))
# print("Last Day for Withdrawal SSI: " + str(summer_1_withdraw))
# print("Last Day of Classes Summer Session I: " + str(summer_1_last_day))
# print(holidays[12][0] + ": " + str(holidays[12][1]))
# print("Summer Session II Classes Begin: " + str(summer_2_start_day))
# print("Summer Session II Add/Drop Period Ends: " + str(summer_2_add_drop))
# print("Last Day for Withdrawal SSII and Full Summer: " + str(summer_2_withdraw))
