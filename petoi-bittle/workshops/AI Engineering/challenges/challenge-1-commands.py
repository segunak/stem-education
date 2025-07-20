"""
CHALLENGE 1: Teaching AI New Commands
=====================================

🎯 MISSION: The robot knows 50+ commands, but your AI only knows 3!
Your job is to teach it more by adding commands to the dictionary below.

📖 HOW THIS WORKS:
The AI gets "context" from the ROBOT_COMMANDS dictionary. More commands = smarter AI!
This is called "context engineering" - a key AI skill.

🔧 YOUR TASK:
1. Run this file first - try asking the AI to "jump" (it won't work!)
2. Look at robot-dog-commands.md for available commands
3. Add "jump" and other commands to ROBOT_COMMANDS below
4. Save and run again - now "jump" should work!

💡 HINTS:
- Each command needs: "name": {"command": "code", "description": "what it does"}
- Copy examples from robot-dog-commands.md
- Ask GitHub Copilot: "Add robot commands to this dictionary"
- Add at least 10 commands to see the AI get much smarter!

🚀 WELCOME TO THE AI ROBOT WORKSHOP!
This is Challenge 1 of 4. Complete them in order for the best experience.

RUN THIS FILE DIRECTLY - Click the ▶️ button!
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
