# Petoi Unified File Creation

## Overview

This folder contains the original Petoi Python files that were combined into a single unified file `Petoi.py` for easier workshop deployment.

The source of the original files is <https://github.com/PetoiCamp/Petoi_MindPlusLib/tree/main/python/libraries>.

## Original Files

The following files were combined:

1. **SerialCommunication.py** - Core serial communication class for connecting to the Petoi robot
2. **ardSerial.py** - Arduino-style serial communication functions and protocol handling
3. **PetoiRobot.py** - High-level robot control functions and skill management
4. **config.py** - Configuration settings and model definitions

## What Was Done

1. **File Consolidation**: All four files were merged into `Petoi.py` while preserving their original functionality
2. **Code Organization**: Each original file's code is clearly marked with comments in the unified file
3. **Import Optimization**: All imports were moved to the top of the unified file
4. **Function Preservation**: Every function maintains its original behavior and parameters
5. **Error Handling**: Original error handling and logging remain intact

## Usage

Instead of importing multiple files:

```python
from PetoiRobot import *
from SerialCommunication import *
from ardSerial import *
```

You can now use a single import:

```python
from Petoi import *

# Connect to robot
autoConnect()

# Send commands
sendSkillStr("ksit", 1)  # Make robot sit
sendSkillStr("kup", 1)   # Make robot stand

# Close connection
closePort()
```
