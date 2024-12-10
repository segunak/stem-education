# 03_interactive.py
#
# In this final step, you directly interact with the model:
# - Choose how many words to generate.
# - Choose window_size (how many previous words guide the next choice).
# - Choose temperature (how "predictable" vs. "creative" the word selection is).
# - Provide a starting word (case-insensitive).
#
# There's no single "right" answer—experiment!
# Try different parameters and starting words to see how they affect the output.
#
# Tips:
# - A higher window_size may yield more coherent text if you have enough output length.
# - Lower temperature (e.g., 0.3) gives more predictable text, higher (e.g., 1.0) adds variety.
# - If unsure which word to start with, pick one from the examples provided.
#
# This builds on everything you've learned: random → context-aware → interactive.
# Have fun exploring!

import os
import random

script_dir = os.path.dirname(__file__)
data_file_path = os.path.join(script_dir, "data.txt")

with open(data_file_path, "r") as f:
    lines = f.readlines()

words = []
for line in lines:
    words.extend(line.strip().split())

# Prepare a lowercase set for case-insensitive checking of the starting word
words_lower = [w.lower() for w in words]
words_lower_set = set(words_lower)

# Default parameters
default_window_size = 2
default_temperature = 0.3
default_output_length = 20

# Allowed ranges
MIN_WINDOW_SIZE = 1
MAX_WINDOW_SIZE = 50
MIN_OUTPUT_LENGTH = 5
MAX_OUTPUT_LENGTH = 50
MIN_TEMPERATURE = 0.1
MAX_TEMPERATURE = 2.0

print("\n--- 03_interactive.py ---")
print("Welcome to interactive mode! Here you choose the parameters and a starting word.")
print("Experiment with different settings and see how the output changes.\n")

# Get output_length
print(f"How many words to generate? (default={default_output_length}, {MIN_OUTPUT_LENGTH}-{MAX_OUTPUT_LENGTH})")
ol_input = input("Press Enter for default or type a number: ").strip()
try:
    output_length = int(ol_input) if ol_input else default_output_length
    if not (MIN_OUTPUT_LENGTH <= output_length <= MAX_OUTPUT_LENGTH):
        print(f"\nError: Please pick a number between {MIN_OUTPUT_LENGTH} and {MAX_OUTPUT_LENGTH}.\n")
        exit()
except ValueError:
    print("\nError: Please enter a valid integer.\n")
    exit()

# window_size must be less than output_length
max_ws = min(MAX_WINDOW_SIZE, output_length - 1)
if max_ws < MIN_WINDOW_SIZE:
    max_ws = MIN_WINDOW_SIZE

print(f"\nEnter window_size (default={default_window_size}, {MIN_WINDOW_SIZE}-{max_ws}).")
ws_input = input("Press Enter for default or type a number: ").strip()
try:
    window_size = int(ws_input) if ws_input else default_window_size
    if not (MIN_WINDOW_SIZE <= window_size <= max_ws):
        print(f"\nError: window_size must be between {MIN_WINDOW_SIZE} and {max_ws}.\n")
        exit()
except ValueError:
    print("\nError: Please enter a valid integer.\n")
    exit()

print(f"\nEnter temperature (default={default_temperature}, {MIN_TEMPERATURE}-{MAX_TEMPERATURE}).")
print("Lower=more predictable, Higher=more variety. For example, try 0.5 or 1.0.")
t_input = input("Press Enter for default or type a number: ").strip()
try:
    temperature = float(t_input) if t_input else default_temperature
    if not (MIN_TEMPERATURE <= temperature <= MAX_TEMPERATURE):
        print(f"\nError: temperature must be between {MIN_TEMPERATURE} and {MAX_TEMPERATURE}.\n")
        exit()
except ValueError:
    print("\nError: Please enter a valid number.\n")
    exit()

# Build Markov dictionary
markov_dict = {}
for i in range(len(words) - window_size):
    key = tuple(words[i:i+window_size])
    next_word = words[i+window_size]
    if key not in markov_dict:
        markov_dict[key] = {}
    if next_word not in markov_dict[key]:
        markov_dict[key][next_word] = 0
    markov_dict[key][next_word] += 1

def pick_next_word(key):
    if key not in markov_dict:
        return random.choice(words)
    word_freqs = markov_dict[key]
    total = sum(word_freqs.values())
    freqs = [(w, (count/total)**(1/temperature)) for w, count in word_freqs.items()]
    re_total = sum(freq for _, freq in freqs)
    probs = [(w, freq/re_total) for w, freq in freqs]
    r = random.random()
    cum = 0
    for w, p in probs:
        cum += p
        if r < cum:
            return w
    return probs[-1][0]

print("\nEnter a starting word (case-insensitive).")
print("Try one of these for interesting results: Alice, May, On, I, The.")
print("If your chosen word does not exist in the training data, we'll choose a random starter for you.")
start_word = input("Starting word: ").strip()
start_word_lower = start_word.lower()

if start_word_lower in words_lower_set:
    # Find the original-cased version of the chosen word
    for w in words:
        if w.lower() == start_word_lower:
            start_word = w
            break
    # Initialize context
    start_key = [start_word]
    while len(start_key) < window_size:
        start_key.append(random.choice(words))
    generated = start_key[:window_size]
else:
    print("\nThat starting word isn't in the training data. Using a random start.\n")
    start_key = random.choice(list(markov_dict.keys()))
    generated = list(start_key)

print("\nGenerating text...\n")

for _ in range(output_length - window_size):
    curr_key = tuple(generated[-window_size:])
    generated.append(pick_next_word(curr_key))

print(f"Generated text (window_size={window_size}, temperature={temperature}, length={output_length}):")
print("*" * 50)
print(" ".join(generated))
print("*" * 50)

print("\nTry different parameters or a different starting word and run again.")
print("Notice how each choice affects the style and coherence of the output.")
print("Explore and have fun!\n")
