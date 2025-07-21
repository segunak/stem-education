"""
CHALLENGE 5: Robot Arm Control (ADVANCED - ARM REQUIRED)
========================================================

🤖 MISSION: Master robot arm control through expert prompting!
This challenge requires a Bittle X+Arm (robot dog with arm attachment).

🔧 STEP BY STEP:
1. Click ▶️ (play button, upper right corner) - the AI becomes a robot arm expert!
2. Read robot-arm-commands.md to understand arm capabilities
3. Find a small object in the room (toy, block, etc.)
4. Use natural language to control both dog movement AND arm actions
5. Pick up → Move → Put down sequence
6. Try complex multi-step prompts!

💡 NO CODE CHANGES: Just pure prompt engineering and documentation reading!
💡 SAFETY: Never put hands between robot claws when arm is moving!

🎯 CHALLENGES TO TRY:
- Navigate to object, pick it up, move somewhere else, put it down
- Do the entire sequence with ONE complex prompt
- Fine-tune arm positions ("move arm up a little", "open gripper more")
- Try different pickup positions (front, left, right, underneath)
- Combine walking, turning, and arm actions

💡 TO EXIT: Type "quit" or "exit" in the chat, then click ▶️ to run again

RUN THIS FILE DIRECTLY - Click the ▶️ button (upper right corner)!
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'lib'))

from robot_controller import RobotAI
from robot_commands import FULL_COMMANDS

# 🤖 AUTO-LOADED: ALL commands + sequences + FULL robot arm specification!
# 🎯 YOUR FOCUS: Read documentation and master prompting

# Use all available commands as base
ROBOT_COMMANDS = FULL_COMMANDS

# Robot arm specification URL for AI context
ARM_SPEC_URL = "https://raw.githubusercontent.com/segunak/stem-education/refs/heads/master/petoi-bittle/documentation/petoi-robot-arm-specification.md"

def detect_robot_arm():
    """
    Check if robot has arm attachment by analyzing the robot connection output.
    Look for model name and skill names to determine if arm is present.
    """
    try:
        # Try to detect arm by checking if this is actually a Bittle X+Arm model
        # The real detection should be based on the robot's model name or available skills
        
        # For now, we'll be more conservative and require explicit confirmation
        # In the output, we saw "modelName: Bittle" not "modelName: Bittle X+Arm"
        
        print("🔍 Checking for robot arm attachment...")
        print("   Looking for Bittle X+Arm model or arm-specific skills...")
        
        # Simple file-based check for arm model
        import os
        petoi_config_path = os.path.expanduser("~/.config/Petoi/SkillLibrary")
        
        # Check if BittleX+Arm directory exists (this existed in the output)
        arm_dir = os.path.join(petoi_config_path, "BittleX+Arm")
        if os.path.exists(arm_dir):
            print(f"   Found BittleX+Arm directory: {arm_dir}")
            
            # Additional check: ask user to confirm since directory existing doesn't guarantee arm hardware
            print("\n⚠️  IMPORTANT: Directory suggests arm model, but need to verify hardware")
            print("   Does your robot physically have an ARM ATTACHMENT? (y/n)")
            
            while True:
                response = input("   Robot has arm attachment? (y/n): ").lower().strip()
                if response in ['y', 'yes']:
                    print("✅ User confirmed: Robot arm present")
                    return True
                elif response in ['n', 'no']:
                    print("❌ User confirmed: No robot arm - directory may be from previous setup")
                    return False
                else:
                    print("   Please enter 'y' for yes or 'n' for no")
        else:
            print("   No BittleX+Arm directory found")
            return False
            
    except Exception as e:
        print(f"   Error during detection: {e}")
        return False

# 🚀 This runs your AI with FULL robot + arm expertise
if __name__ == "__main__":
    print("🤖 CHALLENGE 5: Robot Arm Control")
    print("="*50)
    
    # Check for robot arm
    has_arm = detect_robot_arm()
    
    if has_arm:
        print("✅ Robot Arm DETECTED - AI now knows ALL arm commands!")
        print("📚 Make sure to read robot-arm-commands.md for prompting tips")
        print("🎯 Your mission: Use prompts to pick up and move objects!")
    else:
        print("❌ Robot Arm NOT DETECTED")
        print("   This challenge requires a Bittle X+Arm model")
        print("   Check: https://docs.petoi.com/extensible-modules/robot-arm")
        input("Press Enter to exit...")
        sys.exit(1)
    
    print("\n🔧 SAFETY REMINDER: Keep hands away from robot claws during movement!")
    print("📖 Read robot-arm-commands.md for examples and tips")
    print("🚀 The AI knows EVERY robot and arm command - just prompt naturally!")
    print("="*50)
    
    try:
        robot = RobotAI(
            commands=ROBOT_COMMANDS,
            show_commands=True,  # Show transparency for learning
            enable_sequences=True,  # Enable sequences
            enable_full_api=True,   # Enable RAG for full capabilities
            api_url=ARM_SPEC_URL    # Load robot arm specification
        )
        print("\n🎉 ROBOT ARM EXPERT MODE ACTIVATED!")
        print("💡 Try: 'walk forward, pick up an object, turn around, and put it down'")
        print("💡 Read robot-arm-commands.md for more examples!\n")
        robot.run()
    except SystemExit:
        # Don't show success message if setup failed
        pass
