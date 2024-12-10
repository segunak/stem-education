# 02_markov_window.py
#
# In this script, we improve text generation by looking at the sequence of previous words.
# This approach is often called a "Markov Chain." Don't worry about the name—it just means:
# "Look at the last few words to guess what comes next."
#
# Instructions:
# 1. Run the script and follow the prompts in the console.
# 2. You can stick with the defaults for `window_size` and `output_length` or enter your own values.
# 3. Observe how the generated text changes as you adjust these values.
# 4. If you're not sure, start with the defaults and experiment later!
#
# Note: If `window_size` is too large (e.g., larger than the number of words in the training data or `output_length`),
# the program will guide you to choose better values.
#
# After experimenting, move on to the next file.

import os
import random

# Ensure we read `data.txt` from the same directory as this script
script_dir = os.path.dirname(__file__)
data_file_path = os.path.join(script_dir, "data.txt")

# Read the training data
with open(data_file_path, "r") as f:
    lines = f.readlines()

# Create a list of words from the training data
words = []
for line in lines:
    words.extend(line.strip().split())

# Default parameters
default_window_size = 1
default_output_length = 10

# Set bounds for inputs
MIN_WINDOW_SIZE = 1
MAX_WINDOW_SIZE = len(words) - 1  # Ensure there's at least one word left for prediction
MIN_OUTPUT_LENGTH = 5
MAX_OUTPUT_LENGTH = len(words)  # Maximum matches the dataset size

# Prompt for runtime inputs
print("\nWelcome to the Markov Chain text generator!")
print("You'll see how looking at previous words helps predict the next word in a sequence.\n")

print(f"Default settings: window_size = {default_window_size}, output_length = {default_output_length}")
print("If this is your first time running the program, we recommend sticking with the defaults.")
print("To use the defaults, just press 'Enter' when prompted for values.\n")

# Get window_size from the user
print(f"Enter the window_size (default = {default_window_size}, valid range: {MIN_WINDOW_SIZE}-{MAX_WINDOW_SIZE}).")
print("This determines how many previous words the program will look at to guess the next word.")
window_size = input("Press 'Enter' to use the default or type a number: ").strip()
try:
    window_size = int(window_size) if window_size else default_window_size
    if not (MIN_WINDOW_SIZE <= window_size <= MAX_WINDOW_SIZE):
        print(f"\nError: Please enter a window_size between {MIN_WINDOW_SIZE} and {MAX_WINDOW_SIZE}.\n")
        exit()
except ValueError:
    print("\nError: Please enter a valid integer for window_size (e.g., 1, 2, 3).\n")
    exit()

# Get output_length from the user
print(f"\nEnter the output_length (default = {default_output_length}, valid range: {MIN_OUTPUT_LENGTH}-{MAX_OUTPUT_LENGTH}).")
print("This is the total number of words the program will generate in its output.")
output_length = input("Press 'Enter' to use the default or type a number: ").strip()
try:
    output_length = int(output_length) if output_length else default_output_length
    if not (MIN_OUTPUT_LENGTH <= output_length <= MAX_OUTPUT_LENGTH):
        print(f"\nError: Please enter an output_length between {MIN_OUTPUT_LENGTH} and {MAX_OUTPUT_LENGTH}.\n")
        exit()
except ValueError:
    print("\nError: Please enter a valid integer for output_length (e.g., 10, 20, 50).\n")
    exit()

# Validate relationship between window_size and output_length
if window_size >= output_length:
    max_window_size = output_length - 1
    print(f"\nError: The max value you can enter as window_size with output_length ({output_length}) is {max_window_size}.")
    print("\nPlease adjust either the window_size or the output_length and try again.\n")
    exit()

# Build a dictionary of "previous_words -> possible_next_words"
markov_dict = {}
for i in range(len(words) - window_size):
    key = tuple(words[i:i + window_size])
    next_word = words[i + window_size]
    if key not in markov_dict:
        markov_dict[key] = []
    markov_dict[key].append(next_word)

# Generate text
print("\nGenerating text...\n")
start_key = random.choice(list(markov_dict.keys()))
generated = list(start_key)

for _ in range(output_length - window_size):
    curr_key = tuple(generated[-window_size:])
    if curr_key in markov_dict:
        next_word = random.choice(markov_dict[curr_key])
    else:
        next_word = random.choice(words)
    generated.append(next_word)

# Print the generated text
print(f"\nGenerated text with window_size = {window_size} and output_length = {output_length}:\n")
print("\n" + "*" * 50)
print(" ".join(generated))
print("*" * 50 + "\n")
print("Try adjusting the values of `window_size` and `output_length` to see how the output changes!\n")
