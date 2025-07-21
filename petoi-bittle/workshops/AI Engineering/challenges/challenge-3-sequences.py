"""
CHALLENGE 3: Command Sequences
==============================

🎯 MISSION: Teach the AI to do multiple actions in a row!

🔧 STEP BY STEP:
1. Click ▶️ (play button, upper right corner) - try asking for "dance" (won't work yet)
2. Look for the setting that controls sequences  
3. Figure out how to enable it (hint: it's currently disabled), do so, then stop the program
4. Click ▶️ again - now try "dance" or "morning routine"!
5. Add your own sequences by copying the examples in MY_CUSTOM_SEQUENCES
6. Check robot-dog-commands.md for sequence examples and robot codes

💡 SEQUENCES: Chain multiple robot codes together for complex behaviors
💡 EASY FORMAT: Just copy the examples in MY_CUSTOM_SEQUENCES and modify!

💡 TO EXIT: Type "quit" or "exit" in the chat, then click ▶️ to run again

RUN THIS FILE DIRECTLY - Click the ▶️ button (upper right corner)!
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'lib'))

from robot_controller import RobotAI
from robot_commands import FULL_COMMANDS, SEQUENCE_COMMANDS

# 🎓 AUTO-LOADED: All robot commands from previous challenges!
# 🎯 YOUR FOCUS: Learn to create command sequences for complex behaviors

# Start with all the single commands you've learned
ROBOT_COMMANDS = FULL_COMMANDS.copy()

# 🚀 Pre-made sequences are already added! Try "dance" or "morning routine"
ROBOT_COMMANDS.update(SEQUENCE_COMMANDS)

# 🎯 ADD YOUR OWN SEQUENCES HERE! 
# Just copy and paste new sequences into this list:
MY_CUSTOM_SEQUENCES = [
    # Copy these examples and modify them, or add new ones:
    
    # {"name": "my_dance", "sequence": ["kup", "kjmp", "kwh", "krest"], "description": "Stand, jump, wave, rest"},
    # {"name": "robot_workout", "sequence": ["kstr", "kpu", "kpu", "kjmp"], "description": "Stretch, pushup, pushup, jump"},
    # {"name": "greeting_routine", "sequence": ["kup", "khi", "kwh", "ksit"], "description": "Stand, greet, wave, sit"},
    
    # ADD YOUR SEQUENCES BELOW (uncomment by removing # and modify):
    # {"name": "my_awesome_trick", "sequence": ["kup", "kbf", "kwh"], "description": "Stand, backflip, wave"},
    
]

# 🔧 AUTOMATIC: This adds your custom sequences to the robot commands
for seq in MY_CUSTOM_SEQUENCES:
    if seq:  # Only add non-empty sequences
        ROBOT_COMMANDS[seq["name"]] = {
            "sequence": seq["sequence"], 
            "description": seq["description"]
        }
# 🎯 YOUR TASK: Modify the setting below to enables sequences!
ENABLE_SEQUENCES = False

# 🚀 This runs your AI with sequence capabilities
if __name__ == "__main__":
    print("🎯 CHALLENGE 3: Command Sequences")
    
    if ENABLE_SEQUENCES:
        print("✅ Sequences ENABLED - you can create multi-step actions!")
        sequence_count = len([cmd for cmd in ROBOT_COMMANDS.values() if "sequence" in cmd])
        print(f"📊 You have {sequence_count} sequences defined")
    else:
        print("⚠️  Sequences DISABLED - change ENABLE_SEQUENCES to True above")
    
    print("Try asking for 'dance' or other sequence commands you create!\n")
    
    try:
        robot = RobotAI(
            commands=ROBOT_COMMANDS,
            show_commands=True,  # Keep transparency on to see sequences in action
            enable_sequences=ENABLE_SEQUENCES
        )
        print("💡 NEXT: When done, open challenge-4-rag.py\n")
        robot.run()
    except SystemExit:
        # Don't show "next challenge" message if setup failed
        pass
