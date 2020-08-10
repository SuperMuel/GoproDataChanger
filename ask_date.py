import sys

from win32_setctime import setctime

from globals import *

# This module will wait for user to type a command : date, day, month, year, set, + int
# The user can choose a date exact date, change either the day, month, or day,
# or simply add or substract one or many days by + 1 or + -1 for example

# for each file, the user will then apply the date to the file by the command SET


c_day = 0
c_month = 0
c_year = 0


def init():
    global c_month, c_day, c_year
    if c_day == 0 and c_month == 0 and c_year == 0:
        date = datetime.date.today()
        c_day = date.day
        c_month = date.month
        c_year = date.year


def format_date(date_tup):
    months = ["0", "Janvier", "Fevrier", "Mars", "Avril", "Mai", "Juin", "Juillet", "Aout", "Septembre", "Octobre",
              "Novembre", "Decembre"]
    formated_date = str(date_tup[0]) + " " + months[date_tup[1]] + " " + str(date_tup[2])
    return formated_date


def get_c_date():
    init()
    global c_month, c_day, c_year
    return (c_day, c_month, c_year)

def set_file_modification_time(filename, mtime):
    """
    Set the modification time of a given filename to the given mtime.
    mtime must be a datetime object.
    """
    stat = os.stat(filename)
    atime = stat.st_atime
    os.utime(filename, times=(atime, mtime.timestamp()))


def ask(fname, fdate):
    global c_month, c_day, c_year
    print("File : ", fname, " Creation Date :", format_date(fdate))
    print("Current date :", format_date(get_c_date()))

    entry = input().split(" ")
    if entry[0].upper() == "MONTH":
        try:
            c_month = int(entry[1])
            print("Current date :", format_date(get_c_date()))
        except:
            print("Please provide a valid integer arg for month value")
    elif (entry[0].upper() == "DAY"):
        try:
            c_day = int(entry[1])
            print("Current date :", format_date(get_c_date()))
        except:
            print("Please provide a valid integer arg for day value")
    elif (entry[0].upper() == "YEAR"):
        try:
            c_year = int(entry[1])
            print("Current date :", format_date(get_c_date()))
        except:
            print("Please provide a valid integer arg for year value")
    elif (entry[0].upper() == "DATE"):
        try:
            c_day = int(entry[1])
            c_month = int(entry[2])
            c_year = int(entry[3])
        except:
            print("Please provide a valid integer for each date value")
    elif (entry[0].upper() == "+"):
        try:
            c_day += int(entry[1])
        except:
            print("The syntax of this command is : + <number>")
    elif (entry[0].upper() == "-"):
        try:
            c_day -= int(entry[1])
        except:
            print("The syntax of this command is : - <number>")


    elif (entry[0].upper() == "SET"):
        print("Date successfuly set to file {} \n\n".format(fname))
        date_t = datetime.datetime(c_year, c_month, c_day)
        fullPath = getPath() + "\\" + fname
        set_file_modification_time(fullPath, date_t)
        setctime(fullPath, date_t.timestamp())
        return 1

    elif (entry[0].upper() == "REMOVE"):
        try:
            os.remove(getPath() + "\\" + fname)
        except:
            print("Coulnd't remove file :/")
        finally:
            print("File succesfully removed\n\n")
            return 1


    elif (entry[0].upper() == "EXIT"):
        sys.exit()

    elif (entry[0].upper() == "NOTHING"):
        return 1

    elif (entry[0].upper() == "HELP"):
        print("""
        Date changing mode :
    In this mode, a date is kept in memory and printed each time as "current date"
    
        SET : Applies the current date to the current file
        REMOVE : Removes the current file
        NOTHING : Does nothing to the current file
    
    Commands to modify the current date :
        date DD MM YYYY : changes the current date.
            Example : "date 1 8 2020" will set the date to the first August of 2020
        
        day DD : only changes the current date's day
        month MM : same for the month 
        year YYYY : same for the year
        
        + <number> : adds a certain number of days to the current date
        - <number> : decreases the current date of a certain number of days
        
        
    All commands can be typed lowercase or uppercase
        
""")


    else:
        print("Valid commands are date, day, month, year, set, +, -")


def main(tup):  # tup = (char * name, datetime)
    fname = tup[0]
    fdate = (tup[1].day, tup[1].month, tup[1].year)
    while (ask(fname, fdate) != 1):
        continue
