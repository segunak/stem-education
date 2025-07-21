# Robot Dog Commands - Student Guide

## AI Assistance

**GitHub Copilot** (recommended): Click the Copilot button in VS Code (upper right corner)
**ChatGPT**: Copy your code and ask for help

**Stuck?** Ask your instructor to help you find GitHub Copilot!

---

## Challenge 1: Add Commands (Copy & Paste These!)

### Movement Commands

```python
"walk forward": {"command": "kwkF", "description": "Makes the robot walk forward"},
"walk backward": {"command": "kbk", "description": "Makes the robot walk backward"},
"walk left": {"command": "kwkL", "description": "Makes the robot walk left"},
"walk right": {"command": "kwkR", "description": "Makes the robot walk right"},
"trot forward": {"command": "ktrF", "description": "Makes the robot trot forward"},
"crawl forward": {"command": "kcrF", "description": "Makes the robot crawl forward"},
"spin left": {"command": "kvtL", "description": "Makes the robot spin left"},
"spin right": {"command": "kvtR", "description": "Makes the robot spin right"},
```

### Fun Tricks

```python
"jump": {"command": "kjmp", "description": "Makes the robot jump"},
"backflip": {"command": "kbf", "description": "Makes the robot do a backflip"},
"front flip": {"command": "kff", "description": "Makes the robot do a front flip"},
"play dead": {"command": "kpd", "description": "Makes the robot play dead"},
"push ups": {"command": "kpu", "description": "Makes the robot do push-ups"},
"roll": {"command": "krl", "description": "Makes the robot roll"},
"boxing": {"command": "kbx", "description": "Makes the robot box"},
"moonwalk": {"command": "kmw", "description": "Makes the robot moonwalk"},
```

### Interactive Behaviors

```python
"wave": {"command": "kwh", "description": "Makes the robot wave its head"},
"hi": {"command": "khi", "description": "Makes the robot say hi"},
"angry": {"command": "kang", "description": "Makes the robot look angry"},
"high five": {"command": "kfiv", "description": "Makes the robot give a high five"},
"hug": {"command": "khg", "description": "Makes the robot give a hug"},
"nod": {"command": "knd", "description": "Makes the robot nod"},
"cheer": {"command": "kchr", "description": "Makes the robot cheer"},
```

### Utility Commands

```python
"stretch": {"command": "kstr", "description": "Makes the robot stretch"},
"balance": {"command": "kbalance", "description": "Makes the robot balance"},
"recover": {"command": "krc", "description": "Makes the robot recover from falling"},
"sniff": {"command": "ksnf", "description": "Makes the robot sniff"},
"scratch": {"command": "kscrh", "description": "Makes the robot scratch"},
```

**Tips**:

- Copy exactly (quotes, colons, commas)
- Add comma after each line except the last one
- Ask GitHub Copilot: *"Add 10 more robot commands to this dictionary"*

---

## Challenge 2: Responsible AI Transparency

Find the setting that controls what you can see when AI sends commands to the robot. Enable it to see everything the AI does for safety and debugging.

---

## Challenge 3: Command Sequences

Find the setting that enables sequences. Then create multi-step commands like:

```python
"dance": {"sequence": ["kup", "kvtL", "kjmp", "ksit"], "description": "Do a dance routine"},
"morning routine": {"sequence": ["kstr", "kup", "kwh"], "description": "Stretch, stand, wave"},
```

Ask GitHub Copilot: *"How do I make command sequences work in this robot controller?"*

---

## Challenge 4: Connect to Full API (Advanced)

Find the setting that enables full API access. Then implement the function that fetches documentation from the internet.

Ask GitHub Copilot: *"How do I fetch text from a URL using Python's built-in urllib?"*

---

## Quick Example

```python
ROBOT_COMMANDS = {
    "stand up": {"command": "kup", "description": "Makes the robot stand up"},
    "sit down": {"command": "ksit", "description": "Makes the robot sit down"},  
    "rest": {"command": "krest", "description": "Makes the robot rest"},
    
    # Add your commands here!
    "jump": {"command": "kjmp", "description": "Makes the robot jump"},
    "wave": {"command": "kwh", "description": "Makes the robot wave its head"},
}
```
