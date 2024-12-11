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
default_window_size = 6
default_temperature = 0.4
default_output_length = 30

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

# Get user input with validation
def get_user_input(prompt, default, min_val, max_val, cast_type):
    user_input = input(prompt).strip()
    if user_input:
        try:
            value = cast_type(user_input)
            if min_val <= value <= max_val:
                return value
            else:
                print(f"Out of range. Using default ({default}).")
        except ValueError:
            print(f"Invalid input. Using default ({default}).")
    return default

output_length = get_user_input(
    f"How many words to generate? (default={default_output_length}, {MIN_OUTPUT_LENGTH}-{MAX_OUTPUT_LENGTH}): ",
    default_output_length, MIN_OUTPUT_LENGTH, MAX_OUTPUT_LENGTH, int
)

max_ws = min(MAX_WINDOW_SIZE, output_length - 1)
window_size = get_user_input(
    f"\nEnter window_size (default={default_window_size}, {MIN_WINDOW_SIZE}-{max_ws}): ",
    default_window_size, MIN_WINDOW_SIZE, max_ws, int
)

temperature = get_user_input(
    f"\nEnter temperature (default={default_temperature}, {MIN_TEMPERATURE}-{MAX_TEMPERATURE}): ",
    default_temperature, MIN_TEMPERATURE, MAX_TEMPERATURE, float
)

# Build Markov dictionary with smoothing
markov_dict = {}
for i in range(len(words) - window_size):
    key = tuple(words[i:i + window_size])
    next_word = words[i + window_size]
    if key not in markov_dict:
        markov_dict[key] = {}
    if next_word not in markov_dict[key]:
        markov_dict[key][next_word] = 0
    markov_dict[key][next_word] += 1

# Add smoothing to all keys
for key, next_words in markov_dict.items():
    total = sum(next_words.values())
    for word in next_words:
        next_words[word] = (next_words[word] + 1) / (total + len(next_words))

def pick_next_word(key):
    if key not in markov_dict:
        return random.choice(words)
    word_freqs = markov_dict[key]
    total = sum(word_freqs.values())

    # Adjust frequencies by temperature
    freqs = [(w, (count / total) ** (1 / temperature)) for w, count in word_freqs.items()]
    re_total = sum(freq for _, freq in freqs)
    probs = [(w, freq / re_total) for w, freq in freqs]

    # Weighted random choice
    r = random.random()
    cum = 0
    for w, p in probs:
        cum += p
        if r < cum:
            return w
    return probs[-1][0]

def is_sentence_end(word):
    return word.endswith(('.', '!', '?', '."', '."')) or word.endswith(("'.", ")?"))

def capitalize_and_punctuate(output):
    sentences = []
    sentence = []
    for word in output:
        sentence.append(word)
        if is_sentence_end(word):
            sentences.append(" ".join(sentence))
            sentence = []
    if sentence:
        sentences.append(" ".join(sentence))
    return ". ".join(sentences).capitalize()

print("\nEnter a starting word (case-insensitive).")
print("Try one of these if you're stuck: I, The, On, How.")
print("If your chosen word does not exist in the training data, we'll choose a random starter for you.")
start_word = input("Starting word: ").strip()
start_word_lower = start_word.lower()

if start_word_lower in words_lower_set:
    for w in words:
        if w.lower() == start_word_lower:
            start_word = w
            break
    start_key = [start_word]
    while len(start_key) < window_size:
        start_key.append(random.choice(words))
    generated = start_key[:window_size]
else:
    print("\nThat starting word isn't in the training data. Using a random start.\n")
    start_key = random.choice(list(markov_dict.keys()))
    generated = list(start_key)

print("\nGenerating text...\n")

for i in range(output_length - window_size):
    curr_key = tuple(generated[-window_size:])

    # Dynamically adjust temperature based on position
    dynamic_temperature = temperature + (i / output_length) * 0.3  # Increase slightly over time
    next_word = pick_next_word(curr_key)

    generated.append(next_word)

formatted_output = capitalize_and_punctuate(generated)

print(f"Generated text (window_size={window_size}, temperature={temperature}, length={output_length}):\n")
print("*" * 50)
print(formatted_output)
print("*" * 50)

print("\nTry different parameters or a different starting word and run again.")
print("Notice how each choice affects the style and coherence of the output.")
print("Explore and have fun!\n")
