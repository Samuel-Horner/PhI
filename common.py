import os
from datetime import datetime

def checkDepDirs():
    checkDir('\\Projects')
    checkDir('\\Templates')

def startFile(name):
    # https://stackoverflow.com/questions/15054434/how-can-i-open-files-in-external-programs-in-python
    os.system('start ' + name)

def createFile(name, openFile = False, printFile = False):
    cwd = os.getcwd()
    path = cwd + name
    if os.path.exists(path) == False:
        with open(path, mode = 'x'): pass
        if openFile == True: startFile(path)
        if printFile == True: print('\'{0}\' has been created.'.format(path))
        return()

    if printFile == True:
        print(path + ' already exists')

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

def checkDir(path, toPrint = False, toReturn = False):
    cdir = os.getcwd()
    folder = cdir + path

    if os.path.exists(folder) == False:
        os.mkdir(folder)
        if toPrint == True: print('Made Directory: '+folder)
        if toReturn == True: return(False)
        else: return()
        
    if toPrint == True:
        print(folder + ' already exists.')

    if toReturn == True:
        return(True)

def printList(array, msg = ''):
    print(msg)
    for i in array:
        print(' - ' + i)