# Robot Dog Arm Commands - Student Guide

## Overview

If your robot dog has the **robot arm attachment**, you can control it with natural language! The AI knows all the robot arm commands - your job is to learn how to prompt it effectively.

⚠️ **Safety First**: Never put your hands between the robot claws when the arm is moving!

## Basic Arm Actions

### Picking Up Objects

Tell the AI to pick up objects from different positions:

```txt
"pick up the object in front of you"
"pick up something to your left" 
"pick up the object underneath you"
"pick up the object to your right"
"grab something in front"
```

### Putting Down Objects

After picking something up, tell the AI where to put it:

```txt
"put it down in front of you"
"place it to your left"
"put the object down underneath"
"set it down to your right"
```

### Special Actions

```txt
"hunt for an object" - quickly grab something in front
"show off what you're holding" - display the object
"clap with your gripper"
"drop what you're holding"
"throw what you have forward"
"toss it to the left"
"launch it forward"
```

## Combining Movement + Arm Control

You can combine walking with arm actions:

```txt
"walk forward, then pick up something"
"turn left, grab an object, then turn right and put it down"
"go to the object, pick it up, walk to the other side, and put it down"
```

## Advanced Prompting Tips

### Be Specific About Positions

- "in front" = directly ahead of the robot
- "to the left" = robot's left side  
- "to the right" = robot's right side
- "underneath" = directly below the arm

### Chain Multiple Actions

```txt
"First stand up, then walk forward, pick up the red ball, turn around, walk back, and put it down"
```

### Fine-Tune Movements

The AI now understands VERY precise arm control! You can control each joint individually:

## 🚨 CRITICAL: Direction Fix Applied!

**Due to servo mounting, directions are now corrected:**
- **LEFT = Say "left" (the AI sends POSITIVE angles)**
- **RIGHT = Say "right" (the AI sends NEGATIVE angles)**

The AI now handles this automatically - just say what you want naturally!

## 🚀 FULL HARDWARE RANGE UNLOCKED!

Your robot arm can now move WAY beyond the previous limits:

### Joint Ranges (No Limits!)
- **Base Rotation**: 250° total (-125° to +125°)
- **Shoulder**: 210° total (-90° to +120°) - Can go ABOVE the head!
- **Gripper**: 180° total (-60° to +120°)

#### Base Rotation (Joint 0 - Left/Right) - FULL RANGE

```txt
"move your arm left a little bit" (AI sends positive angle)
"rotate the base 30 degrees to the right" (AI sends negative angle)
"turn the arm all the way left" (maximum left = 125°)
"rotate extreme right" (maximum right = -125°)
"scan the entire room" (full 250° sweep)
"center the base rotation"
```

#### Shoulder Pitch (Joint 1 - Up/Down) - EXPANDED RANGE

```txt
"raise your arm up halfway" 
"lower the arm a bit"
"point your arm straight up ABOVE THE HEAD" (can go to 120°!)
"point the arm down below the body" (can go to -90°)
"arm as high as possible" (maximum up = 120°)
"tilt the arm down slightly"
```

#### Gripper Control (Joint 2 - Open/Close) - MAXIMUM RANGE

```txt
"open the gripper wide"
"close the gripper gently"
"open gripper as wide as possible" (maximum open = -60°)
"maximum grip strength" (maximum close = 120°)
"grip it tighter"
"open it just a little"
```

#### Multiple Joints at Once

```txt
"point forward with an open gripper"
"move to neutral position"
"reach up and to the left with gripper ready"
"extreme left position with arm high" (combines max left + max up)
"victory pose" (arm up, gripper open, centered)
```

#### Smart Movement Descriptions

The AI understands how much to move based on your words:

- "a little", "slightly", "tiny bit" = small movements (5-15 degrees)
- "some", "a bit" = medium movements (15-30 degrees)
- "more", "further" = larger movements (30-50 degrees)
- "a lot", "much more" = big movements (50-80 degrees)  
- "all the way", "fully" = maximum safe movement
- **"extreme", "as far as possible" = ABSOLUTE HARDWARE LIMITS**

#### Speed-Controlled Movement (NEW!)

```txt
"slowly rotate left" (controlled speed)
"quickly close gripper" (fast movement)
"smoothly sweep from left to right" (fluid motion)
```

#### Complex Sequences

```txt
"scan the room by moving your arm left to right slowly"
"carefully approach the fragile object from above"
"do a little arm dance"
"sweep your arm in a circle"
"test the full range of motion" (moves through ALL extremes)
"calibrate your gripper" (auto-calibration)
"victory dance with the arm" (dynamic sequence)
"make the arm go crazy" (rapid extreme movements)
```

## Challenge Mission

Your goal is to:

1. **Find an object** in the room (small enough for the gripper)
2. **Navigate to it** using prompts
3. **Pick it up** with the robot arm
4. **Move to a new location**
5. **Put it down** in the new spot
6. **Try to do all of this with a single complex prompt!**

## Troubleshooting

**Arm not responding?**

- Make sure you have the Bittle X+Arm model (robot with arm attachment)
- Check that Challenge 5 says "Robot Arm DETECTED"
- Try simpler commands first

**Gripper not working right?**

- The AI will automatically calibrate the gripper
- Try saying "calibrate your gripper" if needed

**Object too big/small?**

- Best objects: small toys, blocks, lightweight items
- Avoid: heavy objects, your fingers, fragile items

## Example Session

```txt
You: "stand up and look around"
AI: "Standing up and scanning the area!"

You: "walk forward until you see a small object"
AI: "Walking forward, searching for objects..."

You: "pick up that object"
AI: "Picking up the object in front of me!"

You: "turn around, walk to the other side of the room, and gently put it down"
AI: "Turning around, walking across the room, and placing the object down carefully!"
```

## Advanced Example Session

```txt
You: "open your gripper wide and lower your arm a bit"
AI: "Opening gripper fully and lowering arm slightly"
[Executes: m2 -30, then m1 -15]

You: "now move the arm left about 30 degrees"
AI: "Moving arm left 30 degrees"
[Executes: m0 30] (CORRECTED: positive for left)

You: "raise the arm as high as possible above the head"
AI: "Moving arm to absolute maximum height!"
[Executes: m1 120] (NEW: can go above head!)

You: "now rotate all the way to the right"
AI: "Rotating arm to maximum right position!"
[Executes: m0 -125] (NEW: full hardware range!)

You: "test the complete range of motion"
AI: "Testing complete range of motion!"
[Executes: Multiple commands covering ALL extremes]

You: "do a victory dance with the arm"
AI: "Victory dance mode activated!"
[Executes: Complex sequence with rapid extreme movements]

You: "calibrate the gripper when you're done"
AI: "Auto-calibrating gripper using vibration feedback"
[Executes: c-2]
```

## 🔥 NEW EXTREME COMMANDS TO TRY

```txt
"arm straight up above the head" → Maximum height (120°)
"point the arm down below the body" → Minimum position (-90°)
"rotate the arm all the way left" → Maximum left (125°)
"rotate the arm all the way right" → Maximum right (-125°)
"open gripper as wide as possible" → Maximum open (-60°)
"maximum grip strength" → Maximum close (120°)
"test every extreme position" → Full range demonstration
"sweep the entire area" → 250° base rotation
"reach behind the robot" → Arm points backward/down
"make the arm go wild" → Rapid extreme movements
```

## Pro Tips

- Start with simple commands, then get more complex
- The AI understands natural language - talk to it like a helpful robot assistant
- Combine robot movement with arm actions for cool sequences
- Try different gripping positions if the first attempt doesn't work
- Be patient - complex sequences take time to execute
- **🆕 DIRECTIONS FIXED**: Just say "left" or "right" naturally - the AI handles the servo inversion
- **🆕 FULL RANGE**: Push the limits! The arm can go WAY higher and further than before
- **🆕 SPEED CONTROL**: Use words like "slowly" or "quickly" for controlled movement
- **🆕 EXTREME POSITIONS**: Try "as far as possible" or "maximum" for hardware limits
- **🆕 COMPLEX SEQUENCES**: Chain multiple extreme movements for dramatic effects
- **🆕 NATURAL LANGUAGE**: Be descriptive - "sweep the entire area" works better than technical commands

## ⚡ NO LIMITS MODE ACTIVATED ⚡

The AI now has access to the FULL mechanical range with corrected directions. Push the boundaries and explore what your robot arm can really do!

Have fun controlling your robot assistant! 🤖🦾
