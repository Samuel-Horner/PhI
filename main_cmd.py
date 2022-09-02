from common import *
from projectCreation import *

checkDepDirs()

printLogo()
printTime()

# Loop
while True:
    cmd = input('[]:').casefold().strip()

    # Help
    if cmd == 'help' or cmd == 'h':
        commands = [['time','prints the current date & time'],
                    ['mk project','makes a new project using a previously made template'],
                    ['mk template','makes a new template'],
                    ['exit','exits the program']]
        print('Command List: ')
        for i in commands:
            print(' - {0}: {1}'.format(i[0],i[1]))

    # Time
    elif cmd == 'time':
        printTime()

    # New project
    elif cmd == 'mk project':
        mkProject()

    # New Template
    elif cmd == 'mk template':
        mkTemplate()

    # Quit
    elif cmd == 'exit':
        break

    else:
        print('{0} is not recognised as a command.'.format(cmd))