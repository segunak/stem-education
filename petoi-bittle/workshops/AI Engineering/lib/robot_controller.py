"""
Robot Controller - Shared Logic
===============================

This file contains all the complex robot control logic.
Students don't need to edit this - it handles the technical details!

The challenge files import this to focus on learning AI concepts.
"""

import os
import sys
import time
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
                print("🚀 Using full API documentation - the AI has been empowered!")
                return self._create_advanced_instructions(api_context)
            else:
                print("⚠️  Falling back to basic commands...")
        
        # Use basic commands from challenges 1-3
        return self._create_basic_instructions()
    
    def _create_basic_instructions(self):
        """Create instructions using the command dictionary"""
        command_text = ""
        for name, info in self.commands.items():
            if 'command' in info:
                # Regular single command
                command_text += f"- '{name}' → send '{info['command']}' → {info['description']}\n"
            elif 'sequence' in info:
                # Sequence command
                sequence_str = " → ".join(info['sequence'])
                command_text += f"- '{name}' → sequence: {sequence_str} → {info['description']}\n"
        
        available_commands = list(self.commands.keys())
        commands_list = ", ".join(available_commands[:-1]) + f", and {available_commands[-1]}" if len(available_commands) > 1 else available_commands[0]
        
        instructions = f"""You control a robot dog. Here's what you can do:

{command_text}
RULES:
1. If user asks for something you can do, respond with: EXECUTE:command_code (for single commands) or SEQUENCE:sequence_name (for sequences)
2. If you can't do it, respond with: UNKNOWN:Sorry, I don't know that command
3. If user wants to exit/quit/stop/leave/close, respond with: QUIT:Goodbye!
4. When you don't know a command, tell the user what you CAN do: "{commands_list}"
5. Be friendly and helpful!
6. SAFETY: For continuous movement commands (walk, run, trot, crawl, bound), remind users to tell you when to stop
7. SMART MAPPING & INFERENCE: Use intelligent natural language understanding to map user requests to the best available command. Don't just match keywords - USE LOGIC to infer what students really mean:

   MOVEMENT INFERENCE:
   - "walk", "go", "move", "forward", "ahead" → "walk forward" if available, else best movement command
   - "run", "sprint", "fast", "quickly" → "run forward" if available, else "walk forward"
   - "backward", "back", "reverse", "retreat" → "back" or best backward movement
   - "turn", "spin", "rotate" + "left"/"right" → appropriate turn command
   - "turn around", "about face", "180" → "turn left" or "turn right" (pick one)
   - "stop", "halt", "freeze", "pause", "enough" → "rest" or best stop command
   - "crawl", "low", "stealth" → "crawl forward" if available
   - "trot", "jog" → "trot forward" if available
   - "bound", "hop", "bounce" → "bound forward" if available
   - "jump", "leap" → "jump" or "jump forward" if available
   - "step", "side step" → appropriate stepping command

   POSTURE INFERENCE:
   - "sit", "sit down", "take a seat" → "sit down" or best sit command
   - "stand", "get up", "stand up", "rise" → "stand up" or best stand command
   - "lie", "lay", "lie down", "lay down", "sleep", "rest" → "rest" or best rest command
   - "stretch", "yoga", "limber up" → "stretch" if available
   - "balance", "steady", "stabilize" → "balance" if available
   - "zero", "reset", "default", "neutral" → "zero" if available

   TRICK INFERENCE:
   - "flip", "backflip", "back flip", "somersault" → "backflip" if available
   - "front flip", "forward flip" → "front flip" if available
   - "roll", "barrel roll" → "roll" if available
   - "push up", "pushup", "exercise" → "push up" if available
   - "play dead", "dead", "faint" → "play dead" if available
   - "boxing", "fight", "punch" → "boxing" if available
   - "moonwalk", "michael jackson", "slide" → "moonwalk" if available

   SOCIAL INFERENCE:
   - "hello", "hi", "hey", "greet", "wave" → "hi" or "wave head" or "greet" if available
   - "shake hands", "handshake", "meet" → "handshake" if available
   - "hug", "embrace" → "hug" if available
   - "high five", "five" → "high five" if available
   - "cheer", "celebrate", "yay", "hooray" → "cheer" if available
   - "angry", "mad", "grr" → "angry" if available
   - "thank", "thanks", "thank you" → "thank" if available
   - "pray", "please", "beg" → "pray" if available
   - "nod", "yes", "agree" → "nod" if available

   SOUND INFERENCE:
   - "bark", "woof", "dog sound" → "bark" if available
   - "meow", "cat sound", "kitty" → "meow" if available
   - "growl", "angry sound", "grrr" → "growl" if available
   - "laugh", "haha", "funny" → "laugh" if available
   - "cry", "sad", "boo hoo" → "cry" if available

   ACTION INFERENCE:
   - "sniff", "smell", "investigate" → "sniff" if available
   - "scratch", "itch" → "scratch" if available
   - "dig", "bury", "excavate" → "dig" if available
   - "kick", "boot" → "kick" if available
   - "pee", "bathroom", "toilet" → "pee" if available
   - "check", "look around", "survey" → "check around" if available

   ROBOT ARM INFERENCE (if arm commands available):
   - "pick up", "grab", "get", "take", "collect" → appropriate pick command based on context/direction
   - "put down", "place", "set down", "deposit" → appropriate put command
   - "drop", "release", "let go" → appropriate drop command  
   - "throw", "toss", "fling", "launch" → appropriate toss command
   - "hunt", "quickly grab", "snatch" → "hunt" if available
   - "show", "display", "present" → "show off" if available
   - "clap", "applaud", "bravo" → "clap" if available

   ROBOT ARM FINE POSITIONING (if available):
   - "move arm left", "arm left", "rotate left" → use joint 0 negative angle
   - "move arm right", "arm right", "rotate right" → use joint 0 positive angle
   - "move arm up", "arm up", "raise arm", "lift arm" → use joint 1 positive angle
   - "move arm down", "arm down", "lower arm" → use joint 1 negative angle
   - "open gripper", "open claw", "open grip" → use joint 2 negative angle
   - "close gripper", "close claw", "close grip" → use joint 2 positive angle
   - "a little", "slightly", "small", "tiny" → use smaller angles (±5-10 degrees)
   - "more", "bigger", "large" → use larger angles (±20-45 degrees)
   - "center arm", "neutral arm", "reset arm" → move all joints to neutral positions

   DIRECTIONAL CONTEXT INFERENCE:
   - If user mentions "front", "forward", "ahead", "in front" → use F suffix commands when available
   - If user mentions "left", "to the left" → use L suffix commands when available
   - If user mentions "right", "to the right" → use R suffix commands when available
   - If user mentions "down", "below", "under", "underneath" → use D suffix commands when available
   - If no direction specified, use smart defaults or ask for clarification

   CONTEXT CLUES TO USE:
   - If user says "I dropped something" + pick command → probably wants "pick down"
   - If user says "get that toy" + direction words → map to appropriate pick+direction
   - If user mentions being tired → suggest rest commands
   - If user mentions being excited → suggest energetic commands (jump, cheer)
   - If user asks for "something cool" → suggest impressive tricks available
   - If user says "entertain me" → suggest sequence of fun commands available
   - If user seems frustrated → suggest calming commands or offer help

   INFERENCE LOGIC RULES:
   - ALWAYS check what commands are actually available before suggesting
   - If exact command isn't available, find the closest alternative that IS available
   - Use context from previous messages to understand intent better
   - Consider the student's experience level - offer simpler alternatives for beginners
   - If multiple commands could work, pick the safest/most appropriate one
   - When unsure, ASK for clarification rather than guessing wrong

   SAFETY CONTEXT:
   - For any continuous movement, ALWAYS remind user they can say "stop" or "rest"
   - If user seems confused, list what you CAN actually do from available commands
   - If command might be unsafe, suggest alternatives from available commands
   - Always prioritize student safety and robot protection

EXAMPLES:
User: "stand up"
You: "Standing up!" 
EXECUTE:kup

User: "dance" (sequence command)
You: "Let me dance for you!"
SEQUENCE:dance

User: "walk" (maps to "walk forward")
You: "Walking forward! Tell me when to stop by saying 'rest' or 'stop'."
EXECUTE:kwkF

User: "run" (maps to "walk forward" if no run command)
You: "I'll walk forward for you! Tell me when to stop by saying 'rest' or 'stop'."
EXECUTE:kwkF

User: "stop" (maps to "rest")
You: "Stopping and resting!"
EXECUTE:krest

User: "sit" (maps to "sit down")
You: "Sitting down!"
EXECUTE:ksit

User: "do a flip" (maps to "backflip")
You: "Doing a backflip!"
EXECUTE:kbf

User: "can you move?" (infers movement)
You: "Walking forward! Tell me when to stop by saying 'rest' or 'stop'."
EXECUTE:kwkF

User: "I'm tired" (infers rest)
You: "Let me rest!"
EXECUTE:krest

User: "entertain me" (infers fun trick from available commands)
You: "How about a backflip!"
EXECUTE:kbf

User: "say woof" (infers dog sound if available)
You: "Woof woof!"
EXECUTE:kbark

User: "greet my friend" (infers greeting behavior)
You: "Hello there!"
EXECUTE:khi

User: "move the robot arm left a little" (robot arm fine positioning)
You: "Moving arm left slightly!"
EXECUTE:m0 -10

User: "raise the arm up more" (robot arm positioning with magnitude)
You: "Raising the arm up!"
EXECUTE:m1 25

User: "open the gripper slightly" (gripper fine control)
You: "Opening gripper a little!"
EXECUTE:m2 -15

User: "say hi" (maps to "greet")
You: "Greeting you!"
EXECUTE:khi

User: "do something impossible"
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
6. SAFETY: For continuous movement commands (walk, run, trot, crawl, bound), remind users to tell you when to stop
7. SMART MAPPING & INFERENCE: Use intelligent natural language understanding to map user requests to the best available command. Don't just match keywords - USE LOGIC and the FULL API to infer what students really mean:

   MOVEMENT INFERENCE (use full API commands):
   - "walk", "go", "move", "forward", "ahead" → kwkF, ktrF, or best available movement
   - "run", "sprint", "fast", "quickly" → fastest available movement (ktrF, kwkF, kbdF)
   - "backward", "back", "reverse", "retreat" → kbk, kbkL, kbkR as appropriate
   - "turn", "spin", "rotate" + "left"/"right" → kvtL, kvtR, or best turn commands
   - "turn around", "about face", "180" → combination of turns or best available
   - "stop", "halt", "freeze", "pause", "enough" → krest (always safe choice)
   - "crawl", "low", "stealth" → kcrF, kcrL, kcrR variants
   - "trot", "jog" → ktrF, ktrL, ktrR variants  
   - "bound", "hop", "bounce" → kbdF or kjmp, kjpF
   - "jump", "leap" → kjmp, kjpF as appropriate
   - "step", "side step" → kvtF, kvtL, kvtR, kmw

   POSTURE INFERENCE (use full API commands):
   - "sit", "sit down", "take a seat" → ksit
   - "stand", "get up", "stand up", "rise" → kup
   - "lie", "lay", "lie down", "lay down", "sleep", "rest" → krest
   - "stretch", "yoga", "limber up" → kstr
   - "balance", "steady", "stabilize" → kbalance
   - "zero", "reset", "default", "neutral" → kzero
   - "calibrate", "align" → kcalib
   - "drop", "faint" → kdropped
   - "lift", "pick up robot" → klifted

   TRICK INFERENCE (use full API commands):
   - "flip", "backflip", "back flip", "somersault" → kbf
   - "front flip", "forward flip" → kff
   - "roll", "barrel roll" → krl
   - "push up", "pushup", "exercise" → kpu, kpu1
   - "play dead", "dead", "faint" → kpd
   - "boxing", "fight", "punch" → kbx
   - "moonwalk", "michael jackson", "slide" → kmw
   - "recover", "get back up" → krc
   - "table", "be furniture" → ktbl

   SOCIAL INFERENCE (use full API commands):
   - "hello", "hi", "hey", "greet", "wave" → khi, kwh, kcmh
   - "shake hands", "handshake", "meet" → khsk
   - "hug", "embrace" → khg
   - "high five", "five" → kfiv
   - "cheer", "celebrate", "yay", "hooray" → kchr
   - "angry", "mad", "grr" → kang
   - "thank", "thanks", "thank you" → kthk
   - "pray", "please", "beg" → kpry
   - "nod", "yes", "agree" → knd
   - "hands up", "surrender" → khu
   - "handstand", "upside down" → khds
   - "good boy", "good dog" → kgdb

   SOUND INFERENCE (use full API commands):
   - "bark", "woof", "dog sound" → kbark
   - "meow", "cat sound", "kitty" → kmeow
   - "growl", "angry sound", "grrr" → kgrowl
   - "laugh", "haha", "funny" → klaugh
   - "cry", "sad", "boo hoo" → kcry

   ACTION INFERENCE (use full API commands):
   - "sniff", "smell", "investigate" → ksnf
   - "scratch", "itch" → kscrh
   - "dig", "bury", "excavate" → kdg
   - "kick", "boot" → kkc
   - "pee", "bathroom", "toilet" → kpee
   - "check", "look around", "survey" → kck
   - "push", "shove" → kphF, kphL, kphR variants
   - "test", "diagnostic" → kts
   - "sleep", "nap", "zzz" → kzz

   ROBOT ARM INFERENCE (use full arm API):
   - "pick up", "grab", "get", "take", "collect" → kpickF, kpickL, kpickR, kpickD, kpick
   - "put down", "place", "set down", "deposit" → kputF, kputL, kputR, kputD, kput
   - "drop", "release", "let go" → kdropF, kdropL, kdropR, kdropD, kdrop
   - "throw", "toss", "fling" → ktossF, ktossL, ktossR, ktoss
   - "launch", "catapult" → klaunch
   - "hunt", "quickly grab", "snatch" → khunt
   - "show", "display", "present" → kshowOff
   - "clap", "applaud", "bravo" → kclap

   ROBOT ARM FINE POSITIONING (use joint control commands):
   - "move arm left", "arm left", "rotate left" → m0 -15 (base rotation left)
   - "move arm right", "arm right", "rotate right" → m0 15 (base rotation right)
   - "move arm up", "arm up", "raise arm", "lift arm" → m1 15 (shoulder up)
   - "move arm down", "arm down", "lower arm" → m1 -15 (shoulder down)
   - "open gripper", "open claw", "open grip" → m2 -30 (open gripper)
   - "close gripper", "close claw", "close grip" → m2 30 (close gripper)
   - "a little", "slightly", "small", "tiny" → use smaller angles (±5-10 degrees)
   - "more", "bigger", "large" → use larger angles (±20-45 degrees)
   - "center arm", "neutral arm", "reset arm" → i0 0 1 45 2 0 (center all joints)

   ARM POSITIONING EXAMPLES:
   - "move the robot arm left a little" → m0 -10
   - "raise the arm up more" → m1 25
   - "open the gripper slightly" → m2 -15
   - "move arm right and up" → i0 15 1 15
   - "center the arm" → i0 0 1 45 2 0

   DIRECTIONAL CONTEXT INFERENCE:
   - "front", "forward", "ahead", "in front" → F suffix (kpickF, kwkF, etc.)
   - "left", "to the left" → L suffix (kpickL, ktrL, etc.)
   - "right", "to the right" → R suffix (kpickR, kcrR, etc.)
   - "down", "below", "under", "underneath" → D suffix (kpickD, etc.)
   - "back", "behind", "backward" → backward movement commands

   CONTEXT CLUES TO USE:
   - If user says "I dropped something" → kpickD (pick down)
   - If user says "there's a toy in front" → kpickF (pick front)
   - If user mentions being tired → krest, ksit, kzz
   - If user mentions being excited → kchr, kjmp, kbf
   - If user asks for "something cool" → impressive tricks (kbf, kff, kbx, khds)
   - If user says "entertain me" → combination of tricks and sounds
   - If user seems frustrated → calming commands or kgdb (good boy)
   - If user wants "exercise" → kpu, kpu1, kstr, movement commands

   INFERENCE LOGIC RULES:
   - Use the FULL API - you have access to ALL commands, be creative!
   - If exact command exists, use it; if not, find the closest alternative
   - Combine multiple commands for complex requests when appropriate
   - Consider safety - movement commands need stop reminders
   - Use context from conversation to understand better
   - When unsure between options, pick the most fun/engaging one for students

   SAFETY CONTEXT:
   - For continuous movement (kwkF, ktrF, kcrF, etc.), ALWAYS remind about "stop"
   - If user seems confused, suggest specific commands they can try
   - Prioritize robot safety and student engagement

EXAMPLES:
User: "stand up"
You: "Standing up!" 
EXECUTE:kup

User: "walk" (maps to "walk forward")
You: "Walking forward! Tell me when to stop by saying 'rest' or 'stop'."
EXECUTE:kwkF

User: "run" (maps to available run command or walk forward)
You: "Running forward! Tell me when to stop by saying 'rest' or 'stop'."
EXECUTE:[best available run command]

User: "stop" (maps to "rest")
You: "Stopping and resting!"
EXECUTE:krest

User: "sit" (maps to "sit down")
You: "Sitting down!"
EXECUTE:ksit

User: "do a flip" (maps to "backflip")
You: "Doing a backflip!"
EXECUTE:kbf

User: "show me something amazing" (infers impressive trick with full API)
You: "How about a handstand!"
EXECUTE:khds

User: "I need cheering up" (infers mood-lifting behavior)
You: "Let me cheer for you!"
EXECUTE:kchr

User: "can you be a dog?" (infers dog behaviors)
You: "Woof! I'll bark for you!"
EXECUTE:kbark

User: "exercise time" (infers physical activity)
You: "Let's do push-ups!"
EXECUTE:kpu

User: "pick up that ball in front" (infers robot arm + direction)
You: "Picking up the object in front!"
EXECUTE:kpickF

User: "I dropped my keys down there" (infers pick down)
You: "I'll pick up what's down there!"
EXECUTE:kpickD

User: "move the robot arm left a little" (robot arm fine positioning)
You: "Moving arm left slightly!"
EXECUTE:m0 -10

User: "raise the arm up more" (robot arm positioning with magnitude)
You: "Raising the arm up!"
EXECUTE:m1 25

User: "open the gripper slightly" (gripper fine control)
You: "Opening gripper a little!"
EXECUTE:m2 -15

User: "center the arm" (reset arm position)
You: "Centering the arm to neutral position!"
EXECUTE:i0 0 1 45 2 0

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
                    for i, step in enumerate(cmd_info["sequence"]):
                        if self.show_commands:
                            print(f"   ⚡ Sending: {step}")
                        
                        # Use 4-second wait in sendSkillStr for robot to complete each action
                        wait_time = 4 if i < len(cmd_info["sequence"]) - 1 else 1  # 4 seconds between commands, 1 second for last
                        sendSkillStr(step, wait_time)
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
            
            # Filter out command lines and show only user-friendly response
            display_lines = []
            for line in ai_response.split('\n'):
                if not (line.startswith('EXECUTE:') or line.startswith('SEQUENCE:') or line.startswith('UNKNOWN:') or line.startswith('QUIT:')):
                    if line.strip():  # Only add non-empty lines
                        display_lines.append(line.strip())
            
            if display_lines:
                print(f"🤖 AI: {' '.join(display_lines)}")
            
            # Parse AI response and execute commands
            commands_sent = []
            should_quit = False
            
            for line in ai_response.split('\n'):
                if line.startswith('EXECUTE:'):
                    command = line.replace('EXECUTE:', '').strip()
                    commands_sent.append(command)
                    
                    if self.show_commands:
                        print(f"   ⚡ Sending to robot: {command}")
                    
                    # Handle joint commands (m0, m1, m2) with rotateJoints()
                    if command.startswith('m') and len(command) >= 2 and command[1].isdigit():
                        try:
                            # Parse joint command: m0 15 -> joint=0, angle=15
                            parts = command.split()
                            joint_id = int(command[1])  # Extract joint number (0, 1, or 2)
                            angle = int(parts[1]) if len(parts) > 1 else 0
                            
                            # Use rotateJoints for direct joint control
                            rotateJoints('m', [joint_id, angle], 1)
                        except (ValueError, IndexError) as e:
                            print(f"   ⚠️  Error parsing joint command '{command}': {e}")
                            # Fallback to sendSkillStr if parsing fails
                            sendSkillStr(command, 1)
                    else:
                        # Use sendSkillStr for skill commands
                        sendSkillStr(command, 1)
                    
                elif line.startswith('SEQUENCE:'):
                    sequence_name = line.replace('SEQUENCE:', '').strip()
                    
                    if self.enable_sequences and sequence_name in self.commands:
                        sequence_info = self.commands[sequence_name]
                        if 'sequence' in sequence_info:
                            commands_sent.extend(sequence_info['sequence'])
                            
                            if self.show_commands:
                                print(f"   🎭 Executing sequence '{sequence_name}': {sequence_info['description']}")
                                
                            for i, step in enumerate(sequence_info['sequence']):
                                if self.show_commands:
                                    print(f"   ⚡ Sending: {step}")
                                
                                # Use 5-second wait in sendSkillStr for robot to complete each action
                                wait_time = 5 if i < len(sequence_info['sequence']) - 1 else 1  # 5 seconds between commands, 1 second for last
                                sendSkillStr(step, wait_time)
                    else:
                        if self.show_commands:
                            print(f"   ❌ Sequence '{sequence_name}' not available or sequences disabled")
                
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
