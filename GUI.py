# import module
import calendar
import datetime
import xlwt
import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import *
import Holidays as Hol
import SemesterStarts as Ss
import InstructionalDays as ID

root = tk.Tk()
root.title("Academic Calendar Generator")
root.geometry("200x200")

clicked = tk.StringVar()


def show():
    myLabel = tk.Label(root, text=clicked.get()).pack()


# creates a dropdown menu to ask the user to input which year they would like to generate a calendar for
def get_year():
    root.geometry("500x100")
    txt = "Please select which year you would like to generate an academic calendar for."
    myLabel = tk.Label(root, text=txt)
    myLabel.pack()

    options = []

    for x in range(0, 100):
        options.append(x + 2000)

    clicked.set(options[20])

    # drop = tk.OptionMenu(root, clicked, *options)
    drop = tk.ttk.Combobox(root, width=5, textvariable=clicked)
    drop['values'] = options
    drop.pack()

    myButton = tk.Button(root, text="Submit", command=root.quit)
    myButton.pack()

    root.mainloop()
    drop.pack_forget()
    myButton.pack_forget()
    myLabel.pack_forget()
    return clicked.get()


# takes a datetime object as a parameter, displays the date and creates a dropdown box to change the day and month.
# then returns the changed date back to the main program.
def input_date(name, day):
    options = []
    month_days = calendar.monthrange(day.year, day.month)[1]
    for x in range(0, month_days):
        options.append(x + 1)

    txt = name + " is currently on: " + day.strftime("%b %d %Y")
    myLabel = tk.Label(root, text=txt)
    myLabel.pack()
    clicked.set(options[day.day - 1])

    drop = tk.ttk.Combobox(root, width=5, textvariable=clicked)
    drop['values'] = options
    drop.pack()

    myButton = tk.Button(root, text="Submit", command=root.quit)
    myButton.pack()

    root.mainloop()
    drop.pack_forget()
    myButton.pack_forget()
    myLabel.pack_forget()
    new_day = datetime.datetime(day.year, day.month, int(clicked.get()))
    return new_day


# prompts user for number of additional instructional days
def extra_ins_days():
    options = []
    for x in range(0, 8):
        options.append(x)

    txt = "Please enter the number of additional instructional days"
    myLabel = tk.Label(root, text=txt)
    myLabel.pack()
    clicked.set(options[0])

    drop = tk.ttk.Combobox(root, width=5, textvariable=clicked)
    drop['values'] = options
    drop.pack()

    myButton = tk.Button(root, text="Submit", command=root.quit)
    myButton.pack()

    root.mainloop()
    drop.pack_forget()
    myButton.pack_forget()
    myLabel.pack_forget()
    return int(clicked.get())


def save(file_name):
    files = [('All Files', '*.*'),
             ('Spreadsheet', '*.xls')]
    file = asksaveasfilename(initialfile=file_name, filetypes=files, defaultextension=files)
    return file
