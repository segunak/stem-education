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
    "push ups with one hand": "kpu1",
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
    "moon walk": "kmw",
    "high five": "kfiv",
    "good boy": "kgdb",
    "leap over": "klpov",
    "wave head": "kwh",
    "recover": "krc",
    "roll": "krl",
    "be table": "ktbl",
    "test": "kts",
    "all joint at 0 degrees": "kzz"
}

def translate_to_robot_command(natural_language_command):
    system_prompt_content = f"""
    You are an advanced coding assistant for the Petoi Bittle X Robot Dog. This robot dog can perform various actions based on commands given to it. Your role is to translate natural language commands into executable Python code that controls the robot dog based on the specified actions. Each command should be represented as a Python list of strings in the format `sendSkillStr("<skillStr>", <delayTime>)` representing the Python function by which the dog can be controlled.
    
    The `sendSkillStr` function takes the following parameters:
    - `skillStr` (str): The command string for the skill.
    - `delayTime` (int): The time to wait in seconds after the skill is performed.
    
    Example usage:
    `sendSkillStr("ksit", 1)`
    
    The commands and their corresponding skill strings are as follows:
    {json.dumps(skill_commands, indent=2)}
    
    Rules for Command Interpretation:
    
    You must follow the following rules in interpeting commands and returning output.
    
    - You must return only a syntactically correct Python list with the commands as strings, without any markdown formatting. This is critical. No markdown formatting, always return a valid Python list.
    - The delay time (in seconds) defaults to 1 unless specified by the user. If the user indicates timing with phrases like "wait X seconds", "pause for X seconds", or "delay X seconds" adjust the delay accordingly.
    - For unknown or ambiguous commands, return a Python list with an error melody using `play('b', [659, 500, 622, 500, 659, 500, 622, 500, 659, 500, 494, 500, 587, 500, 523, 500, 440, 500, 659, 500, 622, 500, 659, 500, 622, 500, 659, 500, 494, 500, 587, 500, 523, 500, 440, 500], 1)`.
    - Handle synonymous terms. For example:
        - "Sit" or "take a seat" should map to `ksit`.
        - "Stand up" or "get up" should map to `kup`.
    - Use the closest command when exact matches aren't found, and notify the user when appropriate.
    - Recognize and interpret user instructions that involve sequences, repetitions, or conditions. Examples:
        - "Do X three times, then Y" should be translated as a loop with the correct delay.
        - Phrases like "pause a bit" or "wait before doing X" should interpret reasonable delays.
        - Finalize each series of commands with `sendSkillStr('krest', 1)` to neutralize the robot's state after executing commands.
    
    Example Scenarios:
    - If the user says "make the dog do a happy dance", interpret this as the "cheer" command. Similarly, 'make the robot dog fight' should be translated to the 'boxing' command. You must intuit what the user means and map it to the closest command.
    - Another example, for "jump 5 times", return a for loop repeating `kjmp` with a 1-second delay, unless the user specifies a different delay.
    - Another example, for "guard by looking around", translate into a sequence or loop that performs a looking motion every few seconds.
    
    If you cannot map the command from the user to a reasonable skill, return a Python list with a command to play an error melody using the play() function.
        
    The play function takes the following parameters:
    - `token` (str): The command token, which should be 'b' for a beep sound.
    - `var` (list of int): The list of frequencies and durations.
    - `delayTime` (int): The time to wait in seconds after the sound is played.
    
    Example usage for an error melody:
    `play('b', [659, 500, 622, 500, 659, 500, 622, 500, 659, 500, 494, 500, 587, 500, 523, 500, 440, 500, 659, 500, 622, 500, 659, 500, 622, 500, 659, 500, 494, 500, 587, 500, 523, 500, 440, 500], 1)`
    
    You are tasked with interpreting commands as intuitively as possible, considering variations in user phrasing, timing, and sequence. No matter what, return a syntactically correct Python list with no markdown formatting. Never return code fenced markdown or code blocks. Remember that `sendSkillStr('krest', 1)` should always be the last command in the list.
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
            deacGyro()
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
    os._exit(0)
