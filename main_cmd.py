from common import *
from projectSystem import *
from directoryManagement import *

checkDepDirs()

printLogo()
printTime()

commandsMisc = ['time : prints the current date & time',
            'ls : lists files in specified directory',
            'mk dir : creates a new directory',
            'rm dir : removes specified directory',
            'exit : exits the program']

commandsProjectSystem = ['mk project : makes a new project using a previously made template',
                    'mk template : makes a new template',
                    'ls template : lists current templates',
                    'rm template : removes templates',
                    'ls project : lists current projects',
                    'rm project : removes projects']

# Loop
while True:
    cmd = input('[]:').casefold().strip()

    # Help
    if cmd == 'help' or cmd == 'h':
        printList(commandsMisc, 'Misc commands: ')
        printList(commandsProjectSystem, '\nProject system commands: ')

    # Time
    elif cmd == 'time':
        printTime()

    # New project
    elif cmd == 'mk project':
        mkProject()

    # New Template
    elif cmd == 'mk template':
        mkTemplate()

    # List Templates
    elif cmd == 'ls template':
        lsTemplate()

    # Remove Template
    elif cmd == 'rm template':
        rmTemplate()

    # List Projects
    elif cmd == 'ls project':
        lsProject()

    # Remove Project
    elif cmd == 'rm project':
        rmProject()

    # Make a folder
    elif cmd == 'mk dir':
        mkDir()

    # Remove a folder
    elif cmd == 'rm dir':
        rmDir()

    # Lists files/folders
    elif cmd == 'ls':
        ls()

    # Quit
    elif cmd == 'exit':
        break

    else:
        print('{0} is not recognised as a command.'.format(cmd))