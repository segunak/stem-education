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
import sys
import random

# Path to data file in the same folder
script_dir = os.path.dirname(__file__)
data_file_path = os.path.join(script_dir, "data.txt")

# Read data into a list of words
with open(data_file_path, "r") as f:
    lines = f.readlines()

words = []
for line in lines:
    words.extend(line.strip().split())


LIVE_MODE = False

# Defaults intentionally set to produce "meh" results
DEFAULT_WINDOW_SIZE = 1
DEFAULT_TEMPERATURE = 1.8
FIXED_OUTPUT_LENGTH = 30
DEFAULT_TRAINING_ITERATIONS = 20

MIN_WINDOW_SIZE = 1
MAX_WINDOW_SIZE = 10
MIN_TEMPERATURE = 0.1
MAX_TEMPERATURE = 2.0

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
    This helps avoid missing keys or extremely skewed distributions.
    """
    for key, next_words in markov_dict.items():
        total = sum(next_words.values())
        for w in next_words:
            next_words[w] = (next_words[w] + 1) / (total + len(next_words))

def refine_weights(markov_dict, iterations):
    """
    Light 'training' pass to adjust frequencies and emphasize differences.
    More iterations -> sharper distinctions in frequent vs. rare words.
    """
    for _ in range(iterations):
        for key in markov_dict:
            next_words = markov_dict[key]
            total = sum(next_words.values())
            for w in next_words:
                # small push to highlight frequent words
                next_words[w] = (next_words[w] + 0.05) / (total + 0.05 * len(next_words))

def pick_next_word(markov_dict, key, temperature):
    """
    Given the last 'window_size' words (key), pick the next word using:
    1) The Markov dictionary for possible next words
    2) Temperature-based exponent to weigh probabilities
    3) Weighted random choice
    """
    if key not in markov_dict:
        key = random.choice(list(markov_dict.keys()))
    next_words = markov_dict[key]
    total = sum(next_words.values())

    # Convert raw counts to temperature-adjusted probabilities
    weighted_probs = []
    for w, count in next_words.items():
        freq = count / total
        # exponent for more extreme changes in high vs. low temperature
        freq = freq ** (1.5 / temperature)
        weighted_probs.append((w, freq))

    sum_weights = sum(adj for _, adj in weighted_probs)
    r = random.random() * sum_weights
    cumulative = 0.0
    for w, adj in weighted_probs:
        cumulative += adj
        if r <= cumulative:
            return w

    # fallback
    return weighted_probs[-1][0]

def is_sentence_end(word):
    # Very simple check for sentence-ending punctuation
    return word.endswith(('.', '!', '?', '."', '."')) or word.endswith(("'.", ")?"))

def normalize_text(generated):
    """
    Joins words, does basic sentence splitting, capitalizes first letters.
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

def get_user_input(prompt, default_val, min_val, max_val, cast_type):
    """
    Reusable function to get user input with range checking & defaults.
    If user types 'quit', we exit the script.
    """
    user_in = input(prompt).strip().lower()
    if user_in == 'quit':
        print("Exiting... Goodbye!")
        sys.exit(0)  # or break, but sys.exit is more final
    elif user_in:
        try:
            val = cast_type(user_in)
            if min_val <= val <= max_val:
                return val
            else:
                print(f"Out of range. Using default ({default_val}).")
        except ValueError:
            print(f"Invalid input. Using default ({default_val}).")
    return default_val

def run_markov():
    """
    The main routine that prompts for window_size & temperature once,
    builds/refines the Markov model, generates text, and prints the result.
    """
    print("\n" + ("*" * 50))
    print("Enter settings below. (Press Enter without typing anything to use default values.)")
    print("*" * 50 + "\n")

    print("window_size controls how many previous words the model considers when choosing the next word.")
    print("• Larger window_size → more context, often more coherent text.")
    print("• Smaller window_size → less context, can be more random.\n")

    # 1) Prompt for window_size
    window_size = get_user_input(
        f"Enter a window_size between 1 and 10 [default={DEFAULT_WINDOW_SIZE}]: ",
        DEFAULT_WINDOW_SIZE, MIN_WINDOW_SIZE, MAX_WINDOW_SIZE, int
    )

    print("\ntemperature controls how 'creative' or random the text generation is.")
    print("• Lower temperature (around 0.1-0.5) → more predictable, stable text.")
    print("• Higher temperature (around 1.0-2.0) → more variety, but possibly less coherent.\n")

    # 2) Prompt for temperature
    temperature = get_user_input(
        f"Enter a temperature between 0.1 and 2.0 [default={DEFAULT_TEMPERATURE}]: ",
        DEFAULT_TEMPERATURE, MIN_TEMPERATURE, MAX_TEMPERATURE, float
    )

    # 3) Build / refine Markov dict based on new window_size
    markov_dict = build_markov_dict(window_size)
    smooth_markov_dict(markov_dict)
    refine_weights(markov_dict, DEFAULT_TRAINING_ITERATIONS)

    # 4) Generate text
    start_key = random.choice(list(markov_dict.keys()))
    generated = list(start_key)
    used_words = set(generated)

    # 5) Produce 'FIXED_OUTPUT_LENGTH' words
    for _ in range(FIXED_OUTPUT_LENGTH - window_size):
        current_key = tuple(generated[-window_size:])
        next_word = pick_next_word(markov_dict, current_key, temperature)

        # occasionally skip repeated word
        if next_word in used_words and random.random() > 0.7:
            next_word = random.choice(words)
        generated.append(next_word)
        used_words.add(next_word)

        # end early if we see sentence boundary & have at least half the words
        if is_sentence_end(next_word) and len(generated) > FIXED_OUTPUT_LENGTH // 2:
            break

    # 6) Format and print output
    final_text = normalize_text(generated)
    print("\nGenerated text with your chosen settings:")
    print(f"(window_size={window_size}, temperature={temperature}, length={FIXED_OUTPUT_LENGTH})\n")
    print("*" * 50)
    print(final_text)
    print("*" * 50 + "\n")

print("\n--- 02_markov_improved.py ---\n")
print("Now we use a Markov chain to look at the last few words for context, plus a temperature setting that controls how 'adventurous' the word choices are.\n")
print("This approach is smarter than picking words purely at random, but the quality still depends on your settings—so it's not always perfect!\n")
print(f"Defaults: window_size={DEFAULT_WINDOW_SIZE}, temperature={DEFAULT_TEMPERATURE}, output_length={FIXED_OUTPUT_LENGTH}")
print("\n--- 02_markov_improved.py ---")

try:
    if not LIVE_MODE:
        # Single-run mode
        run_markov()
    else:
        # Live console mode: loop indefinitely
        while True:
            run_markov()
            print("LIVE_MODE is ON. Re-running immediately. Press Ctrl+C to exit.\n")
except KeyboardInterrupt:
    print("\nExiting... Goodbye!")
    sys.exit(0)
