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
    templateList = os.listdir(cwd + '\\Templates')
    printList(templateList, 'Choose template:')

    template = input('[]:')
    if not template in templateList:
        print('{0} is not a valid template.'.format(template))
        return()

    projectName = input('Project name: ')

    try: 
        os.listdir(cwd + '\\Projects\\' + projectName)
        print('\'{0}\' already exists'.format(projectName))
        return()
    except: print('Creating project {0}'.format(projectName))

    # Copies Directory
    srcDir = cwd + '\\Templates\\' + template
    dstDir =  cwd + '\\Projects\\' + projectName
    shutil.copytree(srcDir, dstDir)

    os.startfile(dstDir)

# List Templates
def lsTemplate():
    cwd = os.getcwd()
    templateList = os.listdir(cwd + '\\Templates')
    printList(templateList, 'Templates:')

# Remove templates
def rmTemplate():
    cwd = os.getcwd()
    templateList = os.listdir(cwd + '\\Templates')
    printList(templateList, 'Templates:')
    template = input('Choose a template to delete: ')
    if template == '': return
    try: 
        shutil.rmtree(cwd + '\\Templates\\' + template)
        print('Template removed.')
    except: print('Template not found.')

# List Projects
def lsProject():
    cwd = os.getcwd()
    projectList = os.listdir(cwd + '\\Projects')
    printList(projectList, 'Projects:')

# Remove Projects
def rmProject():
    cwd = os.getcwd()
    projectList = os.listdir(cwd + '\\Projects')
    printList(projectList, 'Projects:')
    project = input('Choose a project to delete : ')
    if project == '': return
    try: 
        shutil.rmtree(cwd + '\\Projects\\' + project)
        print('Project removed.')
    except: print('Project not found.')
