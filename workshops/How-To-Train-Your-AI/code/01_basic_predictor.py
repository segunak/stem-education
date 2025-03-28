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

# Split lines into words and get stats
words = []
for line in lines:
    words.extend(line.strip().split())

total_words = len(words)
unique_words = len(set(words))

print("\n=== WELCOME TO AI TRAINING: STEP 1 - PURE RANDOMNESS ===")
print(f"\nAnalyzing training data:")
print(f"• Total words: {total_words}")
print(f"• Unique words: {unique_words}")
print(f"• Vocabulary ratio: {(unique_words/total_words)*100:.1f}%")

print("\nGenerating 3 completely random examples to show why we need better methods:\n")

NUM_EXAMPLES = 3
output_length = 10

for i in range(NUM_EXAMPLES):
    generated_words = [random.choice(words) for _ in range(output_length)]
    print(f"\nExample {i+1}:")
    print("*" * 50)
    print(" ".join(generated_words))
    print("*" * 50)

print("\nWhat did we learn?")
print("1. Random word selection produces nonsense")
print("2. No grammar or meaning because there's no context")
print("3. Each run is completely different - no consistency")
print("\nMove on to 02_markov_improved.py to see how adding")
print("context and probability makes the output more coherent!")
