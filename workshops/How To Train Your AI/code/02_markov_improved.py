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
fixed_output_length = 30
default_training_iterations = 500

MIN_WINDOW_SIZE = 1
MAX_WINDOW_SIZE = 10
MIN_TEMPERATURE = 0.1
MAX_TEMPERATURE = 2.0

print("\n--- 02_markov_improved.py ---")
print("Now we consider previous words (Markov method) and adjust word selection (temperature).")
print("This should be better than pure random, but might not be perfect.\n")
print(f"Defaults: window_size={default_window_size}, temperature={default_temperature}, output_length={fixed_output_length}")
print("Press Enter for defaults, or try different values.\n")

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

window_size = get_user_input(f"Enter window_size (default={default_window_size}, allowed {MIN_WINDOW_SIZE}-{MAX_WINDOW_SIZE}): ",
                             default_window_size, MIN_WINDOW_SIZE, MAX_WINDOW_SIZE, int)

temperature = get_user_input(f"\nEnter temperature (default={default_temperature}, range {MIN_TEMPERATURE}-{MAX_TEMPERATURE}): ",
                              default_temperature, MIN_TEMPERATURE, MAX_TEMPERATURE, float)

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
def smooth_markov_dict():
    for key, next_words in markov_dict.items():
        total = sum(next_words.values())
        for word in next_words:
            next_words[word] = (next_words[word] + 1) / (total + len(next_words))

# Training loop to refine weights
def refine_weights():
    for _ in range(default_training_iterations):
        for key in markov_dict:
            next_words = markov_dict[key]
            total = sum(next_words.values())
            for word in next_words:
                next_words[word] = (next_words[word] + 0.1) / (total + 0.1 * len(next_words))

smooth_markov_dict()
refine_weights()

def pick_next_word(key):
    if key not in markov_dict:
        key = random.choice(list(markov_dict.keys()))
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

# Function to normalize capitalization and punctuation
def normalize_text(generated):
    text = " ".join(generated)

    # Split into sentences based on common sentence-ending punctuation
    sentences = []
    current_sentence = []
    for word in text.split():
        current_sentence.append(word)
        if is_sentence_end(word):  # Check if the word ends a sentence
            sentences.append(" ".join(current_sentence))
            current_sentence = []

    # Add any remaining words as a final sentence
    if current_sentence:
        sentences.append(" ".join(current_sentence))

    # Capitalize first character of each sentence
    normalized_sentences = []
    for sentence in sentences:
        sentence = sentence.strip()
        if sentence:
            sentence = sentence[0].upper() + sentence[1:]  # Capitalize
            sentence = sentence.replace(" i ", " I ")  # Correct standalone "i"
            normalized_sentences.append(sentence)

    # Join sentences with proper spacing
    return " ".join(normalized_sentences)

# Generate text
print("\nGenerating text with training...\n")
start_key = random.choice(list(markov_dict.keys()))
generated = list(start_key)
used_words = set(generated)  # Track used words to reduce parroting

# Capitalize the first word of the output
if generated:
    generated[0] = generated[0].capitalize()

for i in range(fixed_output_length - window_size):
    curr_key = tuple(generated[-window_size:])
    next_word = pick_next_word(curr_key)

    # Avoid consecutive repetition
    if next_word in used_words and random.random() > 0.5:
        next_word = random.choice(words)
    generated.append(next_word)
    used_words.add(next_word)

    # Break at sentence boundaries
    if is_sentence_end(next_word) and len(generated) >= fixed_output_length // 2:
        break

# Normalize text for capitalization and punctuation
normalized_output = normalize_text(generated)

print(f"Generated text (window_size={window_size}, temperature={temperature}, length={fixed_output_length}):\n")
print("*" * 50)
print(normalized_output)
print("*" * 50 + "\n")

print("Experiment with window_size and temperature for more coherent or creative text.")
print("Observe how adjusting parameters changes the quality of the output!")
print("Notice improvements in avoiding repetitive or parroted text.\n")
