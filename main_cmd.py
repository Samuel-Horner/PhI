from common import *
from mkProject import *

checkDirs()

printLogo()
printTime()

# Loop
while True:
    cmd = input('[]:').casefold().strip()

    # Help
    if cmd == 'help' or cmd == 'h':
        commands = [['time','prints the current date & time'],
                    ['mk python','makes a new python project'],
                    ['mk html','makes a new html project'],
                    ['exit','exits the program']]
        print('Command List: ')
        for i in commands:
            print(' - {0}: {1}'.format(i[0],i[1]))

    # Time
    elif cmd == 'time':
        printTime()

    # New python project
    elif cmd == 'mk python':
        mkProjectPython()

    # New html project
    elif cmd == 'mk html':
        mkProjectHTML()

    # Quit
    elif cmd == 'exit':
        break

    else:
        print('{0} is not recognised as a command.'.format(cmd))