"""
CHALLENGE 1: Teaching AI New Commands
=====================================

🎯 MISSION: The AI only knows 3 commands. Teach it more!

STEP BY STEP:
1. Click ▶️ (play button, upper right corner) to run this file
2. Try typing: "stand up", "sit down", "rest" (these work!)
3. Try typing: "jump" (this won't work yet)
4. Type "quit" to exit the program
5. Open robot-dog-commands.md for copy-paste examples
6. Add "jump" command to the dictionary below
7. Click ▶️ again to test your change
8. Keep adding more commands from robot-dog-commands.md

💡 TO EXIT: Type "quit" or "exit" in the chat, then click ▶️ to run again

RUN THIS FILE DIRECTLY - Click the ▶️ button (upper right corner)!
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'lib'))

from robot_controller import RobotAI

# 🎯 YOUR WORKSPACE - Add commands here!
# The AI starts with only these 3 basic commands:

ROBOT_COMMANDS = {
    "stand up": {"command": "kup", "description": "Makes the robot stand up"},
    "sit down": {"command": "ksit", "description": "Makes the robot sit down"},
    "rest": {"command": "krest", "description": "Makes the robot rest"},
    
    # TODO: Add more commands here!
    # Look in robot-dog-commands.md for examples
    # Try adding "jump", "wave", "backflip", and others
    # 
    # Format: "command name": {"command": "robot_code", "description": "what it does"},
    # Just copy and paste from robot-dog-commands.md below this line!
    
}

# 🚀 This runs your AI with the commands you added above
if __name__ == "__main__":
    print("🎯 CHALLENGE 1: Teaching AI New Commands")
    print("Try asking the AI to do things. Notice what works and what doesn't!")
    print("Add more commands above to make the AI smarter.\n")
    
    try:
        robot = RobotAI(commands=ROBOT_COMMANDS)
        print("💡 NEXT: When done, open challenge-2-transparency.py\n")
        robot.run()
    except SystemExit:
        # Don't show "next challenge" message if setup failed
        pass
