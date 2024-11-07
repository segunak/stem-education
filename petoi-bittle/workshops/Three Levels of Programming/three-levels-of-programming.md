# Three Levels of Programming with the Petoi Bittle Robot Dog

## Overview

In this workshop, students will learn three distinct levels of programming through controlling the Petoi Bittle Robot Dog. We'll start at the lowest level of programming – **Serial Protocol**, then move to **Python Coding**, and finally explore the future of programming through **Prompt Engineering** with AI.

Each level introduces a progressively more abstracted form of controlling the robot dog, giving students a deeper understanding of how computers function, from low-level command execution to high-level AI-driven tasks.

### Key Objectives

- Understand the basics of Serial Protocol and how early computers were programmed.
- Write Python code to control the robot dog and compare it to the Serial Protocol commands.
- Learn about **Prompt Engineering** and how AI can be used to control computers.
- Highlight the evolution of programming from low-level hardware control to high-level AI-driven commands.
- Engage students in hands-on activities, making learning fun and interactive.

---

## Materials

- 1 Petoi Bittle Robot Dog per 4-5 students.
- Laptops/Desktops. 1 laptop per 4-5 students.
- Printed Serial Protocol documentation from Petoi found at <https://docs.petoi.com/apis/serial-protocol>.
- Mind+ and/or Visual Studio Code IDE installed on computers.
- Python installed on computers.
- Python packages `openai`, and `dotenv` installed via `pip`.
- The `PetoiRobot`, `SerialCommunication`, and `ardSerial` modules from Petoi, found at <https://github.com/PetoiCamp/Petoi_MindPlusLib/tree/main/python/libraries>.
- An OpenAI API key listed in a `.ENV` file that you **really should delete after the workshop**. You can get one at <https://platform.openai.com/api-keys>.
- Projector for demonstrating concepts and results.

---

## Level 1: Serial Protocol – The Foundation of Computing

### Objective

Introduce students to low-level programming by sending commands directly to the Petoi Bittle Robot Dog using the Serial Protocol. Explain how computers operate at this level and why it's foundational to all modern computing.

### Introduction

- Begin by explaining that **Serial Protocol** is one of the earliest ways to communicate directly with a machine.
- Show printed documentation from Petoi on the Serial Protocol commands.
- Demonstrate how to send a simple command to the robot dog to make it move.
- Highlight that these commands are almost at the lowest level – close to binary – and computers only understand instructions like these.

### Hands-On Activity

For details on sending serial protocol commands to the Petoi Bittle using Arduino, see <https://docs.petoi.com/arduino-ide/serial-monitor>. For details on sending serial protocol commands using Python (such as via a terminal in VS Code), see <https://docs.petoi.com/apis/python-api>.

1. **Demo**: At the front of the room, demo sending a command via Serial Protocol to the robot dog, such as making it sit down or stand up.
2. **Task**: Now, let the students explore. Provide each group with printed copies of the Serial Protocol documentation and ask them to control the robot dog themselves. A part of this exercise is getting them familiar with reading and understanding technical documentation, which is a fundamental part of programming. With the robot dog, they should perform the following actions:
   - Make the dog sit down. Command `ksit`.
   - Make it stand up. Command `kbalance`.
   - Make it perform a push-up. Command `kpu`.
   - Make it jump. Command `kjmp`.
   - Make it do a back flip. Command `kbf`.
   - Make it do a front flip. Command `kff`.
   - Make it rest (this is different from sitting). Command `krest`

### Talking Points

Deliver these while the students are working through the serial protocol activity.

- Explain that **this is the nitty-gritty of programming** – how computers used to be programmed before human-readable languages.
- Touch on the **importance of math** in working at this level.
- Highlight how some industries and companies, like **NASA, SpaceX, NVIDIA, AMD, Intel**, and **quantum computing, operating system development (Windows, Linux), electrical engineering, computer engineering, silicon engineering**, still rely on low-level programming today. They need to be that close to the computer, it's like driving stick shift if you're a NASCAR driver. You need complete control, not an automatic system abstracting away information from you.
- Emphasize that while most programming today isn't done at this level, **understanding it is crucial** to grasp how computers really work.
  
### Discussion

- Ask students to reflect on how manual this process feels. Was it easy or hard to understand the commands?
- Introduce the idea that there are easier ways to program, but the **foundation** of all computing lies here.
  
---

## Level 2: Python Coding – The Power of Modern Programming

### Objective

Transition from Serial Protocol to writing code in Python. Students will replicate the exact same actions they performed in Level 1, but using a **high-level language** that is readable and easier to work with.

### Introduction

- Start by discussing **modern programming** and how languages like Python make coding more accessible.
- If you're using it, introduce **Mind+** and explain that it's an Integrated Development Environment, or IDE. It's a tool we can use to write and test Python code specifically built for the Petoi Bittle Robot Dog.
- Mention that most of the software engineers working today use IDEs like **Visual Studio Code**.
- Explain the **compilation process** – how Python code must still be translated down into something the computer understands (binary, machine code), just like the serial commands.
  - **Python's process**: When you run Python code, it is first translated into **bytecode** (an intermediate form). This bytecode is then processed by the **Python Virtual Machine (PVM)**, which ultimately instructs the computer on what to do. While not as low-level as binary, there's still a translation step involved, similar to how serial protocol commands are understood by the robot dog.
  - **Examples of interpreted languages**:
    - **Python**: Translated into bytecode, then interpreted by the PVM.
    - **JavaScript**: Interpreted directly in web browsers or Node.js environments, running code line by line.
    - **Ruby**: Another interpreted language used in web development, processed by an interpreter at runtime.
    - **PHP**: Commonly used for server-side scripting, PHP code is interpreted when the server executes it.
  - **Hybrid languages** (compiled to bytecode and then interpreted or JIT-compiled):
    - **Java**: Compiled into **bytecode** first, which is then interpreted or **Just-in-Time (JIT) compiled** by the **Java Virtual Machine (JVM)** at runtime.
    - **C#**: Compiled into **Intermediate Language (IL)**, which is then executed by the **Common Language Runtime (CLR)**, similar to Java's JVM.
  - **How hybrid languages differ**: These languages fall between interpreted and compiled languages. The code is first compiled into an intermediate form (like bytecode), but instead of compiling all the way to machine code upfront (like in fully compiled languages such as **C** or **C++**), they rely on an interpreter or a **JIT compiler** to execute the bytecode at runtime. This allows for some benefits of interpreted languages (like flexibility and cross-platform execution) while still optimizing performance in certain scenarios.

### Hands-On Activity

1. **Task**: Ask students to write Python code to make the robot dog:
   - Sit down then wait 3 seconds.
   - Stand up then wait 3 seconds.
   - Perform a push-up then wait 3 seconds.
   - Jump then wait 3 seconds.
   - Do a back flip then wait 5 seconds.
   - Do a front flip then wait 5 seconds.
   - Rest then wait 1 second.
2. **Highlight the Power of Python**: Once the basic commands are done, encourage them to extend the task:
   - Make the commands **loop** a fixed number of times.
   - Add some **conditional logic** (e.g., if the dog's sensors detect an object, perform a different action).

The below is starter code to provide the students.

```python
from PetoiRobot import *

autoConnect() # Do not remove this.

# The sendSkillStr function sends a command to the robot dog to perform a skill.
# It takes two parameters:
# - The first parameter is the skill string (e.g., 'ksit') which tells the robot what to do.
# - The second parameter is the delay time in seconds (e.g., 3) which determines how long the robot will wait after performing the action.

# Write your code below! The first command has been written for you.

########## Student Code Area Start #################

# 1. Task: Make the dog sit down, then wait 3 seconds.
sendSkillStr('ksit', 3)

# 2. Task: Make the dog stand up, then wait 3 seconds. Put your code on the line below.


# 3. Task: Make the dog perform a push-up, then wait 3 seconds. Put your code on the line below.


# 4. Task: Make the dog jump, then wait 3 seconds. Put your code on the line below.


# 5. Task: Make the dog do a back flip, then wait 5 seconds. Put your code on the line below.


# 6. Task: Make the dog do a front flip, then wait 5 seconds. Put your code on the line below.


# 7. Task: Make the dog rest, then wait 1 second. Put your code on the line below.

########## Student Code Area End #################

closePort() # Do not remove this.
```

### Talking Points

Introduce these while the students are coding.

- Emphasize that this is where most **software development** happens today. In high level languages like Python.
- Mention that coding in languages like Python allows us to **add more complexity** – loops, variables, conditions – to what we did in Serial Protocol.
- Discuss how engineers at companies like **Microsoft, Google, Apple, Meta, and Amazon** use these kinds of languages daily to build apps, websites, and software. This is the skill set in-demand today, and as we'll explore in the next activity, remains relevant for the future with AI.
  
### Discussion

- Ask students to compare this experience with Level 1. Which was easier? What are the benefits of using a high-level language like Python?
- Guide them to see how **Python abstracts** many of the complexities we dealt with at the lower level, making programming faster and more efficient.

---

## Level 3: Prompt Engineering – The Future of Programming

### Objective

Introduce the concept of **Prompt Engineering** and explain how natural language can now be used to control machines through AI. This demonstrates the cutting edge of computing and how AI is making programming more intuitive.

### Introduction

- Explain that **Prompt Engineering** is a new and growing field where we use **natural language** to interact with machines and AI systems.
- Give a real-world analogy: When you ask someone to grab you a water, you don't tell them every step – where to walk, how to pick it up. They understand. AI works similarly now – it "gets what you mean."
- Highlight that while the AI seems to "know" what you want, **someone still had to write the code** behind the scenes to make this possible (that's you!). This is what makes us still relevant. It knows as much as we program it to understand. Without our input, it's not able to do much of anything valuable.

### Hands-On Activity

1. **Demo**: Show the students how you can prompt the AI in natural language to control the robot dog, e.g., "Make the robot walk forward."
2. **Task**: Let students create their own prompts:
   - Ask them to prompt the robot dog to perform various actions like walking, jumping, or sitting. Prompts should be delivered in the format `Make the robot dog do...` or `Make it do..` or some variations of that.
   - Have them complete the same set of tasks they issued via serial protocol and Python programming, but now using natural language. Namely, the following.
     - `Make the dog sit down.`
     - `Make it stand up.`
     - `Make it perform a push-up.`
     - `Make it jump.`
     - `Make it do a back flip.`
     - `Make it do a front flip.`
     - `Make it rest`
   - Encourage creativity: `Make it dance` or `Make it go crazy`.
   - When they deliver a prompt that results in no action, highlight that's because the code behind this system hasn't explained to AI how to achieve what you asked for. Someone still has to code it.
3. **Explain the AI's Role**: After they try out prompts, explain that **AI acts as their assistant**. While it makes things easier, it's only because **we programmed it** to understand those commands.

The code below maps natural language commands to Python that control the Petoi Bittle Robot Dog. Provide it in an IDE (Visual Studio Code) to students and have them run the program. It should result in a live console (terminal) window where they can type natural language and get reactions. You'll need an Open AI API key present in a `.ENV` file in the same directory as the Python script containing the code. You can get one at <https://platform.openai.com/api-keys>.

The students **should be writing natural language prompts, i.e. prompt engineering, not struggling through the setup of connecting natural language to the Petoi Bittle**. That setup should be done before hand.

```python
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
    
    Always, no matter what, return a syntactically correct Python list. Never return code fenced markdown or code blocks.
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
```

### Talking Points

Deliver these while the students are experimenting.

- Prompt Engineering allows us to **program without writing code**, but it's built on a deep understanding of how programming and machines work.
- Discuss how **AI is an assistant, not a replacement** for human intelligence.
- Highlight how we are still in control – the human knowledge behind coding is essential to teach AI.
- Make the connection that Serial Protocol is like driving stick shift, High-Level Programming Languages is like driving automatic, and AI-Assisted Programming is like Tesla's driver assistance tech that makes driving way easier, but still requires human oversight.
  
### Discussion

- Ask the students what they think about the future of programming – will AI replace coding, or just make it easier?
- Help them see the big picture: **All three levels** of programming are different ways of controlling the same machine, but each level abstracts complexity and makes the process easier.

---

## Conclusion

Wrap up the workshop by reflecting on the journey:

- **Level 1**: They controlled the robot dog at the lowest level using Serial Protocol.
- **Level 2**: They wrote Python code, showing how much easier modern programming can be.
- **Level 3**: They used natural language and AI, showing the future of programming.

Remind students that while **AI is powerful**, human intelligence and coding skills remain foundational. Encourage them to continue exploring programming, AI, and technology.
