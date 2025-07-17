#!/usr/bin/env python3
"""
Test script for Petoi.py

This script tests the basic functionality of the unified Petoi import file.
Run this to verify everything works before using in workshops.
"""

import sys
import os
sys.path.append('.')

try:
    from Petoi import *
    print("✅ Successfully imported Petoi")
    
    # Test basic functions exist
    functions_to_test = [
        'autoConnect',
        'sendSkillStr', 
        'loadSkill',
        'sendCmdStr',
        'sendLongCmd',
        'play',
        'rotateJoints',
        'deacGyro',
        'getAngle',
        'getAngleList',
        'readAnalogValue',
        'readDigitalValue',
        'readUltrasonicDistance',
        'writeAnalogValue',
        'writeDigitalValue',
        'closePort',
        'openPort',
        'printSkillFileName'
    ]
    
    print("\n📋 Testing function availability:")
    for func_name in functions_to_test:
        if func_name in globals():
            print(f"  ✅ {func_name}")
        else:
            print(f"  ❌ {func_name} - MISSING")
    
    # Test Communication class
    print("\n🔌 Testing Communication class:")
    try:
        ports = Communication.Print_Used_Com()
        print(f"  ✅ Found {len(ports)} serial ports: {ports}")
    except Exception as e:
        print(f"  ❌ Error checking ports: {e}")
    
    print("\n🎉 Petoi test completed!")
    print("\nTo use in your workshop code:")
    print("```python")
    print("from Petoi import *")
    print("autoConnect()")
    print("sendSkillStr('ksit', 1)")
    print("closePort()")
    print("```")
    
except ImportError as e:
    print(f"❌ Import failed: {e}")
except Exception as e:
    print(f"❌ Unexpected error: {e}")
