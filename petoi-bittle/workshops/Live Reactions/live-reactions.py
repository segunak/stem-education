import time
from PetoiRobot import *

def execute_command(command, delay=1):
    skill_map = {
        'sit': 'ksit',
        'stand': 'kup',
        'bottom up': 'kbuttUp',
        'stretch': 'kstr',
        'rest': 'krest',
        'zero': 'kzero',
        'boxing': 'kbx',
        'cheer': 'kchr',
        'check around': 'kck',
        'dig': 'kdg',
        'handstand': 'khds',
        'hug': 'khg',
        'hi': 'khi',
        'hands up': 'khu',
        'jump': 'kjmp',
        'kick': 'kkc',
        'nod': 'knd',
        'play dead': 'kpd',
        'pee': 'kpee',
        'push up': 'kpu',
        'scratch': 'kscrh',
        'sniff': 'ksnf',
        'stepping': 'kvtF',
        'crawl forward': 'kcrF',
        'crawl left': 'kcrL',
        'crawl right': 'kcrR',
        'push forward': 'kphF',
        'push left': 'kphL',
        'push right': 'kphR',
        'walk forward': 'kwkF',
        'walk left': 'kwkL',
        'walk right': 'kwkR',
        'back': 'kbk',
        'back left': 'kbkL',
        'back right': 'kbkR',
        'trot forward': 'ktrF',
        'trot left': 'ktrL',
        'trot right': 'ktrR',
        'back flip': 'kbf',
        'front flip': 'kff'
    }

    skill_command = skill_map.get(command)

    if skill_command:
        sendSkillStr(skill_command, delay)
    else:
        print(f"Error: Unknown command: {command}")

autoConnect()

try:
    print("""Welcome! You may use this terminal to control the Petoi "Bittle X" Robot Dog.
You can enter a single command, or a series of commands separated by commas.
    """)
    while True:
        user_input = input("Enter command(s) (or 'exit' to quit).: ").strip().lower()

        if user_input == 'exit':
            print("Exiting...")
            break
        
        commands = user_input.split(',')

        for command in commands:
            command = command.strip()
            execute_command(command)
except KeyboardInterrupt:
    print("\nKeyboard interrupt received. Exiting...")
finally:
    closePort()
    print("Program terminated.")
