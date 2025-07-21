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

```txt
"move your arm up a little bit"
"open the gripper more"
"rotate your base slightly to the right"
"adjust your grip"
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

## Pro Tips

- Start with simple commands, then get more complex
- The AI understands natural language - talk to it like a helpful robot assistant
- Combine robot movement with arm actions for cool sequences
- Try different gripping positions if the first attempt doesn't work
- Be patient - complex sequences take time to execute

Have fun controlling your robot assistant! 🤖🦾
