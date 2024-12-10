# 02_markov_window.py
#
# In this script, we improve text generation by looking at the sequence of previous words.
# This approach is often called a "Markov Chain." Don't worry about the name—it just means:
# "Look at the last few words to guess what comes next."
#
# The number of previous words we look at is called the "window_size."
# For example:
# - If window_size = 1, we only look at the previous word to guess the next word.
# - If window_size = 2, we look at the previous two words.
#
# Instructions:
# 1. Run this script as is. The default window_size is 1.
# 2. Observe the output—it should look slightly better than random guessing.
# 3. Change the window_size to 2 (instructions near the top of the code) and run again.
# 4. Notice how the output becomes more coherent when the model considers more context.
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

# Set the number of previous words to consider (default = 1).
# TODO: STUDENTS! After running this code once, change `window_size` to 2 and observe the output.
# Then experiment by setting it to different numbers (e.g., 3, 4) and see how the output changes.
# Here's what this does: `window_size = 1` tells your program to only look at the 1 word immediately before
# guessing the next word. `window_size = 2` makes it look at the 2 previous words, and so on.
# Think about how having more context can help YOU, as a human, guess the missing word in a sentence.
# For example:
# - "The ___" (not much context—this could be almost anything!).
# - "The cat sat on the ___" (slightly more context—now "mat" becomes a strong guess).
# - "The cat sat on the mat and slept on the ___" (lots of context—now "bed" is an even better guess!).
# More context = better guesses!
window_size = 40

# Build a dictionary of "previous_words -> possible_next_words"
# Example for window_size = 1:
# If the data contains "The cat sat on the mat," the dictionary would map:
#   ("The",) -> ["cat"]
#   ("cat",) -> ["sat"]
#   ("sat",) -> ["on"]
# For window_size = 2, it would map:
#   ("The", "cat") -> ["sat"]
#   ("cat", "sat") -> ["on"]
markov_dict = {}

for i in range(len(words) - window_size):
    # Create a tuple of the last `window_size` words
    key = tuple(words[i:i + window_size])
    next_word = words[i + window_size]
    if key not in markov_dict:
        markov_dict[key] = []
    markov_dict[key].append(next_word)

# Generate text
# Why 10? It's a small, manageable number that allows you to see the output
# without it being overwhelming. You can change it to experiment with longer outputs.
# For example, set it to 20 to generate a longer sentence.
output_length = 10  # The number of words in the generated text

# Start with a random sequence from the training data
start_key = random.choice(list(markov_dict.keys()))
generated = list(start_key)

# Generate the remaining words
for _ in range(output_length - window_size):
    curr_key = tuple(generated[-window_size:])
    if curr_key in markov_dict:
        # Choose the next word based on the current sequence
        next_word = random.choice(markov_dict[curr_key])
    else:
        # If no matching sequence is found, pick a random word
        next_word = random.choice(words)
    generated.append(next_word)

# Print the generated text
print(f"\nGenerated text with window_size = {window_size}:\n")
print(" ".join(generated))
print(f"\nTry changing 'window_size' in the code from {window_size} to a different number and run again! How does it affect the output? Is it better or worse?")
