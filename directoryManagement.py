from common import *
import os
import shutil

def mkDir():
    path = input('Enter valid folder name: ')
    checkDir('\\' + path, toPrint = True)

def rmDir():
    cwd = os.getcwd()
    path = input('Enter path to the directory you wish to delete: ') 
    try: 
        shutil.rmtree(cwd + '\\' + path)
        print('Project removed.')
    except: print('Project not found.')

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