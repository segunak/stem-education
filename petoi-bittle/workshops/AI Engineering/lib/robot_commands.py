"""
Robot Commands Library
======================

This file contains all the robot commands for the AI Engineering workshop.
- BASIC_COMMANDS: Used in Challenge 1 for manual learning
- FULL_COMMANDS: Auto-loaded in Challenges 2+ for advanced concepts
"""

# Basic commands that students start with in Challenge 1
BASIC_COMMANDS = {
    "stand up": {"command": "kup", "description": "Makes the robot stand up"},
    "sit down": {"command": "ksit", "description": "Makes the robot sit down"},
    "rest": {"command": "krest", "description": "Makes the robot rest"},
}

# Full command set - auto-loaded for Challenges 2+
FULL_COMMANDS = {
    # Basic commands (what students learn in Challenge 1)
    **BASIC_COMMANDS,
    
    # Movement commands
    "jump": {"command": "kjmp", "description": "Makes the robot jump"},
    "wave": {"command": "kwh", "description": "Makes the robot wave"},
    "backflip": {"command": "kbf", "description": "Makes the robot do a backflip"},
    "walk forward": {"command": "kwkF", "description": "Makes the robot walk forward"},
    "walk backward": {"command": "kbk", "description": "Makes the robot walk backward"},
    "turn left": {"command": "kL", "description": "Makes the robot turn left"},
    "turn right": {"command": "kR", "description": "Makes the robot turn right"},
    "moonwalk": {"command": "kmw", "description": "Makes the robot moonwalk"},
    "crawl": {"command": "kcr", "description": "Makes the robot crawl"},
    "trot": {"command": "ktr", "description": "Makes the robot trot"},
    "pace": {"command": "kpc", "description": "Makes the robot pace"},
    "bound": {"command": "kbd", "description": "Makes the robot bound"},
    "walk": {"command": "kwk", "description": "Makes the robot walk"},
    
    # Action commands
    "greet": {"command": "khi", "description": "Makes the robot greet"},
    "handstand": {"command": "khs", "description": "Makes the robot do a handstand"},
    "stretch": {"command": "kstr", "description": "Makes the robot stretch"},
    "pushup": {"command": "kpu", "description": "Makes the robot do pushups"},
    "roll": {"command": "krl", "description": "Makes the robot roll"},
    "play dead": {"command": "kdd", "description": "Makes the robot play dead"},
    "pee": {"command": "kpee", "description": "Makes the robot pee"},
    "scratch": {"command": "kscrh", "description": "Makes the robot scratch"},
    "sniff": {"command": "ksnf", "description": "Makes the robot sniff"},
    "check": {"command": "kck", "description": "Makes the robot check around"},
    
    # Emotional expressions
    "angry": {"command": "kang", "description": "Makes the robot show anger"},
    "shy": {"command": "kshy", "description": "Makes the robot act shy"},
    "buttUp": {"command": "kbuttUp", "description": "Makes the robot put its butt up"},
    "calib": {"command": "kcalib", "description": "Makes the robot calibrate"},
    
    # Fun tricks
    "boxing": {"command": "kbx", "description": "Makes the robot box"},
    "test": {"command": "ktest", "description": "Makes the robot run a test"},
    "zero": {"command": "kzero", "description": "Makes the robot go to zero position"},
}

# Sequence commands for Challenge 3 (these get added dynamically)
SEQUENCE_COMMANDS = {
    "dance": {
        "description": "Makes the robot dance with multiple moves",
        "sequence": ["kwh", "kbf", "kjmp", "kwh"]
    },
    "morning routine": {
        "description": "Robot's morning exercise routine", 
        "sequence": ["kstr", "kpu", "kjmp", "krest"]
    },
    "show off": {
        "description": "Robot shows off its best tricks",
        "sequence": ["khs", "kbf", "kwh", "khi"]
    }
}
