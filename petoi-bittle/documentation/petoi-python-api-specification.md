# Petoi Bittle Robot Dog - Python API Technical Specification

## Overview

This document provides the complete technical specification for controlling the Petoi Bittle and Bittle X Robot Dogs using Python.

The official version is at <https://docs.petoi.com/apis/python-api>. This version was created for easy markdown based access, with enhancements for integration with AI systems.

## Quick Start

```python
from Petoi import *

# Connect to robot
autoConnect()

# Send skill commands
sendSkillStr("ksit", 1)  # Make robot sit
sendSkillStr("kup", 1)   # Make robot stand
sendSkillStr("krest", 1)   # Make robot rest. Always leave the robot in a resting state after taking actions.

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

- Send raw command strings to robot
- Parameters:
  - `cmdStr` (string): Raw command string
  - `delayTime` (int): Delay in seconds
- Available raw commands:
  - `'c'` - Enter calibration mode
  - `'d'` - Put robot down and shut down servos
  - `'m'` - Control joint servo rotation (ASCII format)
  - `'M'` - Control joint servo rotation (binary format)
  - `'i'` - Control multiple joint servos simultaneously (ASCII format)
  - `'I'` - Control multiple joint servos simultaneously (binary format)
  - `'b'` - Control buzzer to beep
  - `'K'` - Send skill data arrays in real-time
  - `'l'` - Load skill from library
- Example: `sendCmdStr('d', 2)` - Put robot down with 2-second delay
- **Warning**: This should not be used by automated AI systems - use `sendSkillStr` instead

## Complete Skill Command Reference

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
| `kdropped` | Dropped | Makes robot assume dropped position |
| `klifted` | Lifted | Makes robot assume lifted position |
| `klnd` | Landing | Makes robot assume landing pose |

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
| `kvtR` | Spin Right | Makes the robot spin to the right |
| `kmw` | Moon Walk | Makes the robot perform the moonwalk |

### Tricks & Acrobatics

| Command | Action | Description |
|---------|--------|-------------|
| `kjmp` | Jump | Makes the robot jump |
| `kbf` | Back Flip | Makes the robot perform a backflip |
| `kff` | Front Flip | Makes the robot perform a front flip |
| `kpd` | Play Dead | Makes the robot play dead |
| `kpu` | Push Up | Makes the robot do push-ups |
| `kpu1` | Push Up One Hand | Makes the robot do push-ups with one hand |
| `krl` | Roll | Makes the robot roll |
| `kbx` | Boxing | Makes the robot perform boxing movements |
| `kmw` | Moonwalk | Makes the robot moonwalk |
| `kvt` | Side Step | Makes the robot side step |
| `krc` | Recover | Makes the robot recover from a fall |
| `ktbl` | Be Table | Makes the robot assume "table" position |

### Interactive Behaviors

| Command | Action | Description |
|---------|--------|-------------|
| `kwh` | Wave Head | Makes the robot wave its head |
| `khi` | Hi | Makes the robot wave hello |
| `kchr` | Cheer | Makes the robot cheer |
| `kang` | Angry | Makes the robot display angry stance |
| `kck` | Check Around | Makes the robot check its surroundings |
| `kcmh` | Come Here | Makes the robot beckon |
| `khsk` | Hand Shake | Makes the robot shake hands |
| `khg` | Hug | Makes the robot give a hug |
| `kfiv` | High Five | Makes the robot give a high five |
| `khu` | Hands Up | Makes the robot raise its hands |
| `khds` | Stand on Hands | Makes the robot stand on its hands |
| `knd` | Nod | Makes the robot nod |
| `kpry` | Pray | Makes the robot pray |
| `kthk` | Thank | Makes the robot show thanks |
| `kgdb` | Good Boy | Makes the robot perform good boy behavior |

### Utility & Maintenance Commands

| Command | Action | Description |
|---------|--------|-------------|
| `ksnf` | Sniff | Makes the robot sniff |
| `kscrh` | Scratch | Makes the robot scratch |
| `kdg` | Dig | Makes the robot dig |
| `kpee` | Pee | Makes the robot simulate peeing |
| `kkc` | Kick | Makes the robot kick |
| `kts` | Test | Puts the robot in test mode |
| `kzz` | Sleep | Makes the robot go to sleep |

### Push Commands

| Command | Action | Description |
|---------|--------|-------------|
| `kphF` | Push Forward | Makes the robot push forward |
| `kphL` | Push Left | Makes the robot push to the left |
| `kphR` | Push Right | Makes the robot push to the right |

### Sound Commands

| Command | Action | Description |
|---------|--------|-------------|
| `kmeow` | Meow | Makes the robot meow |
| `kbark` | Bark | Makes the robot bark |
| `kgrowl` | Growl | Makes the robot growl |
| `klaugh` | Laugh | Makes the robot laugh |
| `kcry` | Cry | Makes the robot cry |

- Send raw command strings to robot
- Parameters:
  - `cmdStr` (string): Raw command string
  - `delayTime` (int): Delay in seconds
- Available raw commands:
  - `'c'` - Enter calibration mode
  - `'d'` - Put robot down and shut down servos
  - `'m'` - Control joint servo rotation (ASCII format)
  - `'M'` - Control joint servo rotation (binary format)
  - `'i'` - Control multiple joint servos simultaneously (ASCII format)
  - `'I'` - Control multiple joint servos simultaneously (binary format)
  - `'b'` - Control buzzer to beep
  - `'K'` - Send skill data arrays in real-time
  - `'l'` - Load skill from library
- Example: `sendCmdStr('d', 2)` - Put robot down with 2-second delay
- **Warning**: This should not be used by automated AI systems - use `sendSkillStr` instead

## Advanced Control

**`loadSkill(fileName, delayTime)`**

- Load and execute custom skill files
- Parameters:
  - `fileName` (string): Skill file name (.md format)
  - `delayTime` (int): Delay in seconds

**`sendLongCmd(token, var, delayTime)`**

- Send complex commands with multiple parameters
- Parameters:
  - `token` (string): Command token ('m', 'M', 'i', 'I', 'b', 'K', 'c')
  - `var` (list): List of parameters depending on command
  - `delayTime` (int): Delay in seconds
- Examples:
  - `sendLongCmd('m', [0, 45, 0, -45], 2)` - Move joints sequentially
  - `sendLongCmd('I', [8, 50, 9, 50], 3)` - Move joints simultaneously
  - `sendLongCmd('b', [14, 4, 21, 4], 1)` - Play melody
  - `sendLongCmd('c', [0, -9], 2)` - Calibrate specific joint

**`play(token, var, delayTime)`**

- Play tones and melodies using the buzzer
- Parameters:
  - `token` (string): 'b' for buzzer control
  - `var` (list): List of [note, duration, note, duration...] pairs
  - `delayTime` (int): Delay in seconds after melody
- Example: `play('b', [14, 4, 21, 4, 23, 4], 2)` - Play simple melody

**`deacGyro()`**

- Deactivate the gyroscope sensor
- No parameters required
- Use when gyroscope interferes with movements

**`printSkillFileName()`**

- Print all available skill file names
- No parameters required
- Useful for debugging and discovering available skills

## Sensor Reading

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

## Music and Sound Control

**`play(token, var, delayTime)`**

- Play tones and melodies using the buzzer
- Parameters:
  - `token` (string): 'b' for buzzer control
  - `var` (list): List of [note, duration, note, duration...] pairs
  - `delayTime` (int): Delay in seconds after melody
- Note values: 0-23 represent different musical notes
- Duration values: 1-8 represent note lengths (1/duration second)
- Example: `play('b', [14, 4, 21, 4, 23, 4], 2)` - Play simple melody

## Utility Functions

**`printH(head, value)`**

- Print debug information with formatting
- Parameters:
  - `head` (string): Header text
  - `value` (any): Value to print
- Use for debugging and monitoring

**`encode(in_str, encoding='utf-8')`**

- Encode character strings to bytes
- Parameters:
  - `in_str` (string): String to encode
  - `encoding` (string): Encoding format (default: 'utf-8')
- Returns: Encoded byte string

## Joint Control

**`getAngle(index)`**

- Get current angle of specific joint
- Parameter: `index` (int) - Joint index (0-15)
- Returns: Current angle in degrees

**`getCurAng(index)`**

- Alternative function to get current angle of specific joint
- Parameter: `index` (int) - Joint index (0-15)
- Returns: Current angle in degrees

**`getAngleList()`**

- Get angles of all joints
- Returns: List of current joint angles for all 16 joints

**`rotateJoints(token, var, delayTime)`**

- Rotate specific joints to absolute positions
- Parameters:
  - `token` (string): 'm' (sequential ASCII), 'M' (sequential binary), 'i' (simultaneous ASCII), 'I' (simultaneous binary)
  - `var` (list): List of [joint_index, angle, joint_index, angle...] pairs
  - `delayTime` (int): Delay in seconds
- Examples:
  - `rotateJoints('m', [0, 45, 8, -30], 2)` - Move joints 0 and 8 sequentially
  - `rotateJoints('I', [0, 45, 8, -30], 2)` - Move joints 0 and 8 simultaneously

**`absValList(joint_index, angle)`**

- Create an absolute value list for joint rotation
- Parameters:
  - `joint_index` (int): Index of the joint (0-15)
  - `angle` (int): Target angle in degrees
- Returns: List formatted for `rotateJoints`

**`relativeValList(index, symbol, angle)`**

- Create a relative value list for joint rotation
- Parameters:
  - `index` (int): Joint index (0-15)
  - `symbol` (string): '+' for addition, '-' for subtraction
  - `angle` (int): Angle change in degrees
- Returns: List formatted for `rotateJoints`

## Output Control

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

## Command Patterns and Best Practices

### Delay Time Guidelines

- **Short actions (1 second)**: Basic postures, simple movements
- **Medium actions (2-3 seconds)**: Walking, complex movements
- **Long actions (4+ seconds)**: Continuous movements, sequences

### Error Handling

```python
try:
    autoConnect()
    sendSkillStr("ksit", 1)
    play('b', [14, 4, 21, 4], 1)  # Play simple beep
    rotateJoints('I', [0, 45, 8, -30], 2)  # Move joints simultaneously
except Exception as e:
    print(f"Robot control error: {e}")
finally:
    closePort()
```

### Advanced Command Examples

```python
# Joint control examples
rotateJoints('m', [0, 45, 0, -45, 0, 45, 0, -45], 2)  # Sequential movement
rotateJoints('I', [8, 50, 9, 50, 10, 50, 11, 50], 3)  # Simultaneous movement
rotateJoints('I', [20, 0, 0, 0, 0, 0, 0, 0, 45, 45, 45, 45, 36, 36, 36, 36], 5)  # All 16 joints

# Buzzer control examples
play('b', [10, 2], 2)  # Single tone
play('b', [14, 8, 14, 8, 21, 8, 21, 8, 23, 8, 23, 8, 21, 4], 3)  # Simple melody

# Calibration examples
sendCmdStr('c', 2)  # Enter calibration mode
sendLongCmd('c', [0, -9], 2)  # Calibrate specific joint

# Raw command examples (use with caution)
sendCmdStr('d', 2)  # Put robot down and shut down servos
```

### Real-time Skill Data

```python
# Example skill data array for custom movements
skill_data = [
    -3, 0, 5, 1,  # Header information
    0, 1, 2,      # Timing data
    45, 0, 0, 0, 0, 0, 0, 0, 45, 35, 38, 50, -30, -10, 0, -20, 6, 1, 0, 0,  # Frame 1
    -45, 0, 0, 0, 0, 0, 0, 0, 35, 45, 50, 38, -10, -30, -20, 0, 6, 1, 0, 0,  # Frame 2
    0, 0, 0, 0, 0, 0, 0, 0, 30, 30, 30, 30, 30, 30, 30, 30, 5, 0, 0, 0,  # Frame 3
]

# Send skill data in real-time
sendLongCmd('K', skill_data, 1)
```

### Safe Command Sequences

- Always end sequences with `krest`
- Use appropriate delays between commands
- Keep sequences under 12 commands for reliability
- Test complex sequences step by step before automation
- Use `deacGyro()` if gyroscope interferes with movements
- Always call `closePort()` when finished

### Joint Index Reference

The robot has 16 joints (0-15):

- Head joints: 0-3
- Body joints: 4-7  
- Leg joints: 8-15

### Command Token Reference

- `'m'` - Sequential joint movement (ASCII format)
- `'M'` - Sequential joint movement (binary format)
- `'i'` - Simultaneous joint movement (ASCII format)
- `'I'` - Simultaneous joint movement (binary format)
- `'b'` - Buzzer control
- `'c'` - Calibration mode
- `'d'` - Put down and shut down servos
- `'K'` - Real-time skill data
- `'l'` - Load skill from library

## Prompt Engineering Guidelines

When connecting to AI systems, provide this context:

1. Available commands from skill reference table
2. Delay time recommendations
3. Safe sequencing patterns
4. Error handling requirements
5. Joint control capabilities for advanced movements
6. Music/sound control options
7. Real-time skill data format for custom movements

### AI Safety Guidelines

- Always use `sendSkillStr()` for AI-controlled movements
- Avoid `sendCmdStr()` and `sendLongCmd()` in automated systems
- Require human approval for complex joint movements
- Always end AI-generated sequences with `krest`
- Implement command logging for transparency

## Technical Notes

- All commands are case-sensitive
- Robot must be connected before sending commands
- Commands are executed immediately upon receipt
- Delay parameter controls inter-command timing, not action duration
- Serial communication uses 115200 baud rate
- Compatible with Windows, macOS, and Linux systems
- Supports up to 16 degrees of freedom (joints 0-15)
- Buzzer supports musical notes 0-23
- Skill data arrays enable custom movement sequences
