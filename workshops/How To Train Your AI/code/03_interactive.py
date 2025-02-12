# 03_interactive.py
#
# In this final step, you directly interact with the model:
# - Choose how many words to generate.
# - Choose window_size (how many previous words guide the next choice).
# - Choose temperature (how "predictable" vs. "creative" the word selection is).
# - Provide a starting word (case-insensitive).
# - Simulates training through iterative refinement.
#
# There's no single "right" answer—experiment!
# Try different parameters and starting words to see how they affect the output.
#
# Tips:
# - Higher window_size may yield more coherent text (if your output length is big enough).
# - Lower temperature (e.g., 0.3) is more predictable; higher (e.g., 1.5) is more creative.
# - If unsure which word to start with, pick one from the examples provided.
#
# This demonstrates random → context-aware → interactive → plus improved training logic!

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
DEFAULT_WINDOW_SIZE = 6
DEFAULT_TEMPERATURE = 1.5
DEFAULT_OUTPUT_LENGTH = 30
DEFAULT_TRAINING_ITERATIONS = 500

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

def get_user_input(prompt, default, min_val, max_val, cast_type):
    user_in = input(prompt).strip()
    if user_in.startswith('.'):
        user_in = '0' + user_in

    if user_in:
        try:
            value = cast_type(user_in)
            if min_val <= value <= max_val:
                return value
            else:
                print(f"Out of range. Using default ({default}).")
        except ValueError:
            print(f"Invalid input. Using default ({default}).")
    return default

# Step 1) Prompt for number of words to generate
output_length = get_user_input(
    f"How many words to generate? (default={DEFAULT_OUTPUT_LENGTH}, {MIN_OUTPUT_LENGTH}-{MAX_OUTPUT_LENGTH}): ",
    DEFAULT_OUTPUT_LENGTH, MIN_OUTPUT_LENGTH, MAX_OUTPUT_LENGTH, int
)

# Step 2) Prompt for window_size
max_ws = min(MAX_WINDOW_SIZE, output_length - 1)
window_size = get_user_input(
    f"\nEnter window_size (default={DEFAULT_WINDOW_SIZE}, {MIN_WINDOW_SIZE}-{max_ws}): ",
    DEFAULT_WINDOW_SIZE, MIN_WINDOW_SIZE, max_ws, int
)

# Step 3) Prompt for temperature
temperature = get_user_input(
    f"\nEnter temperature (default={DEFAULT_TEMPERATURE}, {MIN_TEMPERATURE}-{MAX_TEMPERATURE}): ",
    DEFAULT_TEMPERATURE, MIN_TEMPERATURE, MAX_TEMPERATURE, float
)

def build_markov_dict(window_size):
    """
    Build a Markov dictionary keyed by tuples of length=window_size,
    each leading to a dict of possible next words and their counts.
    """
    markov_dict = {}
    for i in range(len(words) - window_size):
        key = tuple(words[i:i + window_size])
        next_word = words[i + window_size]
        if key not in markov_dict:
            markov_dict[key] = {}
        if next_word not in markov_dict[key]:
            markov_dict[key][next_word] = 0
        markov_dict[key][next_word] += 1
    return markov_dict

def smooth_markov_dict(markov_dict):
    """
    Basic smoothing so no next_word has zero probability.
    This helps avoid missing keys or skewed distributions.
    """
    for key, next_words in markov_dict.items():
        total = sum(next_words.values())
        for w in next_words:
            # Add +1, then divide by total + len(next_words)
            next_words[w] = (next_words[w] + 1) / (total + len(next_words))

def refine_weights(markov_dict, iterations):
    """
    Similar to 02_markov_improved:
    A 'light training' pass to emphasize frequent words over multiple iterations.
    Each iteration, we do a small push ( +0.05 ), then re-normalize.
    """
    for _ in range(iterations):
        for key in markov_dict:
            next_words = markov_dict[key]
            total = sum(next_words.values())
            for w in next_words:
                next_words[w] = (next_words[w] + 0.05) / (total + 0.05 * len(next_words))

def pick_next_word(key):
    """
    Picks the next word with temperature-based exponent = (1.5 / temperature)
    for sharper extremes at high vs. low temperatures.
    """
    if key not in markov_dict:
        return random.choice(words)

    next_words = markov_dict[key]
    total = sum(next_words.values())

    # Convert raw count to temperature-adjusted probability
    weighted_probs = []
    for w, count in next_words.items():
        freq = count / total
        freq = freq ** (1.5 / temperature)  # exponent for stronger effect
        weighted_probs.append((w, freq))

    sum_weights = sum(adj for _, adj in weighted_probs)
    r = random.random() * sum_weights
    cumulative = 0
    for w, adj in weighted_probs:
        cumulative += adj
        if r < cumulative:
            return w
    return weighted_probs[-1][0]

markov_dict = build_markov_dict(window_size)
smooth_markov_dict(markov_dict)
refine_weights(markov_dict, DEFAULT_TRAINING_ITERATIONS)

print("\nEnter a starting word (case-insensitive).")
print("Try one of these if you're stuck: 'I', 'The', 'On', 'How'.")
print("If your chosen word does not exist in the training data, we'll choose a random starter.\n")
start_word = input("Starting word: ").strip()
start_word_lower = start_word.lower()

if start_word_lower in words_lower_set:
    # find the case-accurate version
    for w in words:
        if w.lower() == start_word_lower:
            start_word = w
            break
    # build an initial set of words up to window_size
    start_key = [start_word]
    while len(start_key) < window_size:
        start_key.append(random.choice(words))
    generated = list(start_key)
else:
    print("\nThat starting word isn't in the training data. Using a random start.\n")
    chosen_key = random.choice(list(markov_dict.keys()))
    generated = list(chosen_key)

used_words = set(generated)

for i in range(output_length - window_size):
    curr_key = tuple(generated[-window_size:])
    next_word = pick_next_word(curr_key)
    # occasionally skip repeated words
    if next_word in used_words and random.random() > 0.7:
        next_word = random.choice(words)
    generated.append(next_word)
    used_words.add(next_word)

def capitalize_and_punctuate(output):
    """
    Original function from your code, or you can rename it to 'normalize_text'.
    We'll keep it consistent with your existing approach.
    """
    sentences = []
    sentence = []
    for word in output:
        sentence.append(word)
        if (word.endswith(('.', '!', '?', '."', '."')) or
            word.endswith(("'.", ")?"))):
            sentences.append(" ".join(sentence))
            sentence = []
    if sentence:
        sentences.append(" ".join(sentence))
    return ". ".join(sentences).capitalize()

formatted_output = capitalize_and_punctuate(generated)

print(f"Generated text (window_size={window_size}, temperature={temperature}, length={output_length}):\n")
print("*" * 50)
print(formatted_output)
print("*" * 50)

print("\nTry different parameters or a different starting word and run again.")
print("Notice how each choice affects the style and coherence of the output.")
print("Explore and have fun!\n")
