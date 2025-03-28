# User Story: Robot Dog Obstacle Course

## Overview

As students in the robotics workshop, you will create an obstacle course for the Petoi Bittle X Robot Dog using items found around the Microsoft Charlotte office. The robot dog must complete various skills as it traverses the course without losing its balance. The course should last a minimum of 2 minutes and include specific skills.

## Objective

Design and implement an obstacle course for the robot dog that includes performing specific skills at designated points. The course must last a minimum of 2 minutes from start to finish, and the robot dog must maintain its balance throughout.

## Background

In this workshop, you will learn the importance of precise programming and debugging, as well as how to create complex sequences of commands to control a robot. You will also learn about timing and how to ensure the robot dog performs actions smoothly without losing balance.

## Key Concepts

- **Commands:** Specific instructions that tell the robot dog what to do.
- **Timing:** Ensuring the robot dog performs actions with precise timing to avoid losing balance.
- **Debugging:** Identifying and fixing issues in the code to ensure smooth execution.
- **Obstacle Course Design:** Creating a course using everyday items and ensuring the robot dog can navigate it.

## Prerequisites

Before starting, ensure you have completed the previous workshops and are familiar with the following:

- Connecting to the robot dog using the `autoConnect()` function.
- Using the `sendSkillStr()` function to send commands to the robot dog.
- Basic knowledge of Python programming.

## Function to Use

You will primarily use the `sendSkillStr()` function to control the robot dog. Here is the function definition:

```python
def sendSkillStr(skillStr, delayTime):
    """
    Send a skill command to the robot dog.

    Parameters:
    skillStr (str): The command string for the skill.
    delayTime (int): The time to wait in seconds after the skill is performed.
    """
```

## Instructions

### Step 1: Design the Obstacle Course

1. Explore the Microsoft Charlotte office and identify items you can use to create obstacles for the robot dog.
2. Plan a course that will take the robot dog a minimum of 2 minutes to complete.
3. Include the following skills in the course:
   - At least 1 front flip.
   - At least 1 back flip.
   - At least 1 handstand.
   - At least 2 jumps.
   - At least 1 push-up.
4. Ensure the course is safe for the robot dog and won't cause any damage to office property.

### Step 2: Write the Code

1. **Connect to the Robot Dog:**
    ```python
    from PetoiRobot import *
    autoConnect()
    ```

2. **Control the Robot Dog:**
    Write a Python program that directs the robot dog through the obstacle course. Use the `sendSkillStr()` function to perform each skill at designated points in the course. Ensure the robot dog maintains its balance and stability throughout.

    Example code to perform a front flip:
    ```python
    sendSkillStr("kff", 1)
    ```

3. **Include Timing:**
    Ensure that the total time taken to complete the course is at least 2 minutes. You can achieve this by adjusting the delays between commands.

### Example Code

Here's a template to get you started. Modify it according to your obstacle course design:

```python
from PetoiRobot import *
import time

autoConnect()

# Start the obstacle course
start_time = time.time()

# Example sequence of commands
sendSkillStr("kup", 1)      # Stand up
sendSkillStr("kcrF", 5)     # Crawl forward for 5 seconds
sendSkillStr("kjmp", 1)     # Jump
sendSkillStr("kjmp", 1)     # Jump again
sendSkillStr("khds", 1)     # Handstand
sendSkillStr("kbf", 1)      # Back flip
sendSkillStr("kff", 1)      # Front flip
sendSkillStr("kpu", 1)      # Push up

# Ensure the course lasts at least 2 minutes
while time.time() - start_time < 120:
    sendSkillStr("kwkF", 1)  # Keep walking forward

# End of the obstacle course
sendSkillStr("krest", 1)  # Rest

closePort()
```

### Acceptance Criteria

The following criteria define success for this project. Your program must satisfy these criteria to be considered complete.

1. **Course Duration:**
    - The entire course should last a minimum of 2 minutes from start to finish.

2. **Perform Skills:**
    - The robot dog should perform at least 1 front flip, 1 back flip, 1 handstand, 2 jumps, and 1 push-up at designated points in the course without losing balance.

3. **Balance and Stability:**
    - The robot dog should maintain its balance and stability, not falling over during the performance of any skill.

4. **Obstacle Navigation:**
    - The course should include obstacles created from office items, which the robot dog must navigate without falling over.

## Conclusion

By the end of this workshop, you will have created a challenging obstacle course for the robot dog and learned how to control it through complex sequences of commands. Remember to ensure safety and have fun designing your course!
