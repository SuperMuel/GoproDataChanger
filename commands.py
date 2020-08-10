
from globals import *
from operator import itemgetter
import sys
import ask_date
import subprocess


def path(args):
    if len(args) == 1:
        print("Args for this command are : VLC, GOPRO")
        return 0
    elif(args[1].upper() == "VLC"):
        if len(args) == 2:
            print(print("Current path of vlc :",getVlc()))
        else:
            try:
                setVlc(" ".join(args[2:]).strip("\"").strip("'"))
                print("Vlc path changed to", getVlc())
            except:
                print("Couldn't change vlc path")



    elif(args[1].upper() == "GOPRO"):
        if len(args) == 2:
            print("Current Gopro folder path :", getPath())
        else:
            try:
                setPath(" ".join(args[2:]).strip("\"").strip("'"))
                print("Gopro folder path changed to :", getPath())
            except:
                print("Coulnd't change path")
    else:
        print("Invalid argument:", args[1])


def deleteTHM():
    for file in os.listdir(getPath()):
        if file.endswith("THM"):
            os.remove(getPath()+"\\"+file)
            print(file,"removed")

def deleteLRV():
    for file in os.listdir(getPath()):
        if file.endswith("LRV"):
            print(file,"removed")
            os.remove(getPath() + "\\" + file)

def clean(args):

    if(len(args) == 1):
        print("Caution : this feature will delete all .THM and .LRV files.")
        print("Are you sure ? ( Y, n )")
        if(input().capitalize() == "Y"):
            deleteLRV()
            deleteTHM()
            print("Files succesfully deleted \n")


    else:
        if(args[1].upper() == "THM"):
            deleteTHM()
            print("Files succesfully deleted \n")
        elif(args[1].upper() == "LRV"):
            deleteLRV()
            print("Files succesfully deleted \n")



def playVideo(name):
    command = "\"" + getVlc() + "\" \"" + getPath() + "\\" + name + "\""
    subprocess.run(command)


def help():
    print("""
     
     HELP :
path :
    vlc : prints the vlc executable path
    gopro : prints the gopro folder path

    vlc/gopro <path> : modifies the selected item

clean : Removes ALL .LRV and .THM files
    lrv : removes only .lrv files
    thm : removes only .thm files

date : enters the date changing mode
    (while in this mode) :
    help : prints this mode's help""")


def date():
    max_year = getMaxYear()
    print("""Will only modify files created before {}.
Change this year ? (Y, n)""".format(max_year))
    entry = input()
    while(len(entry)==0):
        print("""Will only modify files created before {}.
        Change this year ? (Y, n)""".format(max_year))
        entry = input()

    if entry.capitalize()[0] == "Y":
        print("Enter the wanted year :")
        max_year = 0
        while max_year == 0:
            try:
                max_year = int(input().strip())
                setMaxYear(max_year)
            except:
                print("couldn't change year. Please enter a valid number")


    path = getPath()
    initFiles()
    getFiles().sort(key=itemgetter(1))
    print("Showing files < {} : ".format(getMaxYear()))
    for tup in getFiles():
        playVideo(tup[0])
        ask_date.main(tup)
    print("End of old files :)")

def exit():
    sys.exit("Ok, Adieu")


def printFiles():
    for file in os.listdir(getPath()):
        print(file)