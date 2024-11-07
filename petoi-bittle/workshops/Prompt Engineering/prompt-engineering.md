# User Story: Robot Dog Control With AI & Prompt Engineering

## Overview

In this workshop, you will learn the importance of prompt engineering and how precise input to AI models can make a significant difference in the output. The goal is to understand the amazing capabilities of AI, how to guide AI with detailed instructions, and how to write effective prompts that generate correct code. This workshop will highlight the evolving paradigm of programming with natural language as a superset of traditional programming languages.

## Objective

1. Understand the concept of prompt engineering and its importance in AI.
2. Learn how to craft detailed and specific prompts to guide AI effectively.
3. Experience fixing a piece of code and enhancing it to handle more complex requirements.
4. Write natural language prompts that generate specific sequences of actions for the Petoi Bittle X Robot Dog.

## Background

In today's AI-driven world, the ability to communicate effectively with AI models is becoming increasingly important. Just as programming languages serve as a bridge between human intentions and machine actions, natural language can serve as a higher-level abstraction for programming. However, this requires precision, clarity, and an understanding of both the capabilities and limitations of AI models.

This workshop will involve:

1. Fixing broken code to ensure it runs correctly.
2. Enhancing the code by improving the prompt given to the AI model.
3. Crafting natural language prompts to control the robot dog and achieve specific sequences of actions.

## Key Concepts

- **Prompt Engineering:** The process of designing and refining prompts to guide AI models effectively.
- **Natural Language Processing (NLP):** The ability of AI to understand and generate human language.
- **Precision in Language:** The need for detailed and specific instructions to achieve desired outcomes.

## Prerequisites

Before starting the exercise, make sure you have the necessary setup:

1. **Connect the Ports:** Use the `autoConnect()` function to establish a connection between the computer and the robot dog. This ensures that you can send commands to the robot dog.
2. Install the Python packages below on the computer to support AI capabilities (this is already done for you).
    `pip install python-dotenv openai`

## Exercise Tasks

**It is important that you complete this tasks in order. Don't skip ahead!**

### Task 1: Fix the Broken Code

The provided code is slightly broken. Your first task is to identify and fix the issue. Specifically, the part where multiple commands need to be executed is missing. You need to write a for loop to iterate over the list of commands.

**Hint:** Each command in the list is a string that needs to be executed using the `exec()` function. Print out the string value before executing it.

### Task 2: Enhance the Prompt

The initial prompt to the AI model (the variable called `system_prompt_content`) instructs it to return all `sendSkillStr("<skillStr>", <delayTime>)` code commands with a 1 second delay. Enhance the prompt to understand and determine the delay value based on the natural language input from the user.

**Hint:** Modify the system prompt to include instructions on how to handle custom delay values specified by the user. Ensure the system can interpret phrases like "wait 3 seconds," "pause for 2 seconds," etc. Your goal is to have the AI model return code that includes the delay described by the users's input.

### Task 3: Create a Natural Language Prompt

Given a set of instructions for the robot dog, write a natural language prompt that will generate the correct sequence of actions. You must write a natural language prompt that results in the robot dog doing the following actions in order, with the specified delays.

**Robot Dog Instructions:**

1. The robot dog should sit and delay 1 second.
2. The robot dog should stand and delay 1 second.
3. The robot dog should stretch and delay 1 seconds.
4. The robot dog should check around and delay 1 second.
5. The robot dog should stand on it's hands and delay 5 seconds.
6. The robot dog should should box and delay 5 seconds.
7. The robot dog should jump and delay 5 seconds.
8. The robot dog should front flip and delay 5 seconds.
9. The robot dog should back flip and delay 5 seconds.
10. The robot dog should do 1 jump and delay 5 seconds, 2 front flips and delay 5 seconds between each, 2 back flips and delay 5 seconds between each, 1 handstand and delay 7 seconds, and then rest and delay 1 second. To get this one right, you're going to have to craft a really good and detailed prompt!

You must type these instructions in natural language and ensure the AI model generates the correct code for the robot dog to perform the described actions.

## Acceptance Criteria

### Task 1: Fix the Broken Code

- **GIVEN:** The robot dog is connected.
- **WHEN:** The code is run.
- **THEN:** It should execute each command in the list by iterating over them and using `exec()`.

### Task 2: Enhance the Prompt

- **GIVEN:** The user specifies a custom delay in the natural language command.
- **WHEN:** The AI model generates the Python code.
- **THEN:** The generated code should include the specified delay.

### Task 3: Create a Natural Language Prompt

- **GIVEN:** The user provides a sequence of actions in natural language.
- **WHEN:** The AI model generates the Python code.
- **THEN:** The robot dog should perform the exact sequence of actions as described.

## Reference Code

This is the initial code provided to you. Start by fixing the broken part and then proceed with the enhancements.

```python
import os
import json
from PetoiRobot import *
from openai import OpenAI
from dotenv import load_dotenv

# Load the .env file
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
    "front flip": "kff"
}

def translate_to_robot_command(natural_language_command):
    #### Student Code Start ####

    system_prompt_content = f"""
    You are a coding assistant for the Petoi Bittle X Robot Dog. This robot dog can perform various actions based on commands given to it. 
    Translate the following natural language command into a Python list of commands. Each command in the list should be a string in the format `sendSkillStr("<skillStr>", <delayTime>)`. 

    The delay time unit is an integer in seconds and should always be set to 1.

    The commands and their corresponding skill strings are as follows:
    {json.dumps(skill_commands, indent=2)}
    
    The `sendSkillStr` function takes the following parameters:
    - `skillStr` (str): The command string for the skill.
    - `delayTime` (int): The time to wait in seconds after the skill is performed, which should be set to 1 unless specified by the user.
    
    Example usage:
    `sendSkillStr("ksit", 1)`
    
    You must return only a syntactically correct Python list with the commands as strings, without any markdown formatting.

    You must be able to infer what command to execute based on the natural language command given to you. This includes translating words similar to the commands provided in the list above into the corresponding skill strings.

    For example, if the user says 'make the dog do a happy dance', this should be translated to the 'cheer' command. Similarly, 'make the robot dog fight' should be translated to the 'boxing' command. 

    Your goal is to interpret the user's intent and map it to the closest matching command.

    If you cannot map the command to a reasonable skill, return a Python list with a single command to play a long error melody using the play() function.

    The play function takes the following parameters:
    - `token` (str): The command token, which should be 'b' for a beep sound.
    - `var` (list of int): The list of frequencies and durations.
    - `delayTime` (int): The time to wait in seconds after the sound is played, which should always be set to 1.
    
    Example usage for an error melody:
    `play('b', [659, 500, 622, 500, 659, 500, 622, 500, 659, 500, 494, 500, 587, 500, 523, 500, 440, 500, 659, 500, 622, 500, 659, 500, 622, 500, 659, 500, 494, 500, 587, 500, 523, 500, 440, 500], 1)`

    Additionally, if a command involves repeating an action multiple times, such as 'jump 5 times', you should return the command using a for loop in Python. However, it should still be a syntactically correct Python list. For example, 'jump 5 times' should be translated to a list with a 1 string entry that is a for loop that repeats the 'kjmp' command 5 times using the default delay value.

    Always, no matter what, return a syntactically correct Python list. Never return code fenced markdown or code blocks.
    """
    #### Student Code End ####

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
        model="gpt-4-turbo",
        messages=messages
    )
    
    response_text = response.choices[0].message.content
    print(f"Raw API response: {response_text}\n")
    return response_text

try:
    print("""Welcome to the Petoi "Bittle X

" Robot Dog Control Terminal!
    
In this terminal, you can control the Petoi "Bittle X" Robot Dog using natural language commands. You can enter a single command or a series of commands, and the program will translate them into robot commands for the dog to perform.

For example, you can type:
- "Make the robot dog sit, then stand up, and then do a back flip."

The available commands include actions like sitting, standing up, doing flips, and many more.

Give it a try and see your robot dog come to life!\n\n
    """)

    while True:
        user_input = input("Enter command(s) in natural (conversational) language (or 'exit' to quit): ").strip().lower()

        if user_input == 'exit':
            print("Exiting...")
            break
        
        api_response = translate_to_robot_command(user_input)
        
        try:
            commands = eval(api_response)
            #### Student Code Start ####


            #### Student Code End ####
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
```

## Conclusion

By the end of this workshop, you will have a deeper understanding of prompt engineering and how to guide AI models effectively. You will have experienced fixing broken code, enhancing it, and crafting detailed natural language prompts to achieve specific actions with the Petoi Bittle X Robot Dog. Remember, the key to effective prompt engineering is precision, clarity, and attention to detail.
