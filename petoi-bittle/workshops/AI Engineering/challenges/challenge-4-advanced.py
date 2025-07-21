"""
CHALLENGE 4: Full API Connection (ADVANCED)
===========================================

🎯 MISSION: Connect AI to live robot documentation from the internet!
This is called "Retrieval Augmented Generation" (RAG).

🔧 STEP BY STEP:
1. Click ▶️ (play button, upper right corner) - AI knows limited commands from previous challenges
2. Look for the setting below that controls API access
3. Figure out how to enable it (hint: it's currently disabled)
4. Copy the example code in fetch_api_documentation() and uncomment it
5. Click ▶️ - now AI knows EVERYTHING about the robot!
6. Check robot-dog-commands.md for more advanced commands to try

💡 RAG: Instead of pre-programming knowledge, AI fetches it live from URLs
💡 COPY & PASTE: The example code is provided - just copy and uncomment it!

💡 TO EXIT: Type "quit" or "exit" in the chat, then click ▶️ to run again

RUN THIS FILE DIRECTLY - Click the ▶️ button (upper right corner)!
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'lib'))

from robot_controller import RobotAI
from robot_commands import FULL_COMMANDS
import urllib.request

# 🎓 AUTO-LOADED: All commands from previous challenges!
# 🎯 YOUR FOCUS: Learn Retrieval Augmented Generation (RAG)

# Fallback commands if API fails
ROBOT_COMMANDS = FULL_COMMANDS

# 🎯 YOUR TASK: Find the setting below that enables full API access!
ENABLE_FULL_API = False  # TODO: You need to change this line

# The URL to the complete robot API documentation
API_URL = "https://raw.githubusercontent.com/segunak/stem-education/refs/heads/master/petoi-bittle/documentation/petoi-python-api-specification.md"

def fetch_api_documentation():
    """
    🎯 YOUR IMPLEMENTATION WORKSPACE
    
    This function should fetch the robot API documentation from the internet.
    This is called "Retrieval Augmented Generation" (RAG) - getting fresh data for AI!
    
    💡 STEP-BY-STEP GUIDE:
    
    1. Use try/except to handle errors safely
    2. Inside try: use urllib.request.urlopen(API_URL) to open the URL
    3. Use .read() to get the data, then .decode('utf-8') to make it text
    4. Return the text
    5. In except: print error message and return None
    
    💡 EXAMPLE PATTERN:
    try:
        with urllib.request.urlopen(API_URL) as response:
            return response.read().decode('utf-8')
    except Exception as e:
        print(f"Error fetching API: {e}")
        return None
    
    Returns:
        str: The API documentation text, or None if failed
    """
    
    # TODO: Copy the example pattern above and uncomment it!
    # Replace this return None with the try/except code
    return None

# 🚀 This runs your AI with full API capabilities
if __name__ == "__main__":
    print("🎯 CHALLENGE 4: Full API Connection")
    
    if ENABLE_FULL_API:
        print("✅ Full API ENABLED - testing your implementation...")
        
        # Test the student's implementation
        result = fetch_api_documentation()
        if result:
            print(f"🚀 SUCCESS! Your implementation worked! Fetched {len(result)} characters")
            print("   The AI now has access to the complete robot documentation!")
        else:
            print("⚠️  Your implementation returned None - using robot_controller fallback")
            print("   (This still works, but try implementing the function for more learning!)")
    else:
        print("⚠️  Full API DISABLED - change ENABLE_FULL_API to True above")
    
    print("With full API, the AI should know ALL robot capabilities!\n")
    
    try:
        robot = RobotAI(
            commands=ROBOT_COMMANDS,
            show_commands=True,
            enable_sequences=True,
            enable_full_api=ENABLE_FULL_API,
            api_url=API_URL
        )
        print("🎉 CONGRATULATIONS! You've completed all 4 challenges!")
        print("💡 Try experimenting with advanced features and combinations!\n")
        robot.run()
    except SystemExit:
        # Don't show congratulations message if setup failed
        pass
