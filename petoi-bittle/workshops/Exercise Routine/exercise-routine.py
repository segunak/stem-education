import time
from PetoiRobot import *

# Function to play Twinkle Twinkle Little Star
def playMelody1():
    play('b', [
        14, 8, 14, 8, 21, 8, 21, 8, 23, 8, 23, 8, 21, 4,
        19, 8, 19, 8, 18, 8, 18, 8, 16, 8, 16, 8, 14, 4,
        21, 8, 21, 8, 19, 8, 19, 8, 18, 8, 18, 8, 16, 4,
        21, 8, 21, 8, 19, 8, 19, 8, 18, 8, 18, 8, 16, 4,
        14, 8, 14, 8, 21, 8, 21, 8, 23, 8, 23, 8, 21, 4,
        19, 8, 19, 8, 18, 8, 18, 8, 16, 8, 16, 8, 14, 4
    ], 0)

# Function to play Happy Birthday
def playMelody2():
    play('b', [
        15, 8, 15, 4, 17, 4, 15, 4, 20, 4, 19, 8,
        15, 8, 15, 4, 17, 4, 15, 4, 22, 4, 20, 8,
        15, 8, 15, 4, 29, 4, 24, 4, 20, 4, 19, 4, 17, 8,
        26, 8, 26, 4, 24, 4, 20, 4, 22, 4, 20, 8
    ], 0)

# Function to play Fur Elise
def playMelody3():
    play(
        'b',
        [
            24, 4, 23, 4, 24, 4, 23, 4, 24, 4, 19, 4, 21, 4, 23, 4,
            0, 4, 14, 4, 16, 4, 18, 4, 19, 4, 18, 4, 16, 4, 14, 4, 0, 4,
            24, 4, 23, 4, 24, 4, 23, 4, 24, 4, 19, 4, 21, 4, 23, 4,
            0, 4, 14, 4, 16, 4, 18, 4, 19, 4, 18, 4, 16, 4, 14, 4
        ],
        2
    )

def playBonusMelody():
    play('b', [
        21, 4, 19, 4, 18, 4, 19, 4, 21, 4, 21, 4, 21, 4, 
        19, 4, 19, 4, 19, 4, 21, 4, 24, 4, 24, 4, 
        21, 4, 19, 4, 18, 4, 19, 4, 21, 4, 21, 4, 21, 4, 
        21, 4, 19, 4, 19, 4, 21, 4, 19, 4, 18, 4
    ], 0)

# Connect to the robot dog
autoConnect()

# Deactivate the voice module
sendSkillStr("XAd 0", 1)

# Sit down
sendSkillStr('ksit', 1)

# Stand up
sendSkillStr('kup', 1)

# Stretch
sendSkillStr('kstr', 1)

# Front flip
sendSkillStr('kff', 1)

# Back flip
sendSkillStr('kbf', 1)

# Handstand
sendSkillStr('khds', 1)

# Continuous jumping
for i in range(5):
    sendSkillStr('kjmp', 0.5)

# Continuous push-ups
for i in range(5):
    sendSkillStr('kpu', 0.5)

# Continuous boxing
for i in range(10):
    sendSkillStr('kbx', 0.3)

# Continuous front flips
for i in range(3):
    sendSkillStr('kff', 3)

# Continuous back flips
for i in range(3):
    sendSkillStr('kbf', 3)

# Pee action
sendSkillStr('kpee', 1)

# Play dead
sendSkillStr('kpd', 1)

# Rest
sendSkillStr('krest', 1)

# Play melodies
playMelody1()
time.sleep(5)

playMelody2()
time.sleep(5)

playMelody3()
time.sleep(5)

# Close the ports
closePort()
