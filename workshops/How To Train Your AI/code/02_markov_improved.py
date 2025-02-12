# 02_markov_improved.py
#
# In this script, we improve on the random output from 01_basic_predictor.py by:
# 1. Considering previous words before choosing the next (a Markov chain idea).
# 2. Adjusting how "predictable" or "creative" the choices are (temperature).
# 3. Introducing iterative training to refine the output quality.
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
#    For example, window_size=6 and temperature=1.1 might produce more coherent text.
# 3. Experiment with different values and see what happens.

import os
import random

# Get path to data in the same folder
script_dir = os.path.dirname(__file__)
data_file_path = os.path.join(script_dir, "data.txt")

with open(data_file_path, "r") as f:
    lines = f.readlines()

words = []
for line in lines:
    # Split each line into words and add to the list
    words.extend(line.strip().split())

# Defaults intentionally set to produce "meh" results
default_window_size = 1
default_temperature = 1.8
fixed_output_length = 30

default_training_iterations = 20 

MIN_WINDOW_SIZE = 1
MAX_WINDOW_SIZE = 10
MIN_TEMPERATURE = 0.1
MAX_TEMPERATURE = 2.0

print("\n--- 02_markov_improved.py ---")
print("Now we consider previous words (Markov method) and adjust word selection (temperature).")
print("This should be better than pure random, but might not be perfect.\n")
print(f"Defaults: window_size={default_window_size}, temperature={default_temperature}, output_length={fixed_output_length}")
print("Press Enter for defaults, or try different values.\n")

# Ask user for window_size & temperature
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

window_size = get_user_input(
    f"Enter window_size (default={default_window_size}, allowed {MIN_WINDOW_SIZE}-{MAX_WINDOW_SIZE}): ",
    default_window_size, MIN_WINDOW_SIZE, MAX_WINDOW_SIZE, int
)

temperature = get_user_input(
    f"\nEnter temperature (default={default_temperature}, range {MIN_TEMPERATURE}-{MAX_TEMPERATURE}): ",
    default_temperature, MIN_TEMPERATURE, MAX_TEMPERATURE, float
)

# Build a Markov dictionary keyed by tuples of length=window_size, leading to next_word counts
markov_dict = {}
for i in range(len(words) - window_size):
    key = tuple(words[i:i + window_size])
    next_word = words[i + window_size]
    if key not in markov_dict:
        markov_dict[key] = {}
    if next_word not in markov_dict[key]:
        markov_dict[key][next_word] = 0
    markov_dict[key][next_word] += 1

def smooth_markov_dict():
    """
    Basic smoothing so that no next_word has zero probability.
    This helps avoid missing keys and extremely skewed distributions.
    """
    for key, next_words in markov_dict.items():
        total = sum(next_words.values())
        for w in next_words:
            # Add +1 to each count, then divide by total+len(next_words)
            next_words[w] = (next_words[w] + 1) / (total + len(next_words))

def refine_weights(iterations):
    """
    Extra 'training' pass to push probabilities around.
    Each pass slightly increases each count, emphasizing differences.
    More iterations -> sharper distinctions in frequent vs. rare words.
    """
    for _ in range(iterations):
        for key in markov_dict:
            next_words = markov_dict[key]
            total = sum(next_words.values())
            # We'll do a small push to each next_word
            for w in next_words:
                # This push helps highlight frequent words vs. infrequent
                next_words[w] = (next_words[w] + 0.05) / (total + 0.05 * len(next_words))

# Smooth and refine
smooth_markov_dict()
refine_weights(default_training_iterations)

def pick_next_word(key):
    """
    Given the last 'window_size' words (key), pick the next word.
    We'll:
    1) Grab the dictionary of possible next words & their frequencies
    2) Adjust frequencies further by temperature
       - We use an exponent to amplify or dampen differences
    3) Weighted random choice to pick next_word
    """
    if key not in markov_dict:
        # If unseen combo, pick a random key to keep going
        key = random.choice(list(markov_dict.keys()))
    next_words = markov_dict[key]
    total = sum(next_words.values())

    # Convert raw count to a temperature-adjusted probability
    # (count / total)^(1.2 / temperature) gives bigger extremes
    # for low vs. high temperature than the standard approach
    weighted_probs = []
    for w, count in next_words.items():
        # normalized frequency
        freq = count / total
        # apply exponent for temperature effect
        freq = freq ** (1.5 / temperature)  ### CHANGED: intensify exponent
        weighted_probs.append((w, freq))

    # Now we do a standard weighted random pick from these adjusted frequencies
    sum_of_weights = sum([wp[1] for wp in weighted_probs])
    r = random.random() * sum_of_weights
    cumulative = 0.0
    for w, wp in weighted_probs:
        cumulative += wp
        if r <= cumulative:
            return w

    # fallback if something goes off
    return weighted_probs[-1][0]

def is_sentence_end(word):
    """
    Simple check if a word appears to end a sentence
    (punctuation).
    """
    return word.endswith(('.', '!', '?', '."', '."')) or word.endswith(("'.", ")?"))

def normalize_text(generated):
    """
    Joins words into a string, attempts basic sentence splitting,
    then capitalizes the first letter of each sentence.
    """
    text = " ".join(generated)
    all_words = text.split()
    sentences = []
    current_sentence = []

    for w in all_words:
        current_sentence.append(w)
        if is_sentence_end(w):
            sentences.append(" ".join(current_sentence))
            current_sentence = []
    if current_sentence:
        sentences.append(" ".join(current_sentence))

    # Capitalize each sentence
    final_sentences = []
    for s in sentences:
        s = s.strip()
        if s:
            # Capitalize first letter
            s = s[0].upper() + s[1:]
            final_sentences.append(s)

    return " ".join(final_sentences)

print("\nGenerating text with your chosen settings...\n")

# Start from a random key
start_key = random.choice(list(markov_dict.keys()))
generated = list(start_key)

# We'll keep track of used words just to reduce immediate repetition
used_words = set(generated)

# We'll produce 'fixed_output_length' total words, though might exit early if we see a sentence end
for i in range(fixed_output_length - window_size):
    current_key = tuple(generated[-window_size:])
    next_word = pick_next_word(current_key)

    # occasionally skip a repeated word
    if next_word in used_words and random.random() > 0.7:
        next_word = random.choice(words)
    generated.append(next_word)
    used_words.add(next_word)

    # if we see a sentence end and we've generated over half the words, we might stop
    if is_sentence_end(next_word) and len(generated) > fixed_output_length // 2:
        break

# Normalize final output
final_text = normalize_text(generated)

print(f"Generated text (window_size={window_size}, temperature={temperature}, length={fixed_output_length}):\n")
print("*" * 50)
print(final_text)
print("*" * 50 + "\n")

print("Experiment with window_size and temperature for more coherent or creative text.")
print("Observe how adjusting parameters changes the quality of the output!")
print("Notice improvements in avoiding repetitive or parroted text.\n")
