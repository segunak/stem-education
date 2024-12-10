# 02_markov_improved.py
#
# In this script, we improve on the random output from 01_basic_predictor.py by:
# 1. Considering previous words before choosing the next (a Markov chain idea).
# 2. Adjusting how "predictable" or "creative" the choices are (temperature).
#
# Markov Chain Concept (Simple Version):
# Instead of picking the next word randomly, we look at the last 'window_size' words.
# We then choose a next word based on how often it followed those words in the training text.
#
# window_size: How many previous words we consider (1 to 10).
#  - Larger window_size = more context = often more coherent text.
#
# temperature: Controls how we pick from the possible next words (0.1 to 2.0).
#  - Lower temperature (e.g. 0.2) = more predictable and coherent.
#  - Higher temperature (e.g. 1.0) = more variety, but can be less coherent.
#
# Instructions:
# 1. Run once with defaults by pressing Enter. Compare to 01_basic_predictor.py output.
#    You should see some improvement, but maybe not great.
# 2. Then rerun and try different settings:
#    For example, window_size=2 and temperature=0.5 might produce more coherent text.
# 3. Experiment with different values and see what happens.
#
# After experimenting here, move on to 03_interactive.py.

import os
import random

script_dir = os.path.dirname(__file__)
data_file_path = os.path.join(script_dir, "data.txt")

with open(data_file_path, "r") as f:
    lines = f.readlines()

words = []
for line in lines:
    words.extend(line.strip().split())

# Not-so-ideal defaults, encouraging experimentation:
default_window_size = 1
default_temperature = 1.0
fixed_output_length = 20

MIN_WINDOW_SIZE = 1
MAX_WINDOW_SIZE = 10
MIN_TEMPERATURE = 0.1
MAX_TEMPERATURE = 2.0

print("\n--- 02_markov_improved.py ---")
print("Now we consider previous words (Markov method) and adjust word selection (temperature).")
print("This should be better than pure random, but might not be perfect.\n")

print(f"Defaults: window_size={default_window_size}, temperature={default_temperature}, output_length={fixed_output_length}")
print("Press Enter for defaults, or try different values.\n")
print("Hint: After seeing the defaults, try window_size=2 and temperature=0.5 for more coherence.\n")

# Get window_size
print(f"Enter window_size (default={default_window_size}, allowed {MIN_WINDOW_SIZE}-{MAX_WINDOW_SIZE}):")
ws_input = input("Press Enter or type a number: ").strip()
if ws_input:
    try:
        window_size = int(ws_input)
        if not (MIN_WINDOW_SIZE <= window_size <= MAX_WINDOW_SIZE):
            print(f"\nInvalid. Using default ({default_window_size}).")
            window_size = default_window_size
    except ValueError:
        print(f"\nInvalid. Using default ({default_window_size}).")
        window_size = default_window_size
else:
    window_size = default_window_size

# Get temperature
print(f"\nEnter temperature (default={default_temperature}, {MIN_TEMPERATURE}-{MAX_TEMPERATURE}):")
t_input = input("Press Enter or type a number: ").strip()
if t_input:
    try:
        temperature = float(t_input)
        if not (MIN_TEMPERATURE <= temperature <= MAX_TEMPERATURE):
            print(f"\nInvalid. Using default ({default_temperature}).")
            temperature = default_temperature
    except ValueError:
        print(f"\nInvalid. Using default ({default_temperature}).")
        temperature = default_temperature
else:
    temperature = default_temperature

# Build a dictionary of which words tend to follow which sequences
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
    # If this sequence hasn't been seen, pick a random word
    if key not in markov_dict:
        return random.choice(words)
    word_freqs = markov_dict[key]
    total = sum(word_freqs.values())
    # Adjust frequencies by temperature
    freqs = [(w, (count/total)**(1/temperature)) for w, count in word_freqs.items()]
    re_total = sum(freq for _, freq in freqs)
    probs = []
    for w, freq in freqs:
        probs.append((w, freq/re_total))
    r = random.random()
    cum = 0
    for w, p in probs:
        cum += p
        if r < cum:
            return w
    return probs[-1][0]

print("\nGenerating text...\n")
start_key = random.choice(list(markov_dict.keys()))
generated = list(start_key)

for _ in range(fixed_output_length - window_size):
    curr_key = tuple(generated[-window_size:])
    next_word = pick_next_word(curr_key)
    generated.append(next_word)

print(f"Generated text (window_size={window_size}, temperature={temperature}, length={fixed_output_length}):\n")
print("*" * 50)
print(" ".join(generated))
print("*" * 50 + "\n")

print("Compare this to the random output from 01_basic_predictor.py.")
print("It's using context now, so it might be slightly better.")
print("Try different window_size and temperature values. For example, window_size=2, temperature=0.5")
print("It might give more coherent results. Experiment!")

