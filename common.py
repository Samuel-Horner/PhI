import os
from datetime import datetime

# https://stackoverflow.com/questions/15054434/how-can-i-open-files-in-external-programs-in-python
def startFile(name):
    os.system('start ' + name)

def printTime():
    # Datetime tutorial from https://www.programiz.com/python-programming/datetime/current-time
    now = datetime.now()
    current_time = now.strftime('%I:%M:%S %p')
    current_date = now.strftime('%D')

    print('Time: ' + current_time + ' || Date: ' + current_date)

def printLogo():
    print('PhI-0.0.3-----------')
    print('--------------------')
    print('---Made by A3therium')

def checkDirs():
    cdir = os.getcwd()

    cdirPython = cdir + '//Python'
    # Python Check
    if os.path.exists(cdirPython) == False:
        os.mkdir(cdirPython)

    cdirHTML = cdir + '//HTML'
    if os.path.exists(cdirHTML) == False:
        os.mkdir(cdirHTML)


    