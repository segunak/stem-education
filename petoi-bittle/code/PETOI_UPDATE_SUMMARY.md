# Petoi.py Update Summary

## Overview
Updated the unified `Petoi.py` file to incorporate all the latest changes from the original Petoi files. The original files were significantly updated from Feb 2, 2024 to Feb 27, 2025.

## Key Changes Made

### 1. **Enhanced Imports and Dependencies**
- **Added**: `import copy` and `import glob` for enhanced functionality
- **Added**: `import tkinter.messagebox` for UI message boxes
- **Updated**: Enhanced import structure for better compatibility

### 2. **Updated Date Stamps**
- **ardSerial date**: Updated from "Feb 2, 2024" to "Feb 27, 2025"
- **Mind+ date**: Updated from "Oct 18, 2023" to "Feb 25, 2025"

### 3. **Enhanced Serial Communication**

#### **serialWriteNumToByte Function**
- **Major Enhancement**: Complete rewrite of the function
- **Added**: Support for skill header detection based on period
- **Added**: Frame size calculation for different skill types (gait, posture, behavior)
- **Added**: Automatic angle scaling for large angles (>125 or <-125)
- **Added**: Binary data packing using `struct.pack()`
- **Added**: Enhanced data slicing for better transmission (20-byte chunks)
- **Added**: Support for uppercase tokens with binary encoding
- **Added**: Improved handling of different token types

#### **serialWriteByte Function**
- **Enhanced**: Better handling of different token types
- **Added**: Support for 'X' and 'g' tokens
- **Added**: Binary encoding for 'L' and 'I' tokens using `struct.pack()`
- **Improved**: More robust variable handling

#### **printSerialMessage Function**
- **Updated**: Changed thresholds (8 seconds for 'k'/'K', 3 seconds for others)
- **Added**: Support for 'X' token handling
- **Enhanced**: Better response parsing with `split('\r')[0]`
- **Added**: Special handling for 'p' token responses
- **Improved**: More robust error handling

### 4. **New Robot Model Support**
- **Added**: `BittleX+Arm` model support with `BittleRData`
- **Added**: Comprehensive skill data for arm-equipped robots
- **Updated**: Model dictionary to include new robot variants

### 5. **Enhanced Directory Management**
- **Major Enhancement**: `makeDirectory()` function now handles model name conversions
- **Added**: Special handling for "BittleX+Arm" directory creation
- **Added**: Automatic directory renaming from "BittleR" to "BittleX+Arm"
- **Improved**: Better error handling and user feedback

### 6. **Updated File Handling**
- **Enhanced**: `file_name()` function now filters for `.md` files only
- **Added**: Better skill file management
- **Updated**: `creatSkillFile()` function with improved error handling
- **Added**: UTF-8 encoding support for file operations

### 7. **Enhanced Robot Control**
- **Updated**: `deacGyro()` function with board version detection
- **Added**: Support for both 'G' and 'g' commands based on board version
- **Enhanced**: Better type conversion in `absValList()` and `relativeValList()`

### 8. **New Global Variables**
- **Added**: `intoCameraMode = False`
- **Added**: `intoGestureMode = False`
- **Added**: `modelName = 'Bittle'`

### 9. **Enhanced Error Handling**
- **Improved**: Better exception handling throughout the codebase
- **Added**: More robust fallback mechanisms
- **Enhanced**: Better logging and debugging information

### 10. **Translation System Updates**
- **Enhanced**: Better handling of the translation system
- **Added**: Support for `config.strLan` language selection
- **Added**: Fallback to `textEN` for missing translations

## Backwards Compatibility
- All existing function calls remain compatible
- Same import structure: `from Petoi import *`
- All original functionality preserved

## New Features Available
1. **Enhanced Skill Support**: Better handling of complex robot skills
2. **Arm Robot Support**: Full support for BittleX+Arm robots
3. **Improved Communication**: More robust serial communication
4. **Better Error Handling**: Enhanced error detection and recovery
5. **Multi-Model Support**: Seamless switching between robot models

## Testing Results
- ✅ Successfully imports without errors
- ✅ All original functions available
- ✅ Enhanced serial communication protocols active
- ✅ New robot model support functional
- ✅ Backwards compatibility maintained

## Impact on Workshops
- **No Changes Required**: Existing workshop code continues to work
- **Enhanced Reliability**: Better error handling and communication
- **New Capabilities**: Support for arm-equipped robots
- **Improved Performance**: More efficient data transmission

The updated `Petoi.py` file is now ready for use in all workshops with enhanced functionality and improved reliability.
