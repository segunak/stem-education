# Petoi Robot Python Control

Python libraries for controlling the Petoi Bittle X Robot Dog using the official Petoi Python API.

## Library Source

The Python control files come directly from the official Petoi repository:
**<https://github.com/PetoiCamp/Petoi_MindPlusLib/tree/main/python/libraries>**

These files should be updated periodically by downloading the latest versions from the official repository to ensure compatibility with current firmware.

## Required Files

To control the Petoi robot, you need all these files in your project folder:

- `PetoiRobot.py` - Main robot control functions.
- `ardSerial.py` - Serial communication handling.
- `SerialCommunication.py` - Low-level serial operations.
- `config.py` - Configuration settings.

**Important**: All files must be in the same directory for the imports to work correctly.

## Basic Usage

```python
from PetoiRobot import *

# Connect to robot
autoConnect()

# Send commands
sendSkillStr("ksit", 1)  # Make robot sit
sendSkillStr("kup", 1)   # Make robot stand
sendSkillStr("kjmp", 1)  # Make robot jump

# Close connection
closePort()
```

## Features

- **Official Support**: Uses Petoi's official Python API
- **Multi-Model Support**: Works with Bittle, Nybble, and BittleX+Arm robots
- **Regular Updates**: Download latest files from official repo for best compatibility

## Installation

1. **Install Python**: Make sure you have Python 3.6 or later installed on your system

2. **Download Libraries**: Copy all Python files from the official Petoi repository into your project folder

3. **Install Dependencies**: Run the following command to install required packages: `pip install -r requirements.txt`

4. **Connect Robot**: Connect your Petoi robot to your computer via USB or Bluetooth

## Official Documentation

- **Python API Reference**: <https://docs.petoi.com/apis/python-api>
- **Library Repository**: <https://github.com/PetoiCamp/Petoi_MindPlusLib/tree/main/python/libraries>
