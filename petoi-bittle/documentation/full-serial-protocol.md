# OpenCat ESP32 Serial Protocol Commands Documentation

## Overview

The OpenCat ESP32 robot uses a serial communication protocol to control various aspects of the robot including movement, servos, sensors, and system configuration. Commands are sent via Serial (USB), Bluetooth, or WiFi connections.

## Command Structure

- Commands are typically single characters or character combinations
- Some commands accept parameters immediately following the command letter
- Commands are case-sensitive
- Most commands are terminated by newline or processed immediately

## Complete Command Reference

### 🎯 **Movement & Gait Commands**

#### Basic Gaits

- **`d`** - **Default gait** (walk forward)
- **`F`** - **Forward walk** - Makes the robot walk forward continuously
- **`L`** - **Left turn** - Rotates the robot left while walking
- **`R`** - **Right turn** - Rotates the robot right while walking
- **`B`** - **Backward walk** - Makes the robot walk backward
- **`G`** - **Gallop** - Fast galloping gait
- **`H`** - **Hop** - Hopping movement
- **`J`** - **Jump** - Jumping motion

#### Specialized Gaits

- **`bdF`** - **Bound forward** - Bounding gait moving forward
- **`bk`** - **Back kick** - Performs a back kick motion
- **`bkF`** - **Back flip** - Attempts a backflip motion
- **`bkL`** - **Back kick left** - Back kick with left rotation
- **`crF`** - **Crawl forward** - Low crawling motion forward
- **`crL`** - **Crawl left** - Crawling with left turn
- **`gpF`** - **Gap forward** - Gait for crossing gaps
- **`gpL`** - **Gap left** - Gap crossing with left turn
- **`hlw`** - **Halloween** - Special Halloween-themed motion
- **`jpF`** - **Jump forward** - Forward jumping motion
- **`lftF`** - **Lift forward** - Lifting motion while moving forward
- **`lftL`** - **Lift left** - Lifting motion with left turn
- **`phF`** - **Push forward** - Pushing motion forward
- **`phL`** - **Push left** - Pushing motion with left turn
- **`trF`** - **Trot forward** - Trotting gait forward
- **`trL`** - **Trot left** - Trotting with left turn
- **`vtF`** - **Vault forward** - Vaulting motion forward
- **`vtL`** - **Vault left** - Vaulting with left turn
- **`wkF`** - **Walk forward** - Standard walking forward
- **`wkL`** - **Walk left** - Walking with left turn

### 🎭 **Behavior Commands**

#### Basic Behaviors

- **`kbalance`** - **Balance** - Activates balancing mode
- **`ksit`** - **Sit** - Makes the robot sit down
- **`kup`** - **Stand up** - Makes the robot stand up from sitting
- **`krest`** - **Rest** - Rest position (lying down)
- **`kstr`** - **Stretch** - Performs stretching motion
- **`khi`** - **Say hi** - Wave hello gesture
- **`kpee`** - **Pee** - Mimics peeing behavior
- **`kpu`** - **Push up** - Performs push-up motion
- **`kpd`** - **Play dead** - Falls and plays dead
- **`kzero`** - **Zero position** - Returns all servos to zero/calibration position
- **`kng`** - **Nod** - Nodding gesture
- **`kck`** - **Check** - Self-check motion
- **`kdig`** - **Dig** - Digging motion
- **`ksnf`** - **Sniff** - Sniffing behavior

### 🎮 **Servo Control Commands**

#### Joint Control

- **`m`** - **Move joint** - Format: `m[index] [angle]`
  - Example: `m8 45` moves joint 8 to 45 degrees
  - Supports multiple joints: `m8 45 12 -30 16 50`

- **`M`** - **Move with time** - Format: `M[index] [angle] [time]`
  - Includes movement duration in milliseconds

- **`i`** - **Simultaneous move** - Format: `i[index] [angle] [index] [angle]...`
  - Moves multiple joints simultaneously
  - Example: `i8 45 12 -30 16 50`

- **`I`** - **Indexed move array** - Format: `I[count] [index] [angle]...`
  - First parameter is the count of joint pairs

#### Servo Configuration

- **`@`** - **Set PWM servo range** - Format: `@[min],[max]`
  - Sets the PWM pulse width range for servos
  - Example: `@500,2500` sets 500-2500 microsecond range

- **`;`** - **Soft servo mode** - Sets servos to compliant/soft mode (reduced torque)
- **`:`** - **Hard servo mode** - Sets servos to stiff mode (full torque)
- **`h`** - **Hold position** - Maintains current servo positions
- **`r`** - **Relax servos** - Disables all servo torque

### 🔧 **Calibration Commands**

- **`c`** - **Enter calibration mode** - Starts interactive calibration
- **`cc`** - **Calibration with IMU** - Calibration using IMU feedback
- **`s`** - **Save calibration** - Saves current calibration to EEPROM
- **`a`** - **Abort calibration** - Exits calibration without saving
- **`Y`** - **Confirm action** - Used during calibration to confirm
- **`U`** - **Random calibration mode** - Special calibration mode
- **`V[joint] [offset]`** - **Set calibration offset** - Directly set joint calibration offset
  - Example: `V8 5` sets joint 8 offset to 5 degrees

### 🔄 **Gyroscope/IMU Commands**

- **`g`** - **Toggle gyro** - Toggles gyroscope on/off
- **`gb`** - **Gyro balance off** - Disables gyro balancing (C_GYRO_BALANCE_OFF)
- **`gB`** - **Gyro balance on** - Enables gyro balancing (C_GYRO_BALANCE_ON)  
- **`gc`** - **Calibrate IMU** - Calibrates the IMU/gyroscope
- **`gci`** - **Calibrate IMU immediately** - Immediate IMU calibration
- **`gF`** - **Increase gyro frequency** - Increases gyroscope sampling rate
- **`gf`** - **Reduce gyro frequency** - Decreases gyroscope sampling rate
- **`gy`** - **Gyro data** - Prints current gyro readings
- **`ga`** - **Gyro angle** - Shows current tilt angles

### 🔊 **Sound & Voice Module Commands**

- **`b`** - **Beep** - Format: `b[note] [duration]`
  - Plays a beep sound
  - Example: `b12 200` plays note 12 for 200ms

- **`B`** - **Melody** - Format: `B[count] [note1] [duration1] [note2] [duration2]...`
  - Plays a sequence of notes
  
#### Voice Module Control (X-Commands)

- **`XAa`** - **English voice** - Switch to English language
- **`XAb`** - **Chinese voice** - Switch to Chinese language  
- **`XAc`** - **Voice on** - Enable voice/audio responses
- **`XAd`** - **Voice off** - Disable voice/audio responses
- **`XAe`** - **Learn voice** - Start voice command learning mode
- **`XAf`** - **Stop learning** - Stop voice command learning
- **`XAg`** - **Clear voice data** - Clear all learned voice commands

### 📡 **Module Management Commands**

- **`X?`** - **Show modules** - Display status of all connected modules
- **`X~`** - **Deactivate all** - Disable all external modules
- **`X[module_code]`** - **Enable module** - Enable specific module by code
  - Module codes vary by connected hardware

### 🌐 **Communication Commands**

#### Bluetooth Commands

- **`n[name]`** - **Rename Bluetooth** - Changes Bluetooth device name
  - Example: `nMyRobot` renames to "MyRobot"

- **`w`** - **WiFi state** - Shows WiFi connection status
- **`W`** - **WiFi AP mode** - Starts WiFi access point mode

#### Serial Output Control

- **`l`** - **List skills** - Lists all available movement skills
- **`ll`** - **Skill details** - Shows detailed skill information
- **`v`** - **Version** - Displays firmware version
- **`?`** - **Help** - Shows command help information
- **`!`** - **Silent mode** - Toggles verbose output on/off

### 🔢 **System Commands**

#### Memory & Storage

- **`S`** - **Store to EEPROM** - Saves system state to permanent storage
- **`K`** - **Skills from memory** - Load skills from PROGMEM
- **`k`** - **Skill from string** - Execute skill from command string
- **`R`** - **Restore defaults** - Restore factory default settings
- **`E`** - **Export settings** - Export current configuration

#### System Control

- **`z`** - **Shut down** - Safe shutdown procedure
- **`Z`** - **Emergency stop** - Immediate stop all movements
- **`p`** - **Pause** - Pause current action
- **`P`** - **Power status** - Show battery/power information
- **`x`** - **Reset** - Software reset
- **`y`** - **System info** - Display system information

### 🎯 **Special Commands**

#### Testing & Debug

- **`T`** - **Test mode** - Enter test mode for diagnostics
- **`t`** - **Test routine** - Run specific test routine
- **`C`** - **Color detect** - Test color sensor (if equipped)
- **`O`** - **Obstacle test** - Test obstacle sensors
- **`Q`** - **Query sensors** - Display all sensor readings

#### Task Commands

- **`*`** - **Asterisk mode** - Special task mode
- **`#`** - **Hash mode** - Alternative task mode
- **`$`** - **Dollar mode** - Economic/power saving mode
- **`%`** - **Percent mode** - Performance mode

### 📝 **Parameter Formats**

#### Numeric Parameters

- Angles: -125 to 125 degrees (servo dependent)
- Time: milliseconds (0-65535)
- Indices: 0-15 for joint numbers
- Notes: 0-127 for buzzer tones

#### String Parameters

- Names: Up to 16 characters for Bluetooth naming
- Skills: Predefined skill names (case sensitive)

### 🔄 **Command Persistence**

To make settings permanent:

1. Configure desired settings (gyro, voice, etc.)
2. Send **`s`** command to save to EEPROM
3. Settings will persist through power cycles

### 💡 **Usage Examples**

```txt
# Disable gyro and voice permanently
gb      # Turn off gyro
XAd     # Turn off voice  
s       # Save settings

# Calibrate a joint
c       # Enter calibration
m8 5    # Adjust joint 8 by 5 degrees
s       # Save calibration

# Play a tune
B3 60 200 64 200 67 400  # 3 notes melody

# Complex movement
i8 45 12 -30 16 50  # Move 3 joints simultaneously
```

### ⚠️ **Important Notes**

1. Some commands may not be available depending on hardware configuration
2. Always use `s` command to persist important settings
3. Use `Z` for emergency stop in case of issues
4. Calibration changes should be done carefully to avoid damaging servos
5. Module commands (X-prefix) depend on connected hardware modules

This documentation represents the complete serial protocol as found in the OpenCat ESP32 codebase. Commands are continuously updated with firmware revisions.
