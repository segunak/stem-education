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

# We just pick a sequence of random words, no context or learning.
output_length = 10
generated_words = [random.choice(words) for _ in range(output_length)]

print("\n--- 01_basic_predictor.py ---")
print("Randomly generated words (no context, no learning):\n")
print("*" * 50)
print(" ".join(generated_words))
print("*" * 50)
print("\nObserve how random and nonsensical this is.")
