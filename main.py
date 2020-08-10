import commands

from globals import *


def init():
    print("""This program helps you correct wrong dates of videos files.

Videos folder : {path} 
Vlc path :      {vlc} 


Type "help" for the list of command""".format(path = getPath(), vlc= getVlc()))


def ask():
    args = input().split(" ")
    command = args[0].upper()
    if command == "PATH":
        commands.path(args)
    elif command == "CLEAN":
        commands.clean(args)
    elif command == "DATE":
        commands.date()
    elif command == "EXIT":
        commands.exit()
    elif command == "HELP":
        commands.help()
    elif command == "PRINT":
        commands.printFiles()
    else:
        print("Valid commands are PATH, CLEAN, DATE, HELP, EXIT")



def main():
    init()
    while(True):
        ask()


if __name__ == '__main__':
    initGlobals()
    main()
