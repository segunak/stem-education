"""
Prompt Engineering Station Runner

Simple walk up interaction for Petoi Bittle X
- Natural language prompts
- No idle auto actions (robot rests until a student prompts)
- Friendly prompt label for students
"""

import sys
import os
import time
import random

BASE_DIR = os.path.dirname(__file__)
LIB_DIR = os.path.abspath(os.path.join(BASE_DIR, '..', 'lib'))
if LIB_DIR not in sys.path:
    sys.path.append(LIB_DIR)

from robot_controller import RobotAI
from robot_commands import FULL_COMMANDS, SEQUENCE_COMMANDS

# Config toggles (edit as needed)
ENABLE_SEQUENCES = True
ENABLE_FULL_API = False  # True to pull live spec context
SHOW_COMMANDS = True     # Transparency of mapped commands
API_URL = "https://raw.githubusercontent.com/segunak/stem-education/refs/heads/master/petoi-bittle/documentation/petoi-python-api-specification.md"

# User prompt label
PROMPT_LABEL = "Prompt > "  # Shown when asking for user input

HELP_TEXT = """
USAGE
  Just type what you want the robot dog to do in natural language

BASIC COMMANDS
  wave                    Wave hello
  jump                    Jump in place
  front flip              Do a front flip
  backflip                Do a backflip
  roll over               Roll over
  moon walk               Moonwalk backwards
  sit                     Sit down
  rest                    Lie down and rest
  balance                 Balance on hind legs
  stretch                 Stretch routine
  celebrate               Victory celebration

CREATIVE PROMPTS
  make a routine          Create a custom sequence
  act sleepy              Show tired behavior
  act like a hero         Strike heroic poses
  surprise me             Random cool moves

SEQUENCES
  You can chain multiple actions together:
    backflip then wave then sit
    walk forward then spin left then celebrate
    stretch then jump then rest

COMMANDS
  help                    Show this help
  quit                    Exit the program
""".strip()


def merged_commands():
    cmds = FULL_COMMANDS.copy()
    for k, v in SEQUENCE_COMMANDS.items():
        if k not in cmds:
            cmds[k] = v
    return cmds


def explain_quit():
    print("\nTo quit type: quit and press Enter")
    print("You can also press Ctrl+C once")
    print()


def main():
    print("🐶 Prompt Engineering Station")
    print("Type a prompt to control the robot dog")
    print("Type help for ideas   Type quit to exit")

    robot = RobotAI(
        commands=merged_commands(),
        show_commands=SHOW_COMMANDS,
        enable_sequences=ENABLE_SEQUENCES,
        enable_full_api=ENABLE_FULL_API,
        api_url=API_URL if ENABLE_FULL_API else None
    )

    # Show help only after connection / setup
    print()
    print(HELP_TEXT)
    print()
    explain_quit()

    try:
        while True:
            try:
                text = input(PROMPT_LABEL).strip()
            except EOFError:
                # If terminal sends EOF treat as quit
                break
            if not text:
                continue
            if text.lower() in {"quit", "exit"}:
                break
            if text.lower() in {"help", "?", "ideas"}:
                print("\n" + HELP_TEXT + "\n")
                explain_quit()
                continue
            print("Thinking...", flush=True)
            robot._handle_user_message(text)
            # After completion show a blank line for clarity
            print()
    except KeyboardInterrupt:
        pass
    finally:
        print("\nResting and closing port...")
        try:
            from PetoiRobot import sendSkillStr, closePort  # noqa: WPS433
            sendSkillStr("krest", 1)
            closePort()
        except Exception:
            pass
        print("Done.")


if __name__ == "__main__":
    main()
