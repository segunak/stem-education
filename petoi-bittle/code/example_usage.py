#!/usr/bin/env python3
"""
Example usage of Petoi.py

This demonstrates how to use the unified Petoi import file for basic robot control.
Perfect for workshops and quick prototyping.
"""

# Single import for all Petoi functionality
from Petoi import *

def main():
    print("🤖 Petoi Bittle X Control Example")
    print("=" * 40)
    
    # Connect to the robot
    print("📡 Connecting to robot...")
    try:
        autoConnect()
        print("✅ Connected successfully!")
    except Exception as e:
        print(f"❌ Connection failed: {e}")
        return
    
    # Demonstrate basic movements
    print("\n🎯 Demonstrating basic movements:")
    
    movements = [
        ("Sit", "ksit", 2),
        ("Stand up", "kup", 2),
        ("Stretch", "kstr", 3),
        ("Wave hello", "khi", 2),
        ("Cheer", "kchr", 3),
        ("Rest", "krest", 2)
    ]
    
    try:
        for name, command, delay in movements:
            print(f"  🎬 {name}...")
            sendSkillStr(command, delay)
            
        print("\n🎵 Playing a tune...")
        # Play a simple melody
        melody = [440, 200, 494, 200, 523, 200, 587, 200, 659, 400]
        play('b', melody, 2)
        
    except Exception as e:
        print(f"❌ Movement error: {e}")
    
    # Clean up
    print("\n🔌 Disconnecting...")
    try:
        closePort()
        print("✅ Disconnected successfully!")
    except Exception as e:
        print(f"❌ Disconnect error: {e}")

if __name__ == "__main__":
    main()
