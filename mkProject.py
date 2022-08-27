import os
from common import *

def mkProjectPython():
    name = input('Project Name: ')

    # Tutorial from https://linuxize.com/post/python-get-change-current-working-directory/
    cwd = os.getcwd()
    dirName = cwd + '\\Python\\' + name
    # Dir check
    if os.path.exists(dirName) == False:
        os.mkdir(dirName)
        print('Created directory: ' + dirName)

        # Module Selector
        modules = input('Choose Modules: \n-Ursina (ur)\n-None ()\n').casefold()

        # Ursina
        if modules == 'ur' or modules == 'ursina':
            # Ursina Template
            with open(dirName + '\\main.py', 'w') as file:
                file.write('# Imports\nfrom ursina import *\n\napp = Ursina()\n\n# Globals\n\n# Environment\nwindow.borderless = False\n\n# Functions\ndef update():\n  next\n\napp.run()')

            startFile(dirName + '\\main.py')

        # None
        else: 
            # Empty File
            with open(dirName + '\\main.py','w') as file:
                file.write('# Imports\n\n# Functions\n\n# Driver')

            startFile(dirName + '\\main.py')

    else:
        print('{0} already exists.'.format(name))

def mkProjectHTML():
    name = input('Project Name: ')

    # Tutorial from https://linuxize.com/post/python-get-change-current-working-directory/
    cwd = os.getcwd()
    dirName = cwd + '\\HTML\\' + name
    # Dir check
    if os.path.exists(dirName) == False:
        os.mkdir(dirName)
        print('Created directory: ' + dirName)

        # Index
        with open(dirName + '\\index.html', 'w') as file:
            file.write('<!DOCTYPE html>\n<html lang="en">\n<head>\n    <meta charset="UTF-8">\n    <meta http-equiv="X-UA-Compatible" content="IE=edge">\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n    <link rel="stylesheet" href="style.css">\n    <title>Document</title>\n</head>\n<body>\n\n</body>\n</html>')

        # Style
        with open(dirName + '\\style.css', 'w') as file:
            file.write('body {\n    font-size: 24px;\n    font-family: Arial, Helvetica, sans-serif;\n}')

        startFile(dirName + '\\index.html')

    else:
        print('{0} already exists.'.format(name))