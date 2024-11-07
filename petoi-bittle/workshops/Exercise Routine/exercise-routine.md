# User Story: Robot Dog Exercise Routine

## Overview

As students in the robotics workshop, you will create a detailed exercise routine for the robot dog to keep it in shape. This routine will consist of a series of exercises, including both simple and complex movements. Your task is to implement this routine, ensuring the robot dog maintains balance and performs each exercise correctly.

## Objective

Create an exercise routine for the robot dog that lasts a minimum of 2 minutes. The routine should include various exercises such as sitting, standing, stretching, flips, handstands, push-ups, jumps, and walking. Additionally, the robot dog should play a melody at the end of the routine.

## Background

In a software development team, multiple roles work together to build and deliver software products. Each member of the team has a specific role, but they all need to collaborate closely to achieve the common goal. Here are some common roles in a software development team:

- **Product Owner:** Responsible for defining the product vision and managing the product backlog.
- **Scrum Master:** Facilitates the team’s work and ensures that Agile practices are followed.
- **Developers:** Write the code to implement the features and fix bugs.
- **Testers:** Ensure the quality of the product by testing it thoroughly.
- **Designers:** Create the user interface and experience.

For this exercise, you will be working in groups, with each member taking on a specific role. Here are the roles and their responsibilities:

- **Lead Developer:** Writes the main code for the routine.
- **Assistant Developer:** Helps the lead programmer and writes supplementary code.
- **Tester:** Continuously runs the program to check for errors and ensure it meets the requirements.
- **Documenter:** Keeps track of what has been done, writes comments in the code, and ensures everyone understands the progress.
- **Project Manager:** Ensures the team is on track, keeps everyone organized, and makes sure all tasks are completed on time.

## Key Concepts

- **Commands:** Specific instructions that tell the robot dog what to do. Each command corresponds to a different movement or action.

## Prerequisites

Before starting the exercise routine, you need to prepare the robot dog by following these steps in your code:

1. **Connect the Ports:** Use the `autoConnect()` function to establish a connection between the computer and the robot dog. This ensures that you can send commands to the robot dog.

2. **Deactivate the Voice Module:** This will ensure the robot dog does not respond to voice commands during the exercise. Use the command `sendSkillStr("XAd 0", 1)`.

## Function to Use

You will primarily use the `sendSkillStr()` function to implement the exercise routine. Here is the function definition:

```python
def sendSkillStr(skillStr, delayTime):
    """
    Send a skill command to the robot dog.

    Parameters:
    skillStr (str): The command string for the skill.
    delayTime (int): The time to wait in seconds after the skill is performed.
    """
```

## Exercise Routine

Your task is to create a program that makes the robot dog perform the following exercises in sequence. Implement each item using the `sendSkillStr()` function and the respective command name. The program should be written in Python, not coding blocks.

1. **Sit Down:** The robot dog should sit down. Use the command `ksit` and wait for 1 second.
2. **Stand Up:** The robot dog should stand up. Use the command `kup` and wait for 1 second.
3. **Stretch:** The robot dog should stretch. Use the command `kstr` and wait for 1 second.
4. **Front Flip:** The robot dog should perform a front flip. Use the command `kff` and wait for 1 second.
5. **Back Flip:** The robot dog should perform a back flip. Use the command `kbf` and wait for 1 second.
6. **Handstand:** The robot dog should perform a handstand. Use the command `khds` and wait for 1 second.
7. **Continuous Jumping:** The robot dog should perform 5 consecutive executions of the jump action. Use the command `kjmp` and wait for .5 seconds between each jump.
8. **Continuous Push-Ups:** The robot dog should perform 5 executions of the push up action. Use the command `kpu` and wait for .5 seconds per iteration.
9. **Continuous Boxing:** The robot dog should perform 10 executions of the boxing action. Use the command `kbx` and wait for .3 seconds per iteration.
10. **Continuous Front Flips:** The robot dog should perform 3 continuous front flips waiting for 3 seconds after each. Use the command `kff`.
11. **Continuous Back Flips:** The robot dog should perform 3 continuous back flips waiting for 3 seconds after each. Use the command `kbf`.
12. **Pee:** The robot dog should perform the pee action. All that working out will have it ready to go. Use the command `kpee` and wait for 1 second.
13. **Play Dead:** The robot dog should play dead. Use the command `kpd` and wait for 1 second.
14. **Rest:** The robot dog should rest. Use the command `krest` and wait for 1 second.
15. **Play Melodies:** The robot dog should play the 3 melodies provided in the starter code for this user story. After playing a melody, the program should wait 5 seconds before playing the next one. You need only call the functions for each of the melodies, named `playMelody1()`, `playMelody2()`, and `playMelody3()`. After playing the melodies, try and guess what popular folks/cultural songs each is!

## Acceptance Criteria

The following criteria define success for this project. Your program must satisfy this acceptance criteria to be considered complete. Read them carefully!

### 1. Sit Down

- **GIVEN:** The robot dog is ready.
- **WHEN:** The command `ksit` is issued.
- **THEN:** The robot dog should sit down and wait for 1 second.

### 2. Stand Up

- **GIVEN:** The robot dog is sitting.
- **WHEN:** The command `kup` is issued.
- **THEN:** The robot dog should stand up and wait for 1 second.

### 3. Stretch

- **GIVEN:** The robot dog is standing.
- **WHEN:** The command `kstr` is issued.
- **THEN:** The robot dog should stretch and wait for 1 second.

### 4. Front Flip

- **GIVEN:** The robot dog is stretched.
- **WHEN:** The command `kff` is issued.
- **THEN:** The robot dog should perform a front flip and wait for 1 second.

### 5. Back Flip

- **GIVEN:** The robot dog has completed a front flip.
- **WHEN:** The command `kbf` is issued.
- **THEN:** The robot dog should perform a back flip and wait for 1 second.

### 6. Handstand

- **GIVEN:** The robot dog has completed a back flip.
- **WHEN:** The command `khds` is issued.
- **THEN:** The robot dog should perform a handstand and wait for 1 second.

### 7. Continuous Jumping

- **GIVEN:** The robot dog has completed a handstand.
- **WHEN:** The command `kjmp` is issued.
- **THEN:** The robot dog should perform 5 jumps, waiting 0.5 seconds between each jump.

### 8. Continuous Push Ups

- **GIVEN:** The robot dog has completed the jumps.
- **WHEN:** The command `kpu` is issued.
- **THEN:** The robot dog should perform 5 push-ups, waiting 0.5 seconds between each push-up.

### 9. Continuous Boxing

- **GIVEN:** The robot dog has completed the push-ups.
- **WHEN:** The command `kbx` is issued.
- **THEN:** The robot dog should perform 10 boxing actions, waiting 0.3 seconds between each.

### 10. Continuous Front Flips

- **GIVEN:** The robot dog has completed the boxing.
- **WHEN:** The command `kff` is issued.
- **THEN:** The robot dog should perform 3 continuous front flips waiting 3 seconds between each.

### 11. Continuous Back Flips

- **GIVEN:** The robot dog has completed the front flips.
- **WHEN:** The command `kbf` is issued.
- **THEN:** The robot dog should perform 3 continuous back flips waiting 3 seconds between each.

### 12. Pee

- **GIVEN:** The robot dog has completed the back flips.
- **WHEN:** The command `kpee` is issued.
- **THEN:** The robot dog should perform the pee action and wait for 1 second.

### 13. Play Dead

- **GIVEN:** The robot dog has completed the pee action.
- **WHEN:** The command `kpd` is issued.
- **THEN:** The robot dog should play dead and wait for 1 second.

### 14. Rest

- **GIVEN:** The robot dog has played dead.
- **WHEN:** The command `krest` is issued.
- **THEN:** The robot dog should rest and wait for 1 second.

### 15. Play Melodies

- **GIVEN:** The robot dog has completed the rest.
- **WHEN:** The play melody functions are called.
- **THEN:** The robot dog should play each of the three melodies with a 5-second pause in between.

## Reference Code

This code is to get you started. Write your own code in between the labelled student code blocks.

```python
import time
from PetoiRobot import *

# Function to play a folk song abbreviated TTLS.
def playMelody1():
    play('b', [
        14, 8, 14, 8, 21, 8, 21, 8, 23, 8, 23, 8, 21, 4,
        19, 8, 19, 8, 18, 8, 18, 8, 16, 8, 16, 8, 14, 4,
        21, 8, 21, 8, 19, 8, 19, 8, 18, 8, 18, 8, 16, 4,
        21, 8, 21, 8, 19, 8, 19, 8, 18, 8, 18, 8, 16, 4,
        14, 8, 14, 8, 21, 8, 21, 8, 23, 8, 23, 8, 21, 4,
        19, 8, 19, 8, 18, 8, 18, 8, 16, 8, 16, 8, 14, 4
    ], 0)

# Function to play a classic song used on certain joyous occasions.
def playMelody2():
    play('b', [
        15, 8, 15, 4, 17, 4, 15, 4, 20, 4, 19, 8,
        15, 8, 15, 4, 17, 4, 15, 4, 22, 4, 20, 8,
        15, 8, 15, 4, 29, 4, 24, 4, 20, 4, 19, 4, 17, 8,
        26, 8, 26, 4, 24, 4, 20, 4, 22, 4, 20, 8
    ], 0)

# Function to play a classical song by a famous composer (probably won't sound accurate)
def playMelody3():
    play(
        'b',
        [
            24, 4, 23, 4, 24, 4, 23, 4, 24, 4, 19, 4, 21, 4, 23, 4,
            0, 4, 14, 4, 16, 4, 18, 4, 19, 4, 18, 4, 16, 4, 14, 4, 0, 4,
            24, 4, 23, 4, 24, 4, 23, 4, 24, 4, 19, 4, 21, 4, 23, 4,
            0, 4, 14, 4, 16, 4, 18, 4, 19, 4, 18, 4, 16, 4, 14, 4
        ],
        2
    )

def playBonusMelody():
    play('b', [
        21, 4, 19, 4, 18, 4, 19, 4, 21, 4, 21, 4, 21, 4, 
        19, 4, 19, 4, 19, 4, 21, 4, 24, 4, 24, 4, 
        21, 4, 19, 4, 18, 4, 19, 4, 21, 4, 21, 4, 21, 4, 
        21, 4, 19, 4, 19, 4, 21, 4, 19, 4, 18, 4
    ], 0)

# Connect the computer to the input ports on the dog, either over Bluetooth or a hardwired connection.
autoConnect()

# Deactivate the voice module so the robot doesn't do random things in response to voices in the room.
sendCmdStr("XAd", 0);

# To get started, the command sit is provided with a 0.2 second wait (delay) after execution. Write the rest of your code below.
sendSkillStr('ksit', 1)

######## START STUDENT CODE AREA ########


######### END STUDENT CODE AREA ########

# Close the ports. Like closing up the shop before ending work for the day. This frees up the connection between the computer
# and the software on the robot dog.
closePort()
```

## Conclusion

By the end of this exercise, you will have created a detailed exercise routine for the robot dog, ensuring it performs each movement correctly and maintains balance throughout the routine. Remember to work together as a team, ask questions for clarity, and continuously run your program to check your work. Here's some code to get you started.
