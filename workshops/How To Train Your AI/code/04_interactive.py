# 04_interactive.py
#
# Welcome to the interactive mode!
# In this script, you interact directly with the model:
# 1. Provide a starting word when prompted.
# 2. The model will generate text based on the training data and your input.
#
# Instructions:
# 1. Run the script and follow the prompts.
# 2. Adjust `window_size`, `temperature`, or the number of words to generate interactively.
# 3. Observe how the output changes based on your settings.
#
# Remember: This model was trained on a small dataset. It won't behave like ChatGPT.
# It simply predicts based on patterns in the provided data.

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
default_window_size = 2
default_temperature = 0.3
default_output_length = 20

# Input bounds
MIN_WINDOW_SIZE = 1
MAX_WINDOW_SIZE = len(words) // 2  # Half the dataset size
MIN_OUTPUT_LENGTH = 5
MAX_OUTPUT_LENGTH = 50
MIN_TEMPERATURE = 0.1
MAX_TEMPERATURE = 2.0

# Welcome message
print("\nWelcome to the interactive mode!")
print("You'll see how adjusting input and model parameters influences text generation.\n")

# Get `output_length` from the user
print(f"Enter the number of words to generate (default = {default_output_length}, valid range: {MIN_OUTPUT_LENGTH}-{MAX_OUTPUT_LENGTH}).")
output_length = input("Press 'Enter' to use the default or type a number: ").strip()
try:
    output_length = int(output_length) if output_length else default_output_length
    if not (MIN_OUTPUT_LENGTH <= output_length <= MAX_OUTPUT_LENGTH):
        print(f"\nError: Please enter an output_length between {MIN_OUTPUT_LENGTH} and {MAX_OUTPUT_LENGTH}.\n")
        exit()
except ValueError:
    print("\nError: Please enter a valid integer for output_length (e.g., 10, 20).\n")
    exit()

# Recalculate valid `window_size` range based on `output_length`
MAX_WINDOW_SIZE = output_length - 1
print(f"\nEnter the window_size (default = {default_window_size}, valid range: {MIN_WINDOW_SIZE}-{MAX_WINDOW_SIZE}).")
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

# Get `temperature` from the user
print(f"\nEnter the temperature (default = {default_temperature}, valid range: {MIN_TEMPERATURE}-{MAX_TEMPERATURE}).")
print("Lower temperature makes output predictable, higher temperature adds randomness.")
temperature = input("Press 'Enter' to use the default or type a number: ").strip()
try:
    temperature = float(temperature) if temperature else default_temperature
    if not (MIN_TEMPERATURE <= temperature <= MAX_TEMPERATURE):
        print(f"\nError: Please enter a temperature between {MIN_TEMPERATURE} and {MAX_TEMPERATURE}.\n")
        exit()
except ValueError:
    print("\nError: Please enter a valid number for temperature (e.g., 0.5, 1.0).\n")
    exit()

# Build a dictionary of "previous_words -> possible_next_words"
markov_dict = {}
for i in range(len(words) - window_size):
    key = tuple(words[i:i + window_size])
    next_word = words[i + window_size]
    if key not in markov_dict:
        markov_dict[key] = {}
    if next_word not in markov_dict[key]:
        markov_dict[key][next_word] = 0
    markov_dict[key][next_word] += 1

# Define function to pick next word based on frequency and temperature
def pick_next_word(key):
    if key not in markov_dict:
        return random.choice(words)
    word_freqs = markov_dict[key]
    total = sum(word_freqs.values())
    freqs = [(word, (count / total) ** (1 / temperature)) for word, count in word_freqs.items()]
    re_total = sum(freq for _, freq in freqs)
    scaled_probs = [(word, freq / re_total) for word, freq in freqs]
    r = random.random()
    cumulative = 0
    for word, prob in scaled_probs:
        cumulative += prob
        if r < cumulative:
            return word
    return scaled_probs[-1][0]

# Prompt user for a starting word
print("\nEnter a single starting word. The model will try to continue from there.")
start_word = input("Starting word: ").strip()

# Validate the starting word
if start_word not in words:
    print("\nThat starting word isn't in the training data. Picking a random starting point...\n")
    start_key = random.choice(list(markov_dict.keys()))
    generated = list(start_key)
else:
    start_key = [start_word]
    if window_size > 1:
        start_key.append(random.choice(words))
    generated = start_key[:window_size]

# Generate text
print("\nGenerating text...\n")
for _ in range(output_length - window_size):
    curr_key = tuple(generated[-window_size:])
    next_word = pick_next_word(curr_key)
    generated.append(next_word)

# Print the generated text
print(f"\nGenerated text with window_size = {window_size}, temperature = {temperature}, and output_length = {output_length}:\n")
print("\n" + "*" * 50)
print(" ".join(generated))
print("*" * 50 + "\n")
print("Try adjusting `window_size`, `temperature`, or `output_length` to explore different outputs!\n")
