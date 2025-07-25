# Robot Dog Commands - Quick Reference

**GitHub Copilot**: Click Copilot button (upper right VS Code) • **ChatGPT**: Copy code and ask for help

## Challenge 1: Copy & Paste Commands

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

## Challenges 2-4: Settings & Advanced

| Challenge | Task | Ask GitHub Copilot |
|---|---|---|
| **2: Transparency** | Find setting to see AI commands | *"How do I enable command visibility?"* |
| **3: Sequences** | Create multi-step commands | *"How do I make command sequences?"* |
| **4: Full API** | Connect to live documentation | *"How do I fetch text from URL with Python?"* |

### Challenge 3: Sequence Example

```python
"dance": {"sequence": ["kup", "kvtL", "kjmp", "ksit"], "description": "Do a dance routine"},
"morning routine": {"sequence": ["kstr", "kup", "kwh"], "description": "Stretch, stand, wave"},
```

**Tips**: Copy exactly (quotes, colons, commas) • Add comma after each line except last • Ask Copilot for help!
