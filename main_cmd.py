from common import *
from projectCreation import *

checkDepDirs()

printLogo()
printTime()

commands = ['time : prints the current date & time',
            'mk project : makes a new project using a previously made template',
            'mk template : makes a new template',
            'ls template : lists current templates',
            'rm template : removes templates',
            'exit : exits the program']

# Loop
while True:
    cmd = input('[]:').casefold().strip()

    # Help
    if cmd == 'help' or cmd == 'h':

        printList(commands, 'Command list:')

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

    # Quit
    elif cmd == 'exit':
        break

    else:
        print('{0} is not recognised as a command.'.format(cmd))