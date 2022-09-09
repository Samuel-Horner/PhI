from common import *
import os

def mkDir():
    dirName = input('Enter valid folder name: ')
    checkDir('\\' + dirName, toPrint = True)

def ls():
    cwd = os.getcwd()
    path = input('Enter path (press enter for current dir): ')
    if path != '': 
        try: dirArr = os.listdir(path) 
        except: 
            print('Invalid directory. (include C:\ etc)')
            return
    else: dirArr = os.listdir(cwd)
    printList(dirArr, ':::')