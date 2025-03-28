# 02_markov_improved.py
#
# What is the Markov Method?
# -------------------------
# Imagine writing a sentence. After each word, you look back at what you just wrote
# to decide what word should come next. That's basically what the Markov method does!
#
# For example, if you wrote "The cat", your brain knows that words like "sat", "walked",
# or "jumped" would make sense next, but "banana" probably wouldn't.
#
# The Markov method works the same way:
# 1. It looks at the last few words (called the "window")
# 2. Checks what words often came next in similar situations in its training data
# 3. Picks one of those words as the next word in the sequence
#
# In this script, you control:
# 1. window_size: How many previous words to look at (like context/memory)
# 2. temperature: How "creative" vs "safe" the word choices should be
#
# Lower temperature (0.1-0.5) = Picks common/predictable next words
# Higher temperature (1.0-2.0) = More willing to try unusual combinations
#
# Instructions:
# 1. First run with defaults (just press Enter when asked)
# 2. Then try window_size=3, temperature=0.7 
# 3. Finally experiment with your own values!

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
    # If we don't have this exact key, pick a random one from what we know
    if key not in markov_dict:
        # Let's be transparent about fallbacks
        print(f"\nDebug: No exact match for sequence '{' '.join(key)}', using random fallback...")
        return random.choice(words)  # Fall back to any word from training data
    
    next_words = markov_dict[key]
    total = sum(next_words.values())

    # Convert raw counts to temperature-adjusted probabilities
    weighted_probs = []
    for w, count in next_words.items():
        freq = count / total
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
    print("\n=== STEP 2: ADDING CONTEXT AND CREATIVITY ===")
    print("-" * 50)
    
    print("\nSet two parameters to control the output:")
    print("1. window_size: How many previous words to consider")
    print("2. temperature: How creative vs predictable to be\n")

    print("WINDOW SIZE:")
    print("• Small (1-2): Basic word-to-word connections")
    print("• Medium (3-5): Phrase-level patterns")
    print("• Large (6-10): Full sentence coherence")
    
    window_size = get_user_input(
        f"\nEnter window_size ({MIN_WINDOW_SIZE}-{MAX_WINDOW_SIZE}) [default={DEFAULT_WINDOW_SIZE}]: ",
        DEFAULT_WINDOW_SIZE, MIN_WINDOW_SIZE, MAX_WINDOW_SIZE, int
    )

    print("\nTEMPERATURE:")
    print("• Low (0.1-0.5): Safe, predictable choices")
    print("• Medium (0.6-1.0): Balanced creativity")
    print("• High (1.1-2.0): Wild, experimental text")
    
    temperature = get_user_input(
        f"\nEnter temperature ({MIN_TEMPERATURE}-{MAX_TEMPERATURE}) [default={DEFAULT_TEMPERATURE}]: ",
        DEFAULT_TEMPERATURE, MIN_TEMPERATURE, MAX_TEMPERATURE, float
    )

    print("\nGenerating text with your settings...")
    # Build Markov model
    print("\nBuilding language model...")
    markov_dict = build_markov_dict(window_size)
    print("Smoothing probabilities...")
    smooth_markov_dict(markov_dict)
    print(f"Training model ({DEFAULT_TRAINING_ITERATIONS} iterations)...")
    refine_weights(markov_dict, DEFAULT_TRAINING_ITERATIONS)

    # Generate multiple examples with same settings
    NUM_EXAMPLES = 2
    print(f"\nGenerating {NUM_EXAMPLES} examples with your settings:")
    print(f"(window_size={window_size}, temperature={temperature})\n")

    # Add debug info during generation
    print("\nWatching the AI think...")
    for i in range(NUM_EXAMPLES):
        print(f"\nGenerating Example {i+1}:")
        start_key = random.choice(list(markov_dict.keys()))
        generated = list(start_key)
        used_words = set(generated)

        for _ in range(FIXED_OUTPUT_LENGTH - window_size):
            current_key = tuple(generated[-window_size:])
            
            # Show what we're trying to predict from
            if random.random() < 0.3:  # 30% chance to show debug
                print("\nDebug: Looking at last few words:", " ".join(current_key))
                # Only show probabilities if we have this sequence
                if current_key in markov_dict:
                    next_words = markov_dict[current_key]
                    print("Possible next words (with probabilities):")
                    for word, prob in sorted(next_words.items(), key=lambda x: x[1], reverse=True)[:5]:
                        print(f"  • '{word}': {prob:.2f}")

            next_word = pick_next_word(markov_dict, current_key, temperature)
            
            # Avoid repetition
            if next_word in used_words and random.random() > 0.7:
                next_word = random.choice(words)
            
            generated.append(next_word)
            used_words.add(next_word)

            if is_sentence_end(next_word) and len(generated) > FIXED_OUTPUT_LENGTH // 2:
                break

        final_text = normalize_text(generated)
        print(f"\nOutput {i+1}:")
        print("=" * 50)
        print(final_text)
        print("=" * 50)

    print("\nWant better results?")
    print("• More coherent: Use window_size=5-6")
    print("• More creative: Increase temperature")
    print("• More stable: Decrease temperature")

    print("\n>>> Next step: Run 03_interactive.py to control")
    print("              both parameters and starting words!\n")

print("\n--- WORD PREDICTION EXPERIMENT ---\n")
print("In this step, we're teaching the computer to predict words like humans do!")
print("When you read 'The cat sat on the ___', you can probably guess 'mat' or 'chair'.")
print("That's because you've seen similar patterns in other sentences before.\n")
print("Now we'll help the computer learn to make these kinds of predictions.\n")
print("You'll control HOW it learns through two important settings:")
print(" 1. How many previous words it considers (window_size)")
print(" 2. How creative it gets with its guesses (temperature)\n")

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
