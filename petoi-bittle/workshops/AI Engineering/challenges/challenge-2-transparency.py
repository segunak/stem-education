"""
CHALLENGE 2: Responsible AI Transparency
========================================

🎯 MISSION: Make the AI show what commands it's actually sending to the robot.
This is called "AI transparency" - a crucial responsible AI practice.

📖 WHY THIS MATTERS:
When AI controls physical devices (robots, cars, medical equipment), we need to see 
what it's doing! This builds trust and helps debug problems.

🔧 YOUR TASK:
1. Run this file - notice you can't see what commands the AI sends
2. Change SHOW_COMMANDS from False to True below
3. Run again - now you can see every command the AI sends!
4. Try various commands and watch the transparency in action

💡 WHAT YOU'LL LEARN:
- How to make AI systems transparent
- Why this is important for safety
- How to debug AI behavior
- Responsible AI engineering practices

RUN THIS FILE DIRECTLY - Click the ▶️ button!
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'lib'))

from robot_controller import RobotAI

# Pre-filled with commands from Challenge 1 (add more if you want!)
ROBOT_COMMANDS = {
    "stand up": {"command": "kup", "description": "Makes the robot stand up"},
    "sit down": {"command": "ksit", "description": "Makes the robot sit down"},
    "rest": {"command": "krest", "description": "Makes the robot rest"},
    "jump": {"command": "kjmp", "description": "Makes the robot jump"},
    "wave": {"command": "kwh", "description": "Makes the robot wave"},
    "backflip": {"command": "kbf", "description": "Makes the robot do a backflip"},
    "walk forward": {"command": "kwkF", "description": "Makes the robot walk forward"},
    "walk backward": {"command": "kbk", "description": "Makes the robot walk backward"},
}

# 🎯 YOUR TASK: Change this to True to enable transparency!
SHOW_COMMANDS = False  # TODO: Change this to True

# 🚀 This runs your AI with transparency settings
if __name__ == "__main__":
    print("🎯 CHALLENGE 2: Responsible AI Transparency")
    
    if SHOW_COMMANDS:
        print("✅ Transparency ENABLED - you'll see what the AI sends to the robot!")
    else:
        print("⚠️  Transparency DISABLED - change SHOW_COMMANDS to True above")
    
    print("Try asking the robot to do various things and watch what happens.\n")
    
    try:
        robot = RobotAI(
            commands=ROBOT_COMMANDS,
            show_commands=SHOW_COMMANDS
        )
        print("💡 NEXT: When done, open challenge-3-sequences.py\n")
        robot.run()
    except SystemExit:
        # Don't show "next challenge" message if setup failed
        pass
