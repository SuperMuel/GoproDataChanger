
PATH = ""
files = []
vlc = "C:\\Program Files\\VideoLAN\\VLC\\vlc.exe"

max_year = 2020

temp = ""

import os
import datetime

def getMaxYear():
    global max_year
    return max_year

def setMaxYear(year):
    global max_year, temp
    with open(temp+"\\year","w+") as file:
        file.write(str(year))
    max_year = year

def initFiles():
    for file in os.listdir(getPath()):
        if file.endswith("MP4"):
            path = getPath() + "\\" + file
            time = os.path.getctime(path)
            date = datetime.datetime.fromtimestamp(time)
            if date.year < getMaxYear():
                files.append((file,date))


def initGlobals():
    global temp
    temp = os.getenv("temp") +"\\GoproDateChanger"
    if not os.path.isdir(temp):
        os.mkdir(temp)

    global PATH, vlc, max_year

    try:
        with open(temp+"\\year","r") as file:
            max_year= int(file.readline().strip("\n"))
    except:
        max_year = 2020

    try :
        with open(temp+"\\vlc","r") as file:
            vlc = file.readline().strip("\n")
    except:
        vlc = "C:\\Program Files\\VideoLAN\\VLC\\vlc.exe"

    try :
        with open(temp+"\\path","r") as file:
            PATH = file.readline().strip("\n")
    except:
        PATH = "D:\\DCIM\\100GOPRO"



def getPath():
    global PATH
    return PATH

def setPath(path):
    global PATH, temp
    with open(temp+"\\path","w+") as file:
        file.write(str(path))
    PATH = path

def getCommands():
    global commands
    return commands

def setFiles(file_list):
    global files
    files = file_list

def getFiles():
    global files
    return files

def getVlc():
    global vlc
    return vlc

def setVlc(path):
    global vlc, temp
    print(path)
    with open(temp+"\\vlc","w+") as file:
        file.write(str(path))
    vlc = path