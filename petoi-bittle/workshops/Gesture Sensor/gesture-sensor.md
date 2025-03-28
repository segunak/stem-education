# User Story: Robot Dog Gesture Commands

## Description

Using the Gesture Sensor extension, write a Python program that enables the robot dog to perform actions in response to physical gestures. The table below defines the gestures and associated actions that your program should include.

| Gesture              | Action      |
|----------------------|-------------|
| Swipe Up             | Front flip  |
| Swipe Down           | Back flip   |
| Swipe Left           | Handstand   |
| Swipe Right          | Play dead   |
| Swipe Up then Down   | Stretch     |
| Swipe Left then Right| Push up     |
| Palm                 | Hi          |
| Circular Motion      | Pee         |
| Clap                 | Cheer       |
| Fist                 | Boxing      |

Note: The blue highlighted cells are bonus gestures. There can be some variability with the gesture sensor. If you’re not able to get it working for the blue highlighted rows, that’s alright, but give it a try!

## Implementation Details

For more information about the gesture sensor, visit [Petoi Gesture Sensor Documentation](https://docs.petoi.com/extensible-modules/gesture-sensor).

## Example Code

Below is a sample code snippet to get you started with initializing and using the Gesture Sensor with the robot dog. You may need to adjust the code to fit the exact requirements of your sensor and robot dog.

```python
import os
import json
from PetoiRobot import *
from gesture_sensor import GestureSensor  # Assuming you have a module for the gesture sensor

autoConnect()

# Initialize the gesture sensor
gesture_sensor = GestureSensor()

# Define the gestures and corresponding commands
gesture_commands = {
    "Swipe Up": "kff",
    "Swipe Down": "kbf",
    "Swipe Left": "khds",
    "Swipe Right": "kpd",
    "Swipe Up then Down": "kstr",
    "Swipe Left then Right": "kpu",
    "Palm": "khi",
    "Circular Motion": "kpee",
    "Clap": "kchr",
    "Fist": "kbx"
}

def perform_action(gesture):
    command = gesture_commands.get(gesture)
    if command:
        sendSkillStr(command, 1)
    else:
        print("Gesture not recognized.")

try:
    print("Robot Dog Gesture Control Initialized.")
    
    while True:
        gesture = gesture_sensor.detect_gesture()
        if gesture:
            print(f"Detected Gesture: {gesture}")
            perform_action(gesture)
        
except KeyboardInterrupt:
    print("\nKeyboard interrupt received. Exiting...")
finally:
    closePort()
    print("Program terminated.")
    exit()
```

## Acceptance Criteria

### 1. Gesture Sensor Initialization

- **GIVEN:** The robot dog is equipped with the Gesture Sensor extension.
- **WHEN:** The team writes a Python program that correctly initializes and configures the Gesture Sensor.
- **THEN:** The Gesture Sensor is successfully initialized and ready to detect gestures.

### 2. Gesture Detection Implementation

- **GIVEN:** The Gesture Sensor is initialized and configured.
- **WHEN:** The team implements code to detect each specific gesture as described in the table.
- **THEN:** The program accurately detects each gesture from the Gesture Sensor.

### 3. Correct Action Execution

- **GIVEN:** The program detects gestures accurately.
- **WHEN:** The detected gestures correspond to the actions specified in the table.
- **THEN:** The robot dog performs the correct action for each detected gesture.
