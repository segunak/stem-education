# Level 3: Prompt Engineering

import os
import json
from PetoiRobot import *
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
open_ai_api_key = os.getenv('OPENAI_API_KEY')
openai_client = OpenAI(api_key=open_ai_api_key)

autoConnect()

skill_commands = {
    "sit": "ksit",
    "stand up": "kup",
    "bottom up": "kbuttUp",
    "stretch": "kstr",
    "rest": "krest",
    "zero": "kzero",
    "boxing": "kbx",
    "cheer": "kchr",
    "check around": "kck",
    "dig": "kdg",
    "handstand": "khds",
    "hug": "khg",
    "hi": "khi",
    "hands up": "khu",
    "jump": "kjmp",
    "kick": "kkc",
    "nod": "knd",
    "play dead": "kpd",
    "pee": "kpee",
    "push up": "kpu",
    "scratch": "kscrh",
    "sniff": "ksnf",
    "stepping": "kvtF",
    "crawl forward": "kcrF",
    "crawl left": "kcrL",
    "crawl right": "kcrR",
    "push forward": "kphF",
    "push left": "kphL",
    "push right": "kphR",
    "walk forward": "kwkF",
    "walk left": "kwkL",
    "walk right": "kwkR",
    "back": "kbk",
    "back left": "kbkL",
    "back right": "kbkR",
    "trot forward": "ktrF",
    "trot left": "ktrL",
    "trot right": "ktrR",
    "back flip": "kbf",
    "front flip": "kff",
    "balance": "kbalance",
    "bound forward": "kbdF",
    "angry": "kang",
    "calibration pose": "kcalib",
    "dropped by back legs": "kdropped",
    "lifted by neck": "klifted",
    "landing pose": "klnd",
    "gap forward": "kgpF",
    "gap left": "kgpL",
    "halloween gait": "khlw",
    "jump forward": "kjpF",
    "push ups with one hand": "kpu1",
    "recover": "krc",
    "roll": "krl",
    "be table": "ktbl",
    "test": "kts",
    "wave head": "kwh",
    "all joint at 0 degrees": "kzz"
}

def translate_to_robot_command(natural_language_command):
    system_prompt_content = f"""
    You are a coding assistant for the Petoi Bittle X Robot Dog. This robot dog can perform various actions based on commands given to it. 
    Translate the following natural language command into a Python list of commands. Each command in the list should be a string in the format `sendSkillStr("<skillStr>", <delayTime>)`. 
    
    The delay time unit is an integer in seconds and should be set based on the user's input. If no delay is specified by the user, it should default to 1 second. 
    If the user specifies a delay using phrases such as "wait X seconds", "pause for X seconds", or "delay X seconds", use the specified delay time.

    The commands and their corresponding skill strings are as follows:
    {json.dumps(skill_commands, indent=2)}
    
    The `sendSkillStr` function takes the following parameters:
    - `skillStr` (str): The command string for the skill.
    - `delayTime` (int): The time to wait in seconds after the skill is performed.
    
    Example usage:
    `sendSkillStr("ksit", 1)`
    
    You must return only a syntactically correct Python list with the commands as strings, without any markdown formatting.
    
    You must be able to infer what command to execute based on the natural language command given to you. This includes translating words similar to the commands provided in the list above into the corresponding skill strings.
    
    For example, if the user says 'make the dog do a happy dance', this should be translated to the 'cheer' command. Similarly, 'make the robot dog fight' should be translated to the 'boxing' command.
    
    Your goal is to interpret the user's intent and map it to the closest matching command. 
    
    If you cannot map the command to a reasonable skill, return a Python list with a single command to play an error melody using the play() function.
    
    The play function takes the following parameters:
    - `token` (str): The command token, which should be 'b' for a beep sound.
    - `var` (list of int): The list of frequencies and durations.
    - `delayTime` (int): The time to wait in seconds after the sound is played.
    
    Example usage for an error melody:
    `play('b', [659, 500, 622, 500, 659, 500, 622, 500, 659, 500, 494, 500, 587, 500, 523, 500, 440, 500, 659, 500, 622, 500, 659, 500, 622, 500, 659, 500, 494, 500, 587, 500, 523, 500, 440, 500], 1)`
    
    Additionally, if a command involves repeating an action multiple times, such as 'jump 5 times', you should return the command using a for loop in Python. However, it should still be a syntactically correct Python list. For example, 'jump 5 times' should be translated to a list with a 1 string entry that is a for loop that repeats the 'kjmp' command 5 times with a delay of 1 second between each command since the user did not specify a custom delay time. However, if the user specifies a delay time, you should use that delay time instead of the default 1 second.
    
    Always, no matter what, return a syntactically correct Python list. Never return code fenced markdown or code blocks. The last command in the list, after taking into account user input (this is very important), should always be 'sendSkillStr('krest', 1)'. This ensures the robot dog does not continue with a command in perpetuity.
    """

    messages = [
        {
            "role": "system",
            "content": system_prompt_content
        },
        {
            "role": "user",
            "content": natural_language_command
        }
    ]

    response = openai_client.chat.completions.create(
        model="gpt-4o",
        messages=messages
    )
    
    response_text = response.choices[0].message.content
    print(f"Raw API response: {response_text}\n")
    
    return response_text

try:
    print("""Welcome to the Petoi "Bittle X" Robot Dog Control Terminal!
    
In this terminal, you can control the Petoi "Bittle X" Robot Dog using natural language commands. You can enter a single command or a series of commands, and the program will translate them into robot commands for the dog to perform.

For example, you can type:
- "Make the robot dog sit, then stand up, and then do a back flip."
- "Have the robot dog jump 5 times, then rest."

The available commands include actions like sitting, standing up, doing flips, and many more.

Give it a try and see your robot dog come to life!\n
    """)

    exit_commands = {'exit', 'quit', 'stop', 'leave', 'q'}
    
    while True:
        user_input = input(
            "Enter command(s) in natural (conversational) language."
            "\n\nTo exit, you may type any of the following commands:"
            "\n  - 'exit'"
            "\n  - 'quit'"
            "\n  - 'stop'"
            "\n  - 'leave'"
            "\n  - 'q'\n\nYour command: "
        ).strip().lower()

        if user_input in exit_commands:
            print("Exiting...")
            break
        
        api_response = translate_to_robot_command(user_input)
        
        try:
            commands = eval(api_response)
            for command in commands:
                print(f"Executing the command: {command}")
                exec(command)
        except Exception as e:
            print(f"Error executing the command: {e}")
            # Play error melody if there is an exception
            play('b', [659, 500, 622, 500, 659, 500, 622, 500, 659, 500, 494, 500, 587, 500, 523, 500, 440, 500, 659, 500, 622, 500, 659, 500, 622, 500, 659, 500, 494, 500, 587, 500, 523, 500, 440, 500], 1)
            
except KeyboardInterrupt:
    print("\nKeyboard interrupt received. Exiting...")
finally:
    closePort()
    print("Program terminated.")
    exit()