"""
AI Robot Controller - Context Engineering Workshop
====================================================

This program shows how AI becomes powerful through CONTEXT.

What you'll learn:
• AI only knows what we teach it
• By adding    # Clean shutdown
    print("\n🔄 Shutting down safely...")
    try:
        closePort()  # Close connection
        print("✅ Done!")
    except:
        print("✅ Done!")s to ROBOT_COMMANDS, you make AI smarter
• This is called "AI Engineering" - connecting AI to real systems

Your Challenge:
• The robot can do 50+ tricks
• This AI only knows 3 basic commands  
• Teach the AI more by adding commands to ROBOT_COMMANDS below

How to use:
1. Run this program
2. Try: "stand up", "sit down", "jump"
3. Add new commands and restart to test them
4. Check serial-protocol.md for all available robot commands
"""

import os
import sys
from PetoiRobot import *
from openai import OpenAI
from dotenv import load_dotenv

def setup_openai():
    """Setup OpenAI API - students need their API key in .env file"""
    load_dotenv()
    api_key = os.getenv('OPENAI_API_KEY')
    
    if not api_key:
        print("❌ Missing API Key!")
        print("   Create a .env file with: OPENAI_API_KEY=your_key_here")
        print("   Ask your instructor for help setting this up")
        input("\nPress Enter to exit...")
        sys.exit(1)
    
    return OpenAI(api_key=api_key)

def connect_robot():
    """Connect to robot dog - handles connection issues gracefully"""
    print("🤖 Connecting to robot dog...")
    print("   (This may take a few seconds...)")
    
    try:
        # Suppress verbose Petoi library output during connection
        import logging
        logging.getLogger('Petoi').setLevel(logging.ERROR)
        
        autoConnect()
        print("✅ Robot connected!")
        return True
        
    except Exception as e:
        print(f"❌ Could not connect to robot")
        print("   Check that the robot is:")
        print("   • Powered on (green light)")
        print("   • Connected via USB cable OR paired via Bluetooth")
        print("   • Not connected to another program")
        print(f"\n   Technical error: {e}")
        
        choice = input("\nTry again? (y/n): ").lower()
        if choice == 'y':
            return connect_robot()  # Try again
        else:
            print("   Exiting... Connect your robot and try again!")
            sys.exit(1)

# Initialize everything
openai_client = setup_openai()
connect_robot()

# =============================================================================
# STUDENT WORKSPACE - This is where you add new commands!
# =============================================================================

# BONUS CHALLENGE: Can you make the AI show what commands it's sending?
# HINT: You'd have to change the line below! But to what? Guess, or ask ChatGPT!
SHOW_ROBOT_COMMANDS = False

ROBOT_COMMANDS = {
    # The AI starts with only these 3 commands
    "stand up": {"command": "kup", "description": "Makes the robot stand up"},
    "sit down": {"command": "ksit", "description": "Makes the robot sit down"},  
    "rest": {"command": "krest", "description": "Makes the robot rest"},
    
    # YOUR CHALLENGE: Add more commands here!
    # Check serial-protocol.md for the command codes
    # Example: "jump": {"command": "kjmp", "description": "Makes the robot jump"},
}

def create_ai_instructions():
    """
    This creates the instructions we give to AI.
    This is the 'context' that makes the AI smart!
    """
    # Convert our commands into instructions for AI
    command_text = ""
    for name, info in ROBOT_COMMANDS.items():
        command_text += f"- '{name}' → send '{info['command']}' → {info['description']}\n"
    
    # Create a dynamic list of available commands for AI to reference
    available_commands = list(ROBOT_COMMANDS.keys())
    commands_list = ", ".join(available_commands[:-1]) + f", and {available_commands[-1]}" if len(available_commands) > 1 else available_commands[0]
    
    instructions = f"""You control a robot dog. Here's what you can do:

{command_text}
RULES:
1. If user asks for something you can do, respond with: EXECUTE:command_code
2. If you can't do it, respond with: UNKNOWN:Sorry, I don't know that command
3. If user wants to exit/quit/stop/leave/close, respond with: QUIT:Goodbye!
4. When you don't know a command, tell the user what you CAN do: "{commands_list}"
5. Be friendly and helpful!

EXAMPLES:
User: "stand up"
You: "Standing up!" 
EXECUTE:kup

User: "do a backflip"
You: "I don't know that command yet. I can: {commands_list}"
UNKNOWN:Sorry, I don't know that command

User: "quit" or "exit" or "stop"
You: "Goodbye!"
QUIT:Goodbye!"""

    return instructions

def ask_ai_to_control_robot(user_message):
    """
    Send the user's message to AI and execute robot commands.
    This is where AI Engineering happens!
    """
    print(f"\n💭 Thinking...")
    
    try:
        # Ask AI what to do using our instructions
        response = openai_client.chat.completions.create(
            model="gpt-4o-mini",  # Cost-effective model perfect for workshops
            messages=[
                {"role": "system", "content": create_ai_instructions()},
                {"role": "user", "content": user_message}
            ],
            temperature=0.2  # Keep responses consistent
        )
        
        ai_response = response.choices[0].message.content
        print(f"🤖 AI: {ai_response}")
        
        # Look for commands in AI's response
        commands_sent = []
        should_quit = False
        
        for line in ai_response.split('\n'):
            
            if line.startswith('EXECUTE:'):
                # AI wants to send a command to robot
                command = line.replace('EXECUTE:', '').strip()
                commands_sent.append(command)
                
                # RESPONSIBLE AI: Show what's happening (if enabled)
                if SHOW_ROBOT_COMMANDS:
                    print(f"   ⚡ Sending to robot: {command}")
                
                sendSkillStr(command, 1)  # Send command with 1 second delay
                
            elif line.startswith('UNKNOWN:'):
                # AI doesn't know this command - make error sound
                if SHOW_ROBOT_COMMANDS:
                    print(f"   🔊 Error sound (AI doesn't know this command)")
                play('b', [659, 500, 622, 500, 659, 500, 622, 500, 659, 500, 494, 500, 587, 500, 523, 500, 440, 500], 1)
                
            elif line.startswith('QUIT:'):
                # User wants to quit - make robot rest and signal to exit
                if SHOW_ROBOT_COMMANDS:
                    print(f"   🛑 AI recognized quit command - making robot rest")
                sendSkillStr("krest", 1)
                should_quit = True
        
        # Show what actually happened (this is responsible AI!)
        if commands_sent and SHOW_ROBOT_COMMANDS:
            print(f"   📋 Robot commands executed: {', '.join(commands_sent)}")
            
        return should_quit
            
    except Exception as error:
        print(f"❌ Something went wrong: {error}")
        print("   Check your internet connection and API key")
        return False

def show_welcome():
    """Show welcome message and current robot capabilities"""
    print("\n" + "="*50)
    print("🎯 AI Robot Controller")
    print("="*50)
    
    print("The AI currently knows these commands:")
    for name, info in ROBOT_COMMANDS.items():
        print(f"  ✓ '{name}' - {info['description']}")
    
    print(f"\nBut the robot can do 50+ things! Your job: teach the AI more.")
    print("\nTry these:")
    print("  • 'stand up' (works)")
    print("  • 'sit down' (works)")  
    print("  • 'jump' (doesn't work yet - you need to add it!)")
    print("\nType 'help' for tips, 'quit' to exit")
    print("="*50)

def show_help():
    """Show help and available commands"""
    print(f"\n📚 AI knows these {len(ROBOT_COMMANDS)} commands:")
    for name in ROBOT_COMMANDS.keys():
        print(f"  • {name}")
    
    print("\n💡 To teach AI more commands:")
    print("  1. Open serial-protocol.md to see all robot commands")
    print("  2. Add new entries to ROBOT_COMMANDS in this file")
    print("  3. Save and restart the program")
    print("  4. Test your new commands!")

def main():
    """Main chat loop - this is where students interact with AI"""
    show_welcome()
    
    while True:
        try:
            # Get what the student wants to do
            user_input = input("\n💬 You: ").strip()
            
            # Handle special commands
            if user_input.lower() in ['quit', 'exit']:
                break
            elif user_input.lower() == 'help':
                show_help()
                continue
            elif not user_input:
                continue
            
            # Send to AI and execute robot commands
            should_quit = ask_ai_to_control_robot(user_input)
            if should_quit:
                break
            
        except KeyboardInterrupt:
            print("\n\n👋 Stopping...")
            break
        except Exception as error:
            print(f"\n❌ Unexpected error: {error}")
    
    # Clean shutdown
    print("\n� Shutting down safely...")
    try:
        sendSkillStr("krest", 1)  # Make robot rest
        closePort()  # Close connection
        print("✅ Done!")
    except:
        print("✅ Done!")

if __name__ == "__main__":
    main()
