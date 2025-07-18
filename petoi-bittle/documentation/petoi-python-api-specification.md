# Petoi Bittle Robot Dog - Python API Technical Specification

## Overview

This document provides the complete technical specification for controlling the Petoi Bittle Robot Dog using Python.

The official version is at <https://docs.petoi.com/apis/python-api>. This version was created for easy markdown use for workshops.

## Quick Start

```python
from Petoi import *

# Connect to robot
autoConnect()

# Send skill commands
sendSkillStr("ksit", 1)  # Make robot sit
sendSkillStr("kup", 1)   # Make robot stand
sendSkillStr("krest", 1)   # Make robot rest. This must always be the final command

# Always close connection when done
closePort()
```

## Core Functions

### Connection Management

**`autoConnect()`**

- Automatically detects and connects to the robot
- Must be called before sending any commands
- Handles port detection and communication setup

**`openPort(port)`**

- Manually connect to a specific port
- Parameter: `port` (string) - Port identifier (e.g., "COM3", "/dev/ttyUSB0")

**`closePort()`**

- Closes all serial connections
- Always call when finished to free resources

### Skill Control

**`sendSkillStr(skillStr, delayTime)`**

- Primary function for robot control
- Parameters:
  - `skillStr` (string): Command from skill reference table
  - `delayTime` (int): Delay in seconds after command before accepting next command
- Example: `sendSkillStr("kwkF", 2)` - Walk forward with 2-second delay

**`sendCmdStr(cmdStr, delayTime)`**

- Send raw command strings to robot. This should not ever be used by automated AI systems.
- Parameters:
  - `cmdStr` (string): Raw command string
  - `delayTime` (int): Delay in seconds
- Use for commands not in skill reference

### Advanced Control

**`loadSkill(fileName, delayTime)`**

- Load and execute custom skill files
- Parameters:
  - `fileName` (string): Skill file name (.md format)
  - `delayTime` (int): Delay in seconds

**`sendLongCmd(token, var, delayTime)`**

- Send complex commands with multiple parameters
- Parameters:
  - `token` (string): Command token
  - `var` (list): List of integer parameters
  - `delayTime` (int): Delay in seconds

### Sensor Reading

**`readAnalogValue(pin)`**

- Read analog sensor value
- Parameter: `pin` (int) - Pin number
- Returns: Integer value

**`readDigitalValue(pin)`**

- Read digital sensor value
- Parameter: `pin` (int) - Pin number
- Returns: Integer value (0 or 1)

**`readUltrasonicDistance(triggerPin, echoPin)`**

- Read ultrasonic distance sensor
- Parameters:
  - `triggerPin` (int): Trigger pin number
  - `echoPin` (int): Echo pin number
- Returns: Distance in centimeters

### Joint Control

**`getAngle(index)`**

- Get current angle of specific joint
- Parameter: `index` (int) - Joint index
- Returns: Current angle in degrees

**`getAngleList()`**

- Get angles of all joints
- Returns: List of current joint angles

**`rotateJoints(token, var, delayTime)`**

- Rotate specific joints to absolute positions
- Parameters:
  - `token` (string): Joint command token
  - `var` (list): List of (joint_index, angle) tuples
  - `delayTime` (int): Delay in seconds

### Output Control

**`writeAnalogValue(pin, val)`**

- Write analog value to pin
- Parameters:
  - `pin` (int): Pin number
  - `val` (int): Value to write

**`writeDigitalValue(pin, val)`**

- Write digital value to pin
- Parameters:
  - `pin` (int): Pin number
  - `val` (int): Value to write (0 or 1)

## Complete Skill Reference

### Basic Postures

| Command | Action | Description |
|---------|--------|-------------|
| `ksit` | Sit | Makes the robot sit down |
| `kup` | Stand Up | Makes the robot stand up |
| `krest` | Rest | Puts the robot in resting position |
| `kzero` | Zero | Resets robot to default position |
| `kbalance` | Balance | Makes the robot stand up neutral |
| `kstr` | Stretch | Stretches the robot |
| `kbuttUp` | Bottom Up | Raises the robot's bottom |
| `kcalib` | Calibration | Puts robot in calibration pose |

### Movement Commands

| Command | Action | Description |
|---------|--------|-------------|
| `kwkF` | Walk Forward | Makes the robot walk forward |
| `kwkL` | Walk Left | Makes the robot walk to the left |
| `kwkR` | Walk Right | Makes the robot walk to the right |
| `kbk` | Back | Makes the robot move backward |
| `kbkL` | Back Left | Makes the robot move backward to the left |
| `kbkR` | Back Right | Makes the robot move backward to the right |
| `ktrF` | Trot Forward | Makes the robot trot forward |
| `ktrL` | Trot Left | Makes the robot trot to the left |
| `ktrR` | Trot Right | Makes the robot trot to the right |
| `kcrF` | Crawl Forward | Makes the robot crawl forward |
| `kcrL` | Crawl Left | Makes the robot crawl to the left |
| `kcrR` | Crawl Right | Makes the robot crawl to the right |
| `kbdF` | Bound Forward | Makes the robot bound forward |
| `kjpF` | Jump Forward | Makes the robot jump forward |
| `kvtF` | Stepping | Makes the robot perform stepping movement |
| `kvtL` | Spin Left | Makes the robot spin to the left |
| `kmw` | Moon Walk | Makes the robot perform the moonwalk |

### Tricks and Actions

| Command | Action | Description |
|---------|--------|-------------|
| `kbf` | Back Flip | Makes the robot perform a backflip |
| `kff` | Front Flip | Makes the robot perform a front flip |
| `kbx` | Boxing | Makes the robot perform boxing movements |
| `kchr` | Cheer | Makes the robot cheer |
| `kang` | Angry | Makes the robot display angry stance |
| `kjmp` | Jump | Makes the robot jump |
| `krl` | Roll | Makes the robot roll |
| `krc` | Recover | Makes the robot recover from a fall |
| `kpd` | Play Dead | Makes the robot play dead |
| `kpu` | Push Up | Makes the robot do push-ups |
| `kpu1` | Push Up One Hand | Makes the robot do push-ups with one hand |
| `ktbl` | Be Table | Makes the robot assume "table" position |

### Interactive Behaviors

| Command | Action | Description |
|---------|--------|-------------|
| `khi` | Hi | Makes the robot wave hello |
| `khg` | Hug | Makes the robot give a hug |
| `khsk` | Hand Shake | Makes the robot shake hands |
| `kfiv` | High Five | Makes the robot give a high five |
| `khu` | Hands Up | Makes the robot raise its hands |
| `khds` | Stand on Hands | Makes the robot stand on its hands |
| `knd` | Nod | Makes the robot nod |
| `kwh` | Wave Head | Makes the robot wave its head |
| `kgdb` | Good Boy | Makes the robot perform good boy behavior |

### Utility Commands

| Command | Action | Description |
|---------|--------|-------------|
| `kck` | Check Around | Makes the robot check its surroundings |
| `kdg` | Dig | Makes the robot dig |
| `ksnf` | Sniff | Makes the robot sniff |
| `kscrh` | Scratch | Makes the robot scratch |
| `kpee` | Pee | Makes the robot simulate peeing |
| `kkc` | Kick | Makes the robot kick |
| `kts` | Test | Puts the robot in test mode |
| `kdropped` | Dropped | Makes robot assume dropped position |
| `klifted` | Lifted | Makes robot assume lifted position |
| `klnd` | Landing | Makes robot assume landing pose |

### Push Commands

| Command | Action | Description |
|---------|--------|-------------|
| `kphF` | Push Forward | Makes the robot push forward |
| `kphL` | Push Left | Makes the robot push to the left |
| `kphR` | Push Right | Makes the robot push to the right |

## Command Patterns and Best Practices

### Sequencing Commands

```python
# Basic sequence
sendSkillStr("ksit", 1)     # Sit
sendSkillStr("khi", 2)      # Wave hello
sendSkillStr("kup", 1)      # Stand up

# Complex routine
sendSkillStr("kwkF", 3)     # Walk forward for 3 seconds
sendSkillStr("kvtL", 2)     # Turn left for 2 seconds
sendSkillStr("kbf", 1)      # Backflip
sendSkillStr("krest", 1)    # Rest
```

### Delay Time Guidelines

- **Short actions (1 second)**: Basic postures, simple movements
- **Medium actions (2-3 seconds)**: Walking, complex movements
- **Long actions (4+ seconds)**: Continuous movements, sequences

### Error Handling

```python
try:
    autoConnect()
    sendSkillStr("ksit", 1)
except Exception as e:
    print(f"Robot control error: {e}")
finally:
    closePort()
```

### Safe Command Sequences

- Always end sequences with `krest`.
- Use appropriate delays between commands
- Keep sequences under 12 commands for reliability

## Prompt Engineering Guidelines

When connecting to AI systems, provide this context:

1. Available commands from skill reference table
2. Delay time recommendations
3. Safe sequencing patterns
4. Error handling requirements

## Technical Notes

- All commands are case-sensitive
- Robot must be connected before sending commands
- Commands are executed immediately upon receipt
- Delay parameter controls inter-command timing, not action duration
- Serial communication uses 115200 baud rate
- Compatible with Windows, macOS, and Linux systems
