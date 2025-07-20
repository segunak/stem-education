"""
Robot Controller - Shared Logic
===============================

This file contains all the complex robot control logic.
Students don't need to edit this - it handles the technical details!

The challenge files import this to focus on learning AI concepts.
"""

import os
import sys
import urllib.request
from PetoiRobot import *
from openai import OpenAI
from dotenv import load_dotenv

class RobotAI:
    """
    AI Robot Controller that handles all the complex setup and execution.
    Challenge files create instances of this with different configurations.
    """
    
    def __init__(self, commands=None, show_commands=False, enable_sequences=False, enable_full_api=False, api_url=None):
        """Initialize the robot AI with specific challenge settings"""
        self.commands = commands or {}
        self.show_commands = show_commands
        self.enable_sequences = enable_sequences
        self.enable_full_api = enable_full_api
        self.api_url = api_url
        
        # Setup everything
        self.openai_client = self._setup_openai()
        self._connect_robot()
    
    def _setup_openai(self):
        """Setup OpenAI API - requires .env file with API key"""
        # Look for .env file in the lib directory (where this file is located)
        lib_dir = os.path.dirname(os.path.abspath(__file__))
        env_path = os.path.join(lib_dir, '.env')
        
        load_dotenv(env_path)
        api_key = os.getenv('OPENAI_API_KEY')
        
        if not api_key:
            print("❌ Missing API Key!")
            print(f"   Looking for .env file at: {env_path}")
            
            # Create .env file template if it doesn't exist
            if not os.path.exists(env_path):
                print("   Creating .env template file...")
                try:
                    with open(env_path, 'w') as f:
                        f.write("# OpenAI API Configuration\n")
                        f.write("# Replace 'your_key_here' with your actual OpenAI API key\n")
                        f.write("OPENAI_API_KEY=your_key_here\n")
                    print(f"   ✅ Created .env template at: {env_path}")
                except Exception as e:
                    print(f"   ❌ Could not create .env file: {e}")
            
            print("\n   SETUP INSTRUCTIONS:")
            print(f"   1. Open the file: {env_path}")
            print("   2. Replace 'your_key_here' with your actual OpenAI API key")
            print("   3. Save the file")
            print("   4. Run this program again")
            print("\n   Ask your instructor for help getting an API key!")
            input("\nPress Enter to exit...")
            sys.exit(1)
        
        return OpenAI(api_key=api_key)
    
    def _connect_robot(self):
        """Connect to robot dog with error handling"""
        print("🤖 Connecting to robot dog...")
        print("   (This may take a few seconds...)")
        
        try:
            # Suppress verbose Petoi library output
            import logging
            logging.getLogger('Petoi').setLevel(logging.ERROR)
            
            autoConnect()
            print("✅ Robot connected!")
            
        except Exception as e:
            print(f"❌ Could not connect to robot")
            print("   Check that the robot is:")
            print("   • Powered on (green light)")
            print("   • Connected via USB cable OR paired via Bluetooth")
            print("   • Not connected to another program")
            print(f"\n   Technical error: {e}")
            
            choice = input("\nTry again? (y/n): ").lower()
            if choice == 'y':
                return self._connect_robot()
            else:
                print("   Exiting... Connect your robot and try again!")
                sys.exit(1)
    
    def fetch_api_documentation(self):
        """
        Fetch API documentation from URL.
        This is implemented here so students can call it from Challenge 4.
        """
        if not self.api_url:
            return None
            
        try:
            with urllib.request.urlopen(self.api_url) as response:
                return response.read().decode('utf-8')
        except Exception as e:
            print(f"⚠️  Could not fetch API documentation: {e}")
            return None
    
    def _create_ai_instructions(self):
        """Create AI instructions based on current challenge settings"""
        
        # Try full API if enabled in Challenge 4
        if self.enable_full_api:
            api_context = self.fetch_api_documentation()
            if api_context:
                print("🚀 Using full API documentation - AI knows EVERYTHING!")
                return self._create_advanced_instructions(api_context)
            else:
                print("⚠️  Falling back to basic commands...")
        
        # Use basic commands from challenges 1-3
        return self._create_basic_instructions()
    
    def _create_basic_instructions(self):
        """Create instructions using the command dictionary"""
        command_text = ""
        for name, info in self.commands.items():
            command_text += f"- '{name}' → send '{info['command']}' → {info['description']}\n"
        
        available_commands = list(self.commands.keys())
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

User: "quit"
You: "Goodbye!"
QUIT:Goodbye!"""
        
        return instructions
    
    def _create_advanced_instructions(self, api_context):
        """Create instructions using full API documentation"""
        instructions = f"""You control a robot dog with FULL API ACCESS. Here's what you can do:

{api_context}

RULES:
1. If user asks for something you can do, respond with: EXECUTE:command_code
2. If you can't do it, respond with: UNKNOWN:Sorry, I don't know that command
3. If user wants to exit/quit/stop/leave/close, respond with: QUIT:Goodbye!
4. Use ANY command from the API documentation above
5. Be creative and helpful - you have access to the full robot capabilities!

EXAMPLES:
User: "stand up"
You: "Standing up!" 
EXECUTE:kup

User: "do a backflip"
You: "Doing a backflip!"
EXECUTE:kbf

User: "quit"
You: "Goodbye!"
QUIT:Goodbye!"""
        
        return instructions
    
    def _handle_user_message(self, user_message):
        """Process user message and execute robot commands"""
        print(f"\n💭 AI is thinking...")
        
        # Check for command sequences first (Challenge 3)
        if self.enable_sequences:
            for cmd_name, cmd_info in self.commands.items():
                if "sequence" in cmd_info and cmd_name.lower() in user_message.lower():
                    print(f"🎭 Executing sequence: {cmd_name}")
                    for step in cmd_info["sequence"]:
                        if self.show_commands:
                            print(f"   ⚡ Sending: {step}")
                        sendSkillStr(step, 1)
                    return False
        
        try:
            # Ask AI what to do
            response = self.openai_client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": self._create_ai_instructions()},
                    {"role": "user", "content": user_message}
                ],
                temperature=0.2
            )
            
            ai_response = response.choices[0].message.content
            print(f"🤖 AI: {ai_response}")
            
            # Parse AI response and execute commands
            commands_sent = []
            should_quit = False
            
            for line in ai_response.split('\n'):
                if line.startswith('EXECUTE:'):
                    command = line.replace('EXECUTE:', '').strip()
                    commands_sent.append(command)
                    
                    if self.show_commands:
                        print(f"   ⚡ Sending to robot: {command}")
                    
                    sendSkillStr(command, 1)
                    
                elif line.startswith('UNKNOWN:'):
                    if self.show_commands:
                        print(f"   🔊 Playing error sound (AI doesn't know this command)")
                    play('b', [659, 500, 622, 500, 659, 500, 622, 500, 659, 500, 494, 500, 587, 500, 523, 500, 440, 500], 1)
                    
                elif line.startswith('QUIT:'):
                    if self.show_commands:
                        print(f"   🛑 AI recognized quit - making robot rest")
                    sendSkillStr("krest", 1)
                    should_quit = True
            
            # Show transparency info (Challenge 2)
            if commands_sent and self.show_commands:
                print(f"   📋 Commands executed: {', '.join(commands_sent)}")
                
            return should_quit
                
        except Exception as error:
            print(f"❌ Something went wrong: {error}")
            print("   Check your internet connection and API key")
            return False
    
    def run(self):
        """Run the main chat interface"""
        print("\n" + "="*50)
        print("🎯 AI Robot Controller")
        print("="*50)
        
        print("The AI currently knows these commands:")
        for name, info in self.commands.items():
            print(f"  ✓ '{name}' - {info['description']}")
        
        print(f"\nTry typing commands in natural language!")
        print("Type 'quit' to exit when done")
        print("="*50)
        
        while True:
            try:
                user_input = input("\n💬 You: ").strip()
                
                if user_input.lower() in ['quit', 'exit']:
                    break
                elif not user_input:
                    continue
                
                should_quit = self._handle_user_message(user_input)
                if should_quit:
                    break
                    
            except KeyboardInterrupt:
                print("\n\n👋 Stopping...")
                break
            except Exception as error:
                print(f"\n❌ Unexpected error: {error}")
        
        # Clean shutdown
        print("\n🛑 Shutting down safely...")
        try:
            sendSkillStr("krest", 1)
            closePort()
            print("✅ Done!")
        except:
            print("✅ Done!")
