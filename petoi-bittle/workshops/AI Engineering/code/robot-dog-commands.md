# Robot Dog Commands - Easy Copy & Paste Reference

Copy these lines directly into your `ROBOT_COMMANDS` dictionary!

## 🚶 Movement Commands

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

## 🤸 Fun Tricks

```python
"jump": {"command": "kjmp", "description": "Makes the robot jump"},
"backflip": {"command": "kbf", "description": "Makes the robot do a backflip"},
"front flip": {"command": "kff", "description": "Makes the robot do a front flip"},
"play dead": {"command": "kpd", "description": "Makes the robot play dead"},
"push ups": {"command": "kpu", "description": "Makes the robot do push-ups"},
"moonwalk": {"command": "kmw", "description": "Makes the robot moonwalk"},
"roll": {"command": "krl", "description": "Makes the robot roll"},
"boxing": {"command": "kbx", "description": "Makes the robot box"},
```

## 👋 Interactive Behaviors

```python
"wave": {"command": "kwh", "description": "Makes the robot wave its head"},
"hi": {"command": "khi", "description": "Makes the robot say hi"},
"high five": {"command": "kfiv", "description": "Makes the robot give a high five"},
"shake hands": {"command": "khsk", "description": "Makes the robot shake hands"},
"hug": {"command": "khg", "description": "Makes the robot give a hug"},
"nod": {"command": "knd", "description": "Makes the robot nod"},
"cheer": {"command": "kchr", "description": "Makes the robot cheer"},
"angry": {"command": "kang", "description": "Makes the robot look angry"},
```

## 🛠️ Utility Commands

```python
"stretch": {"command": "kstr", "description": "Makes the robot stretch"},
"balance": {"command": "kbalance", "description": "Makes the robot balance"},
"recover": {"command": "krc", "description": "Makes the robot recover from falling"},
"check around": {"command": "kck", "description": "Makes the robot look around"},
"sniff": {"command": "ksnf", "description": "Makes the robot sniff"},
"scratch": {"command": "kscrh", "description": "Makes the robot scratch"},
"dig": {"command": "kdg", "description": "Makes the robot dig"},
"pee": {"command": "kpee", "description": "Makes the robot pretend to pee"},
```

## 💡 Pro Tips

1. **Copy exactly** - The format must match exactly (quotes, colons, commas)
2. **Add a comma** - Don't forget the comma after each line except the last one
3. **Test each one** - Add a few at a time and test before adding more
4. **Be creative** - You can add multiple names for the same command:

   ```python
   "do a flip": {"command": "kbf", "description": "Makes the robot do a backflip"},
   "backflip": {"command": "kbf", "description": "Makes the robot do a backflip"},
   ```

## 🎮 Example: Adding Commands

Here's what your code might look like after adding some commands:

```python
ROBOT_COMMANDS = {
    # Original commands
    "stand up": {"command": "kup", "description": "Makes the robot stand up"},
    "sit down": {"command": "ksit", "description": "Makes the robot sit down"},  
    "rest": {"command": "krest", "description": "Makes the robot rest"},
    
    # Commands you added!
    "jump": {"command": "kjmp", "description": "Makes the robot jump"},
    "wave": {"command": "kwh", "description": "Makes the robot wave its head"},
    "backflip": {"command": "kbf", "description": "Makes the robot do a backflip"},
}
```

## 🤖 Using ChatGPT to Help

Tired of typing? Ask ChatGPT:

> "I have this Python dictionary format for robot commands:  
> 'command_name': {'command': 'code', 'description': 'what it does'}  
> Can you convert these into that format: kbf=backflip, kff=front flip, kjmp=jump"

ChatGPT will format them perfectly for you to copy and paste!
