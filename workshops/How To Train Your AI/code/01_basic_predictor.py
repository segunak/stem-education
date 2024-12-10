# 01_basic_predictor.py
#
# In this script, we pick words at random to form sentences, without any learning.
# Instructions:
# 1. Just run this code by clicking the "Run" button.
# 2. Observe the output in the terminal below.
# 3. Notice that the output does not resemble your training text at all—it's random.
#
# After this, you'll move on to the next file where we start adding some intelligence.

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

# Currently, we just pick 10 random words from the dataset.
# No context, no pattern, just random picking.
output_length = 10
generated_words = [random.choice(words) for _ in range(output_length)]

print("\nRandomly generated words (no learning, no context):\n")
print(" ".join(generated_words))
