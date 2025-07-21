# Petoi Bittle X Robot Arm Serial Protocol Commands

**Official Documentation**: <https://docs.petoi.com/extensible-modules/robot-arm>
*Please refer to the official documentation for the most up-to-date and authoritative information*

## Overview

The Bittle X robot arm (Bittle X+Arm) is an extensible module that adds gripper functionality to the Bittle quadruped robot. This robotic arm gripper enables more complex skills such as grabbing objects for display or moving them to different places. This document provides comprehensive coverage of all serial protocol commands for controlling the robot arm based on the official Petoi documentation.

## Safety Warning

⚠️ **DANGER**: When the robot arm is in motion, please do not put your hands between the robot claws to avoid being pinched.

## Prerequisites

- Bittle X with robot arm module installed (requires neck part with J-hook)
- Firmware uploaded with model "Bittle X+Arm" selected in Petoi Desktop App
- Proper joint calibration completed
- Serial connection established (USB or Bluetooth)
- Battery installed and powered on

## Joint Mapping

The robot arm uses the following joint indices:

- **Joint 0**: Base rotation (yaw/panning)
- **Joint 1**: Shoulder pitch (arm up/down)
- **Joint 2**: Gripper/claw (open/close)

## Skill-Based Commands (k prefix)

All skill commands must be prefixed with lowercase 'k' when sent via serial.

### Pick Commands

Pick up objects from different positions:

```txt
kpickF    - Pick up the object in front of the robotic arm
kpickL    - Pick up the object to the left of the robotic arm
kpickR    - Pick up the object to the right of the robotic arm
kpickD    - Pick up the object under the robotic arm
kpick     - Pick up object (randomly chooses a direction)
```

### Put Commands

Place grasped objects at different positions:

```txt
kputF     - Place the grasped object in front of the robotic arm
kputL     - Place the grasped object to the left of the robotic arm
kputR     - Place the grasped object to the right of the robotic arm
kputD     - Place the grasped object under the robotic arm
kput      - Place object (randomly chooses a direction)
```

### Drop Commands

Drop objects at different positions (based on skill table):

```txt
kdropF    - Drop object in front
kdropL    - Drop object to the left
kdropR    - Drop object to the right
kdropD    - Drop object down
kdrop     - Drop object (randomly chooses a direction)
```

### Toss/Launch Commands

Throw or launch grasped objects:

```txt
ktossF    - Throw the grasped object forward
ktossL    - Throw the grasped object to the left
ktossR    - Throw the grasped object to the right
ktoss     - Throw object (randomly chooses a direction)
klaunch   - Launch the grasped object forward (equivalent to ktossD)
```

### Special Action Commands

```txt
khunt     - Quickly grasp the object in front
kshowOff  - Show the grasped object
kclap     - Make a clapping motion with the robotic gripper
```

## Directional Command Matrix

| Skill Name | Front  | Left   | Right  | Down           |
|------------|--------|--------|--------|----------------|
| pick       | pickF  | pickL  | pickR  | pickD          |
| drop       | dropF  | dropL  | dropR  | dropD          |
| put        | putF   | putL   | putR   | putD           |
| toss       | tossF  | tossL  | tossR  | tossD = launch |
| hunt       | (front only) | - | -      | -              |
| showOff    | (no directional variants) | - | - | -        |
| clap       | (no directional variants) | - | - | -        |

**Important Notes**:

- Commands without directional suffixes (F/L/R/D) will randomly execute one of the four directional variants
- hunt, showOff, and clap commands do not have directional variants

## Calibration Commands

### Auto-Calibration for Gripper

```txt
c-2
```

This special command auto-calibrates the gripper/claw (joint index 2) using vibration feedback:

- Automatically finds the optimal closing position using IMU feedback
- Detects when gripper contacts objects
- Saves calibration values to EEPROM
- Can also be triggered via the "Auto" button in Petoi Desktop App

### Manual Calibration

```txt
c              - Enter general calibration mode
c[joint] [offset]  - Calibrate specific joint with offset
```

## Direct Joint Control Commands

### Move Commands (m prefix)

Control individual joints directly:

```txt
m[joint] [angle]
```

Examples:

```txt
m0 45          - Rotate base to 45 degrees
m1 90          - Move shoulder to 90 degrees
m2 30          - Set gripper to 30 degrees
m0 -30 1 60 2 120  - Move multiple joints sequentially
```

### Simultaneous Movement (i prefix)

Move multiple joints at the same time:

```txt
i[joint] [angle] [joint] [angle]...
```

Example:

```txt
i0 45 1 90 2 30    - Move all three arm joints simultaneously
```

## Voice Command Integration

The robot arm supports custom voice commands through the voice module. To use voice commands:

1. Say "**Start learning**" to activate custom voice command mode

2. Record the following commands in order:

| Voice Command       | Function                                              |
|-------------------|-------------------------------------------------------|
| Learn skill       | De-energizes servos for skill motion capture         |
| Play skill        | Plays back the captured skill motion                 |
| Follow           | De-energizes servos for leg mimicking                |
| Pick up          | Pick up the object                                   |
| Put it down      | Put the object down                                   |
| Hunt             | Grab the object quickly                              |
| Show off the object | Show off the object                                |
| Put away         | Put away the object                                   |
| Throw away       | Throw the object aside                                |
| Shoot           | Throw the object forward                              |

3. Say "**Stop learning**" to exit custom voice command mode

## Usage Examples

### Basic Pick and Place Operation

```txt
kup        # Stand up
kpickF     # Pick from front
kwkF       # Walk forward
kputD      # Put down
```

### Manual Gripper Control Sequence

```txt
m1 90      # Raise arm to 90 degrees
m2 -30     # Open gripper
m1 45      # Lower arm to object
m2 120     # Close gripper
m1 90      # Raise arm with object
```

### Calibrate and Test Gripper

```txt
c-2        # Auto-calibrate gripper
s          # Save calibration
m2 -30     # Test: open gripper
m2 120     # Test: close gripper
```

## System Commands

```txt
s          # Save calibration/settings to EEPROM
l          # List all available skills
gb         # Turn off gyro balance (useful during arm operations)
gB         # Turn on gyro balance
```

## Mind+ Integration

The robot arm skills can be controlled through Mind+ using the **Perform robot arm skill** block in the Petoi Coding Blocks. This provides a visual programming interface for arm control.

## Advanced Usage

### Creating Custom Skills

Custom arm skills can be created using:

- **Petoi Desktop App Skill Composer**: Visual skill creation and editing
- **Manual skill recording**: Use "Learn skill" and "Play skill" voice commands
- **Direct programming**: Modify source code for advanced control
- **Export options**: Skills can be exported to mobile app, Mind+ programs, or source code

### Extensional Applications

The robot arm can be combined with other sensors such as:

- Grove Vision AI V2 module for vision-based grasping
- Additional sensors for environmental awareness

Note: Sensor integration requires source code modifications (sample code pending from Petoi).

## Important Considerations

1. **Joint Limits**:
   - Each joint has specific angle limits to prevent damage
   - Stay within calibrated ranges for optimal performance

2. **Center of Mass**:
   - The arm weight affects robot balance
   - Firmware automatically adjusts for arm presence

3. **Power Management**:
   - Ensure battery is properly charged for arm operations
   - Arm movements may consume more power than standard gaits

4. **Calibration**:
   - Proper calibration prevents claw jamming and overheating
   - Use Petoi Desktop App for visual calibration interface
   - Save calibration after adjustments

5. **Command Format**:
   - All skill commands require lowercase 'k' prefix
   - Serial commands are case-sensitive
   - Commands can be sent via USB or Bluetooth connection

## Troubleshooting

- If arm doesn't respond, verify firmware is "Bittle X+Arm" version
- For imprecise movements, recalibrate joints
- If gripper jams, use auto-calibration (c-2) command
- Check battery level if movements are weak or erratic

For the latest updates and additional support, refer to the official documentation at <https://docs.petoi.com/extensible-modules/robot-arm>
