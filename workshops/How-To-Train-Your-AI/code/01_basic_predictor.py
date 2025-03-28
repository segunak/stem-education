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

print("\n=== STEP 1: RANDOM TEXT GENERATION ===")
print("-" * 50)
print(f"Training data stats:")
print(f"• Total words: {total_words}")
print(f"• Unique words: {unique_words}")

print("\nGenerating 3 random examples...")
print("(Notice how they make no sense!)\n")

NUM_EXAMPLES = 3
output_length = 10

for i in range(NUM_EXAMPLES):
    generated_words = [random.choice(words) for _ in range(output_length)]
    print(f"Example {i+1}:")
    print("=" * 50)
    print(" ".join(generated_words))
    print("=" * 50 + "\n")

print("What we learned:")
print("• Random words = nonsense text")
print("• No context = no meaning")
print("• We need a smarter approach!")

print("\n>>> Next step: Run 02_markov_improved.py to see how adding")
print("              context makes the output more coherent.\n")
