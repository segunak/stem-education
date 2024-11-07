# User Story: Robot Dog Infrared Navigation

## Description

Using the Infrared (IR) Distance Sensor, write a Python program that enables the robot dog to navigate an obstacle course autonomously. That is, the robot dog should be—via the IR Distance Sensor—capable of avoiding obstacles, reaching the end of the course without manual intervention. You will be responsible for designing the obstacle course, which must include at least 4 right-angle turns. You are free to use your general surroundings as a part of your course (for example, navigating the layout of a conference room).

## Example Code

Below is a sample code snippet to get you started with enabling the robot dog to navigate using the IR Distance Sensor. You may need to adjust the code to fit the exact requirements of your course setup and robot dog capabilities.

```python
import time
from PetoiRobot import *

autoConnect()

# Define distance threshold for obstacle detection (in cm)
DISTANCE_THRESHOLD = 20

def read_ir_sensor():
    # Replace with actual IR sensor reading logic
    return readUltrasonicDistance(triggerPin=8, echoPin=9)

def avoid_obstacle():
    sendSkillStr("kbk", 1)  # Move back
    time.sleep(1)
    sendSkillStr("kwkL", 1)  # Turn left
    time.sleep(1)

def navigate_course():
    while True:
        distance = read_ir_sensor()
        if distance < DISTANCE_THRESHOLD:
            avoid_obstacle()
        else:
            sendSkillStr("kwkF", 1)  # Move forward
            time.sleep(1)

try:
    print("Robot Dog Infrared Navigation Initialized.")
    navigate_course()

except KeyboardInterrupt:
    print("\nKeyboard interrupt received. Exiting...")
finally:
    closePort()
    print("Program terminated.")
    exit()
```

## Acceptance Criteria

### 1. Obstacle Detection and Avoidance

- **GIVEN:** The Infrared (IR) Distance Sensor is properly connected and the Python program is running.
- **WHEN:** The robot dog encounters an obstacle within the detection range of the IR Distance Sensor.
- **THEN:** The robot dog should stop and adjust its path to avoid the obstacle.

### 2. Right-Angle Turn Navigation

- **GIVEN:** The obstacle course includes at least 4 right-angle turns.
- **WHEN:** The robot dog reaches a right-angle turn.
- **THEN:** The robot dog should successfully navigate the turn without colliding with any obstacles.

### 3. Path Adjustment

- **GIVEN:** The robot dog is navigating the obstacle course.
- **WHEN:** The robot dog encounters a dead end or an unavoidable obstacle.
- **THEN:** The robot dog should reverse or adjust its path to find an alternate route.

### 4. Resuming Forward Movement

- **GIVEN:** The robot dog is actively using the IR Distance Sensor.
- **WHEN:** An obstacle is no longer detected in its path.
- **THEN:** The robot dog should resume its forward movement.
