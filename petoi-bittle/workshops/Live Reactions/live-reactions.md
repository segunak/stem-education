# User Story: Robot Dog Live Reactions

## Overview

As students in the robotics workshop, your goal is to bring the robot dog to life with a program that continuously runs and reacts to user inputs. Unlike previous exercises where the program executes a predefined routine and then stops, this challenge requires your code to run indefinitely, accepting and responding to commands in real-time.

## Objective

Create a program that enables the robot dog to react to live user input continuously. The program should accept a variety of commands that instruct the robot dog to perform different actions or movements. The commands can be entered one at a time or as a series of commands separated by commas.

## Background

In the real world, many programs are designed to run continuously, responding to various inputs and events over time. This could be anything from a web server handling requests to an application reacting to user inputs. In this exercise, you will simulate this continuous operation by writing a Python program that keeps the robot dog responsive and active based on live user input.

## Key Concepts

- **Continuous Execution:** Writing a program that runs indefinitely until a specific condition (like a user command) is met.
- **Real-time Input Handling:** Accepting and processing user inputs while the program is running.
- **Command Parsing:** Interpreting user inputs to execute the corresponding actions on the robot dog.

## Prerequisites

Before starting the live reactions program, you need to prepare the robot dog by following these steps in your code:

1. **Connect the Ports:** Use the `autoConnect()` function to establish a connection between the computer and the robot dog. This ensures that you can send commands to the robot dog.

2. **Close the Ports:** The last thing in your program should close the connection between the robot dog and the computer, ensuring that all is in place for the next run.  will ensure the robot dog does not respond to voice commands during the exercise. Use the command `closePort()`.

## Function to Use

You will primarily use the `sendSkillStr()` function to implement the live reactions. Here is the function definition:

```python
def sendSkillStr(skillStr, delayTime):
    """
    Send a skill command to the robot dog.

    Parameters:
    skillStr (str): The command string for the skill.
    delayTime (int): The time to wait in seconds after the skill is performed.
    """
```

## Example Code to Get Started

This example code will help you get started. Your task is to expand it to handle a variety of commands and make the program continuously run.

```python
import time
from PetoiRobot import *

autoConnect()

try:
    print("""Welcome! You may use this terminal to control the Petoi "Bittle X" Robot Dog.
You can enter a single command, or a series of commands separated by commas.
    """)

    ######## Student Code Area Start ##################

    # Hint: Start by figuring out how to read input from the console in Python.
    # Remember to handle different cases (e.g., upper and lower case letters).
    # Research the `input()` function and string methods like `.strip()` and `.lower()`.

    # Hint: Think about how you can make the program run forever without stopping.
    # Research loops that run indefinitely until a certain condition is met.
    # Look into `while True` loops and how to safely exit them.

    # Hint: You will need to split the input if it contains multiple commands separated by commas.
    # Research how to split a string into a list of substrings.
    # Look into the `split()` method for strings.

    # Hint: Think about how you can handle needing to parse many conditions in Python.
    # This is an area where there is more than one way to solve a problem, some being more efficient
    # or easier to maintain (read) than others. Do some research and choose a method that works best for you.
    # Consider exploring both `if-elif` statements and dictionaries/maps.

    # Hint: Don't forget to add a way to exit the loop when the user types 'exit'.
    # Research how to break out of a loop based on a condition.

    # Hint: Once you've figured out how to interpret and process commands, think about how you will execute the corresponding
    # actions on the robot dog. Look into how you can use the `sendSkillStr` function.

    ######## Student Code Area End ##################
except KeyboardInterrupt:
    print("\nKeyboard interrupt received. Exiting...")
finally:
    closePort()
    print("Program terminated.")
```

## Acceptance Criteria

To successfully complete this challenge, your program must meet the following criteria:

### 1. Continuous Execution

- **GIVEN:** The robot dog is ready.
- **WHEN:** The program starts.
- **THEN:** The program should run continuously, accepting and processing user inputs.

### 2. Command Handling

- **GIVEN:** The user enters a command.
- **WHEN:** The command is received.
- **THEN:** The robot dog should execute the corresponding action.

### 3. Multiple Commands

- **GIVEN:** The user enters multiple commands separated by commas.
- **WHEN:** The commands are received.
- **THEN:** The robot dog should execute each action in sequence.

### 4. Exit Condition

- **GIVEN:** The user types 'exit'.
- **WHEN:** The command is received.
- **THEN:** The program should safely exit.

### 5. Implement at least 10 different commands

- **GIVEN:** The program is running.
- **WHEN:** The user enters commands.
- **THEN:** The program should be able to handle at least 10 different commands from the list provided below.

### 6. Bonus: Implement all 40 commands

- **GIVEN:** The program is running.
- **WHEN:** The user enters commands.
- **THEN:** The program should be able to handle all 40 commands from the list provided below.

## List of Commands

Here are the available commands you can implement for the robot dog:

1. **Sit**: `ksit`
   - **Description**: Makes the robot sit down.
   - **Example**: `sendSkillStr("ksit", 500)`

2. **Stand Up**: `kup`
   - **Description**: Makes the robot stand up.
   - **Example**: `sendSkillStr("kup", 500)`

3. **Bottom Up**: `kbuttUp`
   - **Description**: Raises the robot's bottom.
   - **Example**: `sendSkillStr("kbuttUp", 500)`

4. **Stretch**: `kstr`
   - **Description**: Stretches the robot.
   - **Example**: `sendSkillStr("kstr", 500)`

5. **Rest**: `krest`
   - **Description**: Puts the robot in a resting position.
   - **Example**: `sendSkillStr("krest", 500)`

6. **Zero**: `kzero`
   - **Description**: Resets the robot to its default position.
   - **Example**: `sendSkillStr("kzero", 500)`

7. **Boxing**: `kbx`
   - **Description**: Makes the robot perform boxing movements.
   - **Example**: `sendSkillStr("kbx", 500)`

8. **Cheer**: `kchr`
   - **Description**: Makes the robot cheer.
   - **Example**: `sendSkillStr("kchr", 500)`

9. **Check Around**: `kck`
   - **Description**: Makes the robot check its surroundings.
   - **Example**: `sendSkillStr("kck", 500)`

10. **Dig**: `kdg`
    - **Description**: Makes the robot dig.
    - **Example**: `sendSkillStr("kdg", 500)`

11. **Stand on Hands**: `khds`
    - **Description**: Makes the robot stand on its hands.
    - **Example**: `sendSkillStr("khds", 500)`

12. **Hug**: `khg`
    - **Description**: Makes the robot give a hug.
    - **Example**: `sendSkillStr("khg", 500)`

13. **Hi**: `khi`
    - **Description**: Makes the robot wave hello.
    - **Example**: `sendSkillStr("khi", 500)`

14. **Hands Up**: `khu`
    - **Description**: Makes the robot raise its hands.
    - **Example**: `sendSkillStr("khu", 500)`

15. **Jump**: `kjmp`
    - **Description**: Makes the robot jump.
    - **Example**: `sendSkillStr("kjmp", 500)`

16. **Kick**: `kkc`
    - **Description**: Makes the robot kick.
    - **Example**: `sendSkillStr("kkc", 500)`

17. **Nod**: `knd`
    - **Description**: Makes the robot nod.
    - **Example**: `sendSkillStr("knd", 500)`

18. **Play Dead**: `kpd`
    - **Description**: Makes the robot play dead.
    - **Example**: `sendSkillStr("kpd", 500)`

19. **Pee**: `kpee`
    - **Description**: Makes the robot simulate peeing.
    - **Example**: `sendSkillStr("kpee", 500)`

20. **Push Up**: `kpu`
    - **Description**: Makes the robot do push-ups.
    - **Example**: `sendSkillStr("kpu", 500)`

21. **Scratch**: `kscrh`
    - **Description**: Makes the robot scratch.
    - **Example**: `sendSkillStr("kscrh", 500)`

22. **Sniff**: `ksnf`
    - **Description**: Makes the robot sniff.
    - **Example**: `sendSkillStr("ksnf", 500)`

23. **Stepping**: `kvtF`
    - **Description**: Makes the robot perform a stepping movement.
    - **Example**: `sendSkillStr("kvtF", 500)`

24. **Crawl Forward**: `kcrF`
    - **Description**: Makes the robot crawl forward.
    - **Example**: `sendSkillStr("kcrF", 500)`

25. **Crawl Left**: `kcrL`
    - **Description**: Makes the robot crawl to the left.
    - **Example**: `sendSkillStr("kcrL", 500)`

26. **Crawl Right**: `kcrR`
    - **Description**: Makes the robot crawl to the right.
    - **Example**: `sendSkillStr("kcrR", 500)`

27. **Push Forward**: `kphF`
    - **Description**: Makes the robot push forward.
    - **Example**: `sendSkillStr("kphF", 500)`

28. **Push Left**: `kphL`
    - **Description**: Makes the robot push to the left.
    - **Example**: `sendSkillStr("kphL", 500)`

29. **Push Right**: `kphR`
    - **Description**: Makes the robot push to the right.
    - **Example**: `sendSkillStr("kphR", 500)`

30. **Walk Forward**: `kwkF`
    - **Description**: Makes the robot walk forward.
    - **Example**: `sendSkillStr("kwkF", 500)`

31. **Walk Left**: `kwkL`
    - **Description**: Makes the robot walk to the left.
    - **Example**: `sendSkillStr("kwkL", 500)`

32. **Walk Right**: `kwkR`
    - **Description**: Makes the robot walk to the right.
    - **Example**: `sendSkillStr("kwkR", 500)`

33. **Back**: `kbk`
    - **Description**: Makes the robot move backward.
    - **Example**: `sendSkillStr("kbk", 500)`

34. **Back Left**: `kbkL`
    - **Description**: Makes the robot move backward to the left.
    - **Example**: `sendSkillStr("kbkL", 500)`

35. **Back Right**: `kbkR`
    - **Description**: Makes the robot move backward to the right.
    - **Example**: `sendSkillStr("kbkR", 500)`

36. **Trot Forward**: `ktrF`
    - **Description**: Makes the robot trot forward.
    - **Example**: `sendSkillStr("ktrF", 500)`

37. **Trot Left**: `ktrL`
    - **Description**: Makes the robot trot to the left.
    - **Example**: `sendSkillStr("ktrL", 500)`

38. **Trot Right**: `ktrR`
    - **Description**: Makes the robot trot to the right.
    - **Example**: `sendSkillStr("ktrR", 500)`

39. **Back Flip**: `kbf`
    - **Description**: Makes the robot perform a backflip.
    - **Example**: `sendSkillStr("kbf", 500)`

40. **Front Flip**: `kff`
    - **Description**: Makes the robot perform a front flip.
    - **Example**: `sendSkillStr("kff", 500)`

## Conclusion

By the end of this exercise, you will have created a program that continuously runs and enables the robot dog to react to live user input. This exercise will help you understand how to create real-world applications that run indefinitely, responding to user inputs and events dynamically. Remember to work together, ask questions for clarity, and continuously test your program to ensure it meets the acceptance criteria. Good luck!
