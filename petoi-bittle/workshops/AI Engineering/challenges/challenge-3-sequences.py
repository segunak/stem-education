"""
CHALLENGE 3: Command Sequences
==============================

🎯 MISSION: Teach the AI to do multiple actions in a row!
Instead of single commands, create sequences like "dance" or "morning routine".

📖 HOW SEQUENCES WORK:
Normal commands send one robot code. Sequences send multiple codes in order.
This lets you create complex behaviors from simple building blocks!

🔧 YOUR TASK:
1. Enable sequences by changing ENABLE_SEQUENCES to True
2. Add sequence commands to ROBOT_COMMANDS (see examples below)
3. Test your sequences - try asking the AI to "dance"!
4. Create your own creative sequences

💡 SEQUENCE FORMAT:
Instead of {"command": "code"}, use {"sequence": ["code1", "code2", "code3"]}

💡 IDEAS FOR SEQUENCES:
- "dance": combination of jumps, spins, and poses
- "morning routine": stretch, stand up, wave
- "show off": backflip, jump, wave, bow
- "patrol": walk forward, spin, walk back

RUN THIS FILE DIRECTLY - Click the ▶️ button!
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'lib'))

from robot_controller import RobotAI

# Robot commands with some sequence examples
ROBOT_COMMANDS = {
    # Regular single commands
    "stand up": {"command": "kup", "description": "Makes the robot stand up"},
    "sit down": {"command": "ksit", "description": "Makes the robot sit down"},
    "rest": {"command": "krest", "description": "Makes the robot rest"},
    "jump": {"command": "kjmp", "description": "Makes the robot jump"},
    "wave": {"command": "kwh", "description": "Makes the robot wave"},
    "backflip": {"command": "kbf", "description": "Makes the robot do a backflip"},
    "spin left": {"command": "kvtL", "description": "Makes the robot spin left"},
    "walk forward": {"command": "kwkF", "description": "Makes the robot walk forward"},
    
    # TODO: Add sequence commands here!
    # Example format:
    # "dance": {"sequence": ["kup", "kvtL", "kjmp", "ksit"], "description": "Does a dance routine"},
    # "morning routine": {"sequence": ["kstr", "kup", "kwh"], "description": "Stretch, stand, wave"},
    
    # Add your own creative sequences!
    
}

# 🎯 YOUR TASK: Change this to True to enable sequences!
ENABLE_SEQUENCES = False  # TODO: Change this to True

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
        print("💡 NEXT: When done, open challenge-4-advanced.py\n")
        robot.run()
    except SystemExit:
        # Don't show "next challenge" message if setup failed
        pass
