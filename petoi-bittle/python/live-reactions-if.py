import time
from PetoiRobot import *

autoConnect()

try:
    print("""Welcome! You may use this terminal to control the Petoi "Bittle X" Robot Dog.
You can enter a single command, or a series of commands separated by commas.
    """)
    
    while True:
        user_input = input("Enter command(s) (or 'exit' to quit): ").strip().lower()
        
        if user_input == 'exit':
            print("Exiting...")
            break

        commands = user_input.split(',')

        for command in commands:
            command = command.strip()
            
            # Using if-else statements to match and execute commands
            if command == 'sit':
                sendSkillStr('ksit', 1)
            elif command == 'stand':
                sendSkillStr('kup', 1)
            elif command == 'bottom up':
                sendSkillStr('kbuttUp', 1)
            elif command == 'stretch':
                sendSkillStr('kstr', 1)
            elif command == 'rest':
                sendSkillStr('krest', 1)
            elif command == 'zero':
                sendSkillStr('kzero', 1)
            elif command == 'boxing':
                sendSkillStr('kbx', 1)
            elif command == 'cheer':
                sendSkillStr('kchr', 1)
            elif command == 'check around':
                sendSkillStr('kck', 1)
            elif command == 'dig':
                sendSkillStr('kdg', 1)
            elif command == 'handstand':
                sendSkillStr('khds', 1)
            elif command == 'hug':
                sendSkillStr('khg', 1)
            elif command == 'hi':
                sendSkillStr('khi', 1)
            elif command == 'hands up':
                sendSkillStr('khu', 1)
            elif command == 'jump':
                sendSkillStr('kjmp', 1)
            elif command == 'kick':
                sendSkillStr('kkc', 1)
            elif command == 'nod':
                sendSkillStr('knd', 1)
            elif command == 'play dead':
                sendSkillStr('kpd', 1)
            elif command == 'pee':
                sendSkillStr('kpee', 1)
            elif command == 'push up':
                sendSkillStr('kpu', 1)
            elif command == 'scratch':
                sendSkillStr('kscrh', 1)
            elif command == 'sniff':
                sendSkillStr('ksnf', 1)
            elif command == 'stepping':
                sendSkillStr('kvtF', 1)
            elif command == 'crawl forward':
                sendSkillStr('kcrF', 1)
            elif command == 'crawl left':
                sendSkillStr('kcrL', 1)
            elif command == 'crawl right':
                sendSkillStr('kcrR', 1)
            elif command == 'push forward':
                sendSkillStr('kphF', 1)
            elif command == 'push left':
                sendSkillStr('kphL', 1)
            elif command == 'push right':
                sendSkillStr('kphR', 1)
            elif command == 'walk forward':
                sendSkillStr('kwkF', 1)
            elif command == 'walk left':
                sendSkillStr('kwkL', 1)
            elif command == 'walk right':
                sendSkillStr('kwkR', 1)
            elif command == 'back':
                sendSkillStr('kbk', 1)
            elif command == 'back left':
                sendSkillStr('kbkL', 1)
            elif command == 'back right':
                sendSkillStr('kbkR', 1)
            elif command == 'trot forward':
                sendSkillStr('ktrF', 1)
            elif command == 'trot left':
                sendSkillStr('ktrL', 1)
            elif command == 'trot right':
                sendSkillStr('ktrR', 1)
            elif command == 'back flip':
                sendSkillStr('kbf', 1)
            elif command == 'front flip':
                sendSkillStr('kff', 1)
            else:
                print(f"Error: Unknown command: {command}")

except KeyboardInterrupt:
    print("\nKeyboard interrupt received. Exiting...")
finally:
    closePort()
    print("Program terminated.")
