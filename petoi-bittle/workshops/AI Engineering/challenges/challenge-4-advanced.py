"""
CHALLENGE 4: Full API Connection (ADVANCED)
===========================================

🎯 MISSION: Connect your AI to the complete robot API documentation online!
This is called "Retrieval Augmented Generation" (RAG) - a cutting-edge AI technique.

📖 WHAT IS RAG?
Instead of pre-programming all knowledge, RAG lets AI fetch information dynamically.
Your AI will pull the latest robot documentation from GitHub in real-time!

🔧 YOUR TASK:
1. Enable full API by changing ENABLE_FULL_API to True
2. Implement the fetch_api_documentation() function below
3. Test it - your AI should now know ALL robot capabilities!

💡 HINTS:
- The robot_controller already has a working fetch method you can call
- Or implement your own using urllib.request.urlopen()
- The API_URL points to the full robot specification on GitHub
- Ask GitHub Copilot: "How do I fetch text from a URL in Python?"

🚀 ADVANCED FEATURES:
- Parse the markdown to extract specific sections
- Cache the documentation to avoid repeated downloads
- Handle network errors gracefully
- Add your own API endpoints!

RUN THIS FILE DIRECTLY - Click the ▶️ button!
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'lib'))

from robot_controller import RobotAI
import urllib.request

# Basic commands (these will be replaced if full API works)
ROBOT_COMMANDS = {
    "stand up": {"command": "kup", "description": "Makes the robot stand up"},
    "sit down": {"command": "ksit", "description": "Makes the robot sit down"},
    "rest": {"command": "krest", "description": "Makes the robot rest"},
}

# 🎯 YOUR TASK: Change this to True to enable full API!
ENABLE_FULL_API = False  # TODO: Change this to True

# The URL to the complete robot API documentation
API_URL = "https://raw.githubusercontent.com/segunak/stem-education/refs/heads/master/petoi-bittle/documentation/petoi-python-api-specification.md"

def fetch_api_documentation():
    """
    🎯 YOUR IMPLEMENTATION WORKSPACE
    
    This function should fetch the robot API documentation from the internet.
    The robot_controller.py already has a working version, but try implementing your own!
    
    💡 APPROACHES:
    
    Option 1 (Easy): Return None and let robot_controller handle it
    Option 2 (Medium): Use urllib.request to fetch the URL
    Option 3 (Advanced): Parse the markdown and extract specific sections
    
    💡 HINTS:
    - urllib.request.urlopen(API_URL).read().decode('utf-8')
    - Handle exceptions with try/except
    - Return None if something goes wrong
    - Ask GitHub Copilot for help!
    
    Returns:
        str: The API documentation text, or None if failed
    """
    
    # TODO: Implement this function!
    # You can start simple and make it more advanced later
    
    # Option 1: Let robot_controller handle it (works but you don't learn as much)
    return None
    
    # Option 2: Implement yourself (more learning!)
    # try:
    #     # Your code here!
    #     pass
    # except Exception as e:
    #     print(f"Error fetching API: {e}")
    #     return None

# 🚀 This runs your AI with full API capabilities
if __name__ == "__main__":
    print("🎯 CHALLENGE 4: Full API Connection")
    
    if ENABLE_FULL_API:
        print("✅ Full API ENABLED - testing your implementation...")
        
        # Test the student's implementation
        result = fetch_api_documentation()
        if result:
            print(f"🚀 YOUR implementation worked! Fetched {len(result)} characters")
        else:
            print("⚠️  Your implementation returned None - using robot_controller fallback")
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
