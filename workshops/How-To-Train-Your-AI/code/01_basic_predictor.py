# 01_basic_predictor.py
#
# In this script, we pick words at random to form sentences, without any learning or context.
# Instructions:
# 1. Run this code by clicking the "Run" button.
# 2. Observe the output in the terminal below.
# 3. Notice that the output does not resemble your training text at all—it's random.
#
# After this, you'll move on to the next file (02_markov_improved.py) where we start adding some intelligence,
# such as considering previous words (Markov chains) and probability weighting.
#
# The goal of this file is to show you the starting point: pure randomness, no understanding.

import os
import random

# Ensure the script always reads data.txt from the same directory as this script
script_dir = os.path.dirname(__file__)
data_file_path = os.path.join(script_dir, "data.txt")

# Read the data
with open(data_file_path, "r") as f:
    lines = f.readlines()

# Split lines into words
words = []
for line in lines:
    words.extend(line.strip().split())

# Generate multiple examples to show randomness
NUM_EXAMPLES = 3
output_length = 10

print("\n--- 01_basic_predictor.py ---")
print("Showing multiple random outputs to demonstrate complete lack of pattern:\n")

for i in range(NUM_EXAMPLES):
    generated_words = [random.choice(words) for _ in range(output_length)]
    print(f"Example {i+1}:")
    print("*" * 50)
    print(" ".join(generated_words))
    print("*" * 50)
    print()

print("\nNotice how each output is completely different and makes no sense!")
print("This is because we're just picking words at random with no context or learning.")
print("Check data.txt to see the training data, then move on to 02_markov_improved.py")
