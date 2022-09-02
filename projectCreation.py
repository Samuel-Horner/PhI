import os
import shutil
from tempfile import tempdir
from common import *

# New Template
def mkTemplate():
    name = input('Template Name: ')
    temPath = '\\Templates\\' + name
    if checkDir(temPath, True, True) == True:
        return()

    files = input('Enter files within template (seperate each with a comma, include file endings (eg .py), and place \\ after folder names): \n')
    fileArray = files.split(',')
    print(fileArray)
    # File/ Folder Creation
    for i in fileArray:
        i = i.strip()
        # MK folder
        if i[-1] == '\\': checkDir(temPath + '\\' + i)
        # MK file
        else:      
            createFile(temPath + '\\' + i, True, True)

# New Project
def mkProject():
    cwd = os.getcwd()
    projectList = os.listdir(cwd + '\\Templates')
    print('Choose Template:')
    for i in projectList:
        print(' - '+ i)

    template = input('[]:')
    if not template in projectList:
        print('{0} is not a valid template.'.format(template))
        return()

    projectName = input('Project name: ')

    # Copies Directory
    srcDir = cwd + '\\Templates\\' + template
    dstDir =  cwd + '\\Projects\\' + projectName
    shutil.copytree(srcDir, dstDir)

    os.startfile(dstDir)


