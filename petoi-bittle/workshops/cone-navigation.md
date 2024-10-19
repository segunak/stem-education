# User Story: Robot Dog Cone Weaving

## Description

Write a Python program that directs the robot dog as it weaves through a line of 5 cones spaced at regular intervals. Each cone will be placed 12 inches apart.

## Implementation Details

The dog will start with its front feet behind a start line. The time will begin when the dog moves. The dog will move to the first cone and go around it on the right. The dog will then move to the left of the second cone and so on until it reaches the 5th cone. After the 5th cone it will cross the finish line. The time stops when a foot crosses the finish line. Your goal is both speed and accuracy. The dog should traverse the cones without touching them but should also move as fast as possible.

## Example Code

Below is a sample code snippet to get you started with directing the robot dog to weave through the cones. You may need to adjust the code to fit the exact requirements of your course setup and robot dog capabilities.

```python
import os
import time
from PetoiRobot import *

autoConnect()

# Define the weaving pattern
weave_pattern = [
    ("right", 12),  # Move to the right of the first cone
    ("left", 12),   # Move to the left of the second cone
    ("right", 12),  # Move to the right of the third cone
    ("left", 12),   # Move to the left of the fourth cone
    ("right", 12)   # Move to the right of the fifth cone
]

def move_robot(direction, distance):
    # Replace with the appropriate skill command and delay for moving the robot
    if direction == "right":
        sendSkillStr("kwkR", 1)  # Example command for moving right
    elif direction == "left":
        sendSkillStr("kwkL", 1)  # Example command for moving left
    time.sleep(distance / 12)  # Adjust sleep time based on distance

try:
    print("Robot Dog Cone Weaving Initialized.")

    # Position the robot at the start line
    sendSkillStr("kzero", 1)
    time.sleep(1)

    # Start the timer
    start_time = time.time()

    # Execute the weaving pattern
    for direction, distance in weave_pattern:
        move_robot(direction, distance)

    # Finish line crossing
    sendSkillStr("kwkF", 1)  # Move forward to cross the finish line

    # Stop the timer
    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"Course completed in {elapsed_time:.2f} seconds.")

except KeyboardInterrupt:
    print("\nKeyboard interrupt received. Exiting...")
finally:
    closePort()
    print("Program terminated.")
    exit()
```

## Acceptance Criteria

### 1. Timer Initialization

- **GIVEN:** The robot dog is positioned with its front feet behind the start line.
- **WHEN:** The Python program begins execution.
- **THEN:** The timer should start as soon as the robot dog begins to move and stop when at least 1 leg of the robot dog crosses the finish line.

### 2. First Cone Navigation

- **GIVEN:** The robot dog has started moving.
- **WHEN:** The robot dog reaches the first cone.
- **THEN:** The dog should navigate around the first cone on the right without touching it.

### 3. Subsequent Cone Navigation

- **GIVEN:** The robot dog has navigated around the first cone.
- **WHEN:** The robot dog reaches each subsequent cone.
- **THEN:** The dog should alternate its navigation around the cones (right of the first cone, left of the second cone, right of the third cone, left of the fourth cone, right of the fifth cone) without touching them.

### 4. Speed and Accuracy

- **GIVEN:** The robot dog is moving through the course.
- **WHEN:** The robot dog is weaving through the cones.
- **THEN:** The robot dog should complete the course as quickly as possible without touching any of the cones.
