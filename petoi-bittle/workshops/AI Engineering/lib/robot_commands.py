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
    "front flip": {"command": "kff", "description": "Makes the robot do a front flip"},
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
    
    # Robot Arm Commands (for Bittle X+Arm models)
    "pick up front": {"command": "kpickF", "description": "Pick up object in front of the robotic arm"},
    "pick up left": {"command": "kpickL", "description": "Pick up object to the left of the robotic arm"},
    "pick up right": {"command": "kpickR", "description": "Pick up object to the right of the robotic arm"},
    "pick up down": {"command": "kpickD", "description": "Pick up object under the robotic arm"},
    "pick up": {"command": "kpick", "description": "Pick up object (random direction)"},
    
    "put down front": {"command": "kputF", "description": "Place object in front of the robotic arm"},
    "put down left": {"command": "kputL", "description": "Place object to the left of the robotic arm"},
    "put down right": {"command": "kputR", "description": "Place object to the right of the robotic arm"},
    "put down": {"command": "kputD", "description": "Place object under the robotic arm"},
    "put": {"command": "kput", "description": "Place object (random direction)"},
    
    "drop front": {"command": "kdropF", "description": "Drop object in front"},
    "drop left": {"command": "kdropL", "description": "Drop object to the left"},
    "drop right": {"command": "kdropR", "description": "Drop object to the right"},
    "drop down": {"command": "kdropD", "description": "Drop object down"},
    "drop": {"command": "kdrop", "description": "Drop object (random direction)"},
    
    "toss front": {"command": "ktossF", "description": "Throw object forward"},
    "toss left": {"command": "ktossL", "description": "Throw object to the left"},
    "toss right": {"command": "ktossR", "description": "Throw object to the right"},
    "toss": {"command": "ktoss", "description": "Throw object (random direction)"},
    "launch": {"command": "klaunch", "description": "Launch object forward"},
    
    "hunt": {"command": "khunt", "description": "Quickly grasp object in front"},
    "show off": {"command": "kshowOff", "description": "Show the grasped object"},
    "clap": {"command": "kclap", "description": "Make clapping motion with gripper"},
    
    # Additional documented movement variants
    "walk left": {"command": "kwkL", "description": "Makes the robot walk left"},
    "walk right": {"command": "kwkR", "description": "Makes the robot walk right"},
    "back left": {"command": "kbkL", "description": "Makes the robot move backward left"},
    "back right": {"command": "kbkR", "description": "Makes the robot move backward right"},
    "trot forward": {"command": "ktrF", "description": "Makes the robot trot forward"},
    "trot left": {"command": "ktrL", "description": "Makes the robot trot left"},
    "trot right": {"command": "ktrR", "description": "Makes the robot trot right"},
    "crawl forward": {"command": "kcrF", "description": "Makes the robot crawl forward"},
    "crawl left": {"command": "kcrL", "description": "Makes the robot crawl left"},
    "crawl right": {"command": "kcrR", "description": "Makes the robot crawl right"},
    "bound forward": {"command": "kbdF", "description": "Makes the robot bound forward"},
    "jump forward": {"command": "kjpF", "description": "Makes the robot jump forward"},
    "spin left": {"command": "kvtL", "description": "Makes the robot spin left"},
    "spin right": {"command": "kvtR", "description": "Makes the robot spin right"},
    "stepping": {"command": "kvtF", "description": "Makes the robot step at origin"},
    
    # Additional posture / state commands
    "balance": {"command": "kbalance", "description": "Makes the robot stand balanced"},
    "recover": {"command": "krc", "description": "Makes the robot recover from a fall"},
    "table": {"command": "ktbl", "description": "Makes the robot form a table pose"},
    "landing": {"command": "klnd", "description": "Makes the robot do a landing pose"},
    "dropped": {"command": "kdropped", "description": "Makes the robot show dropped pose"},
    "lifted": {"command": "klifted", "description": "Makes the robot show lifted pose"},
    
    # Interactive behaviours and gestures
    "come here": {"command": "kcmh", "description": "Makes the robot beckon come here"},
    "handshake": {"command": "khsk", "description": "Makes the robot shake hands"},
    "high five": {"command": "kfiv", "description": "Makes the robot give high five"},
    "hands up": {"command": "khu", "description": "Makes the robot raise hands"},
    "pray": {"command": "kpry", "description": "Makes the robot pray"},
    "thank": {"command": "kthk", "description": "Makes the robot show thanks"},
    "good boy": {"command": "kgdb", "description": "Good boy behaviour"},
    
    # Maintenance / test / sleep
    "test": {"command": "kts", "description": "Run test mode"},
    "sleep": {"command": "kzz", "description": "Makes the robot sleep"},
}

# Sequence commands for Challenge 3 (these get added dynamically)
SEQUENCE_COMMANDS = {
    # Basic routines
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
    },
    
    # Athletic routines
    "workout": {
        "description": "Complete athletic workout session",
        "sequence": ["kstr", "kpu", "kpu", "kjmp", "kbf", "kbalance", "kstr", "krest"]
    },
    "athlete mode": {
        "description": "Show off athletic abilities",
        "sequence": ["kbf", "kff", "kjmp", "khs", "kbalance", "kwh"]
    },
    "fitness demo": {
        "description": "Fitness demonstration routine",
        "sequence": ["kstr", "kpu", "kjmp", "kbalance", "ktr", "krest"]
    },
    "parkour": {
        "description": "Parkour-style movement sequence",
        "sequence": ["kjpF", "kbdF", "kff", "krc", "kwkF", "kjmp"]
    },
    
    # Entertainment routines
    "entertainment": {
        "description": "Full entertainment package",
        "sequence": ["khi", "kwh", "kbf", "kjmp", "kbx", "kwh", "krest"]
    },
    "party time": {
        "description": "Party celebration routine",
        "sequence": ["kwh", "kjmp", "kvtL", "kvtR", "kfiv", "kwh"]
    },
    "comedy show": {
        "description": "Funny routine to make people laugh",
        "sequence": ["kpee", "kscrh", "kdd", "kup", "kwh", "khi"]
    },
    "circus act": {
        "description": "Circus performer routine",
        "sequence": ["khs", "kbalance", "kbf", "kff", "kwh", "khi"]
    },
    
    # Character routines
    "superhero": {
        "description": "Strike heroic superhero poses",
        "sequence": ["khu", "kbalance", "khi", "kwh", "kfiv"]
    },
    "guard dog": {
        "description": "Alert guard dog behavior",
        "sequence": ["ksnf", "kck", "kang", "khi"]
    },
    "playful puppy": {
        "description": "Cute playful puppy behavior",
        "sequence": ["kwh", "kjmp", "kscrh", "kwh", "krest"]
    },
    "sleepy pet": {
        "description": "Tired pet routine",
        "sequence": ["kstr", "krest", "kshy", "kzz"]
    },
    "excited pet": {
        "description": "Excited happy pet behavior",
        "sequence": ["kjmp", "kwh", "kvtL", "kvtR", "kwh"]
    },
    
    # Social interaction routines
    "meet and greet": {
        "description": "Polite introduction routine",
        "sequence": ["khi", "kwh", "khsk", "kthk", "kwh"]
    },
    "celebration": {
        "description": "Victory celebration routine",
        "sequence": ["kjmp", "kwh", "kfiv", "kvtL", "kvtR", "kwh"]
    },
    "farewell": {
        "description": "Goodbye routine",
        "sequence": ["kwh", "kthk", "khsk", "kwh", "krest"]
    },
    "thank you": {
        "description": "Grateful thank you routine",
        "sequence": ["kthk", "kpry", "kwh", "khi"]
    },
    
    # Storytelling routines
    "adventure story": {
        "description": "Act out an adventure story",
        "sequence": ["kwkF", "ksnf", "kck", "kbf", "krc", "kwh", "khi"]
    },
    "mystery solver": {
        "description": "Detective investigating a mystery",
        "sequence": ["ksnf", "kck", "kwkF", "kscrh", "khi", "kwh"]
    },
    "ninja mode": {
        "description": "Stealthy ninja routine",
        "sequence": ["kcrF", "khs", "kbf", "kbalance", "khi"]
    },
    
    # Interactive games
    "follow the leader": {
        "description": "Interactive follow routine",
        "sequence": ["kwkF", "kL", "kR", "kjmp", "krest"]
    },
    "simon says": {
        "description": "Simon says game routine",
        "sequence": ["kwh", "kjmp", "kvtL", "ksit", "kup"]
    },
    "peek a boo": {
        "description": "Playful peek-a-boo game",
        "sequence": ["kdd", "kup", "kwh", "kdd", "kup", "khi"]
    },
    
    # Emotional expression routines
    "happy dance": {
        "description": "Express pure happiness",
        "sequence": ["kjmp", "kwh", "kvtL", "kvtR", "kjmp", "khi"]
    },
    "confused": {
        "description": "Show confusion and curiosity",
        "sequence": ["kscrh", "kL", "kR", "ksnf", "kshy"]
    },
    "dramatic": {
        "description": "Dramatic theatrical performance",
        "sequence": ["khu", "kbalance", "kdd", "kup", "kwh", "khi"]
    },
    "zen mode": {
        "description": "Peaceful meditation routine",
        "sequence": ["kbalance", "kpry", "kstr", "krest"]
    },
    
    # Skill demonstration routines
    "balance master": {
        "description": "Show off balance skills",
        "sequence": ["kbalance", "khs", "kbalance", "kup", "kbalance"]
    },
    "flip master": {
        "description": "Master of flips and tricks",
        "sequence": ["kbf", "kff", "kbf", "kwh", "khi"]
    },
    "movement demo": {
        "description": "Demonstrate all movement types",
        "sequence": ["kwkF", "kbk", "ktrF", "kcrF", "kjmp", "krest"]
    },
    
    # Surprise routines
    "random fun": {
        "description": "Unpredictable fun sequence",
        "sequence": ["kpee", "kbf", "kwh", "kscrh", "kjmp", "khi"]
    },
    "surprise me": {
        "description": "Unexpected entertaining routine",
        "sequence": ["khs", "kbf", "kwh", "kfiv", "krest"]
    },
    "wild card": {
        "description": "Completely random behavior",
        "sequence": ["kbx", "kmw", "kbf", "kwh", "krest"]
    }
}
