#/usr/bin/env python

import os
import time

# the log file of the channel you want notifications for:
logfile = "/home/oscar/irclogs/freenode/#channel.log"
# messages from these screennames will be ignored (add as many as you like):
screennames = ['screenname', 'name_', 'screenie']

curtime = ""
logchanged = ""

def reset():
    global logchanged
    global curtime
    logchanged = os.stat(logfile).st_mtime
    curtime = os.stat(logfile).st_mtime

def displaynotification(lastline):
    execstring = "notify-send '" + lastline + "'"
    os.system(execstring)

def readlastline():
    f = open(logfile, 'rU')
    lastline = f.readlines()[-1]
    lastline = lastline[5:]
    display = True
    for i in screennames:
        sn = "< " + i + ">"
        if sn in lastline:
            display = False
    if display == True:
        displaynotification(lastline)

def checklog():
    global logchanged
    global curtime
    while curtime == logchanged:
        logchanged = os.stat(logfile).st_mtime
        time.sleep(0.5)
    reset()
    readlastline() 


def launch():
    reset()
    print "irssi-notify is running"
    while 1 == 1:
        checklog()
        time.sleep(0.01)

if __name__ == '__main__':
    launch()
