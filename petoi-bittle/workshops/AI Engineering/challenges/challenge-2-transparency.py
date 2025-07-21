"""
CHALLENGE 2: Responsible AI Transparency
========================================

🎯 MISSION: Make the AI show what it's actually doing to the robot!

🔧 STEP BY STEP:
1. Click ▶️ (play button, upper right corner) - notice you can't see what commands AI sends
2. Look for the setting below that controls what you can see
3. Figure out how to enable it (hint: it's currently disabled)
4. Click ▶️ again - now you can see everything!
5. Try various commands and watch the transparency

💡 WHY THIS MATTERS: When AI controls robots, cars, or medical devices, 
we need to see what it's doing for safety and trust.

💡 TO EXIT: Type "quit" or "exit" in the chat, then click ▶️ to run again

RUN THIS FILE DIRECTLY - Click the ▶️ button (upper right corner)!
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'lib'))

from robot_controller import RobotAI
from robot_commands import FULL_COMMANDS

# 🎓 CONGRATULATIONS! You've learned context engineering in Challenge 1!
# 🚀 For this challenge and beyond, we're auto-loading ALL robot commands
# 📚 Focus on learning responsible AI concepts, not copying commands
ROBOT_COMMANDS = FULL_COMMANDS

# 🎯 YOUR TASK: Modify the setting below that controls transparency!
SHOW_COMMANDS = False

# 🚀 This runs your AI with transparency settings
if __name__ == "__main__":
    print("🎯 CHALLENGE 2: Responsible AI Transparency")
    print("🎓 Great job completing Challenge 1! You learned context engineering!")
    print("🚀 From now on, we're auto-loading ALL robot commands so you can focus on advanced concepts.\n")
    
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
