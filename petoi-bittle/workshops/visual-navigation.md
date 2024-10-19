# User Story: Robot Dog Visual Navigation

## Description

Using the Intelligent Camera Module, write a Python program that enables the robot dog to follow a tennis ball around.

## Example Code

Below is a sample code snippet to get you started with enabling the robot dog to follow a tennis ball using the Intelligent Camera Module. You may need to adjust the code to fit the exact requirements of your setup and robot dog capabilities.

```python
import time
from PetoiRobot import *
from IntelligentCameraModule import *

autoConnect()

# Initialize camera module
camera = IntelligentCameraModule()

def locate_tennis_ball():
    # Replace with actual logic to detect tennis ball
    return camera.detect_object('tennis_ball')

def follow_tennis_ball():
    while True:
        ball_position = locate_tennis_ball()
        if ball_position is not None:
            # Adjust direction based on ball position
            if ball_position == 'left':
                sendSkillStr("kwkL", 1)  # Move left
            elif ball_position == 'right':
                sendSkillStr("kwkR", 1)  # Move right
            elif ball_position == 'center':
                sendSkillStr("kwkF", 1)  # Move forward
        else:
            # If the ball is not detected, scan surroundings
            sendSkillStr("kck", 1)  # Check around
        time.sleep(1)

try:
    print("Robot Dog Visual Navigation Initialized.")
    follow_tennis_ball()

except KeyboardInterrupt:
    print("\nKeyboard interrupt received. Exiting...")
finally:
    closePort()
    print("Program terminated.")
    exit()
```

## Acceptance Criteria

### 1. Autonomous Tracking

- **GIVEN:** The robot dog is using the Intelligent Camera Module.
- **WHEN:** The Python program is initiated.
- **THEN:** The robot dog should be able to identify and track the tennis ball autonomously without manual intervention.

### 2. Tennis Ball Detection and Following

- **GIVEN:** The Intelligent Camera Module is properly connected and the Python program is running.
- **WHEN:** The robot dog’s camera detects a tennis ball within its field of view.
- **THEN:** The robot dog should begin to follow the tennis ball, adjusting its direction as the ball moves.

### 3. Lost Object Recovery

- **GIVEN:** The robot dog is following a tennis ball.
- **WHEN:** The tennis ball moves out of the camera's field of view.
- **THEN:** The robot dog should stop and scan its surroundings to relocate the tennis ball.
