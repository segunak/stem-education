# Imagine that we have images represented as pixel brightness values (numbers).
# Each number in the "image" list represents how bright a certain part of the image is.
#
# We're simplifying a lot: we say that "average brightness" might tell us something about whether it's a cat.
# Real AI uses far more complex and numerous features, but this helps us see how learning works:
# We guess, compare to reality, and adjust.

training_data = [
    {"image": [0.1, 0.5, 0.7], "label": 1},  # In our data, this image is a cat.
    {"image": [0.3, 0.2, 0.1], "label": 0},  # In our data, this image is not a cat.
]

# Weight: A single number representing how much we rely on brightness.
# Initially, we have no idea how brightness relates to being a cat, so we start with a guess of 0.5.
#
# The weight is crucial because it's the ONLY thing that changes as we learn.
# By adjusting the weight, we change how the brightness (input) influences our guess.
weight = 0.5

# Learning rate: How quickly we adjust our belief about brightness after seeing each example.
# A small learning rate means we make gentle adjustments, so we don't over correct.
learning_rate = 0.1

print("Beginning training...\n")

for data in training_data:
    image = data["image"]
    label = data["label"]
    
    # Step 1: Make a guess based on brightness.
    # We take the average brightness and multiply it by the weight.
    #
    # Why do we multiply by a weight?
    # Think of the weight as a dial we can turn to adjust how strongly brightness influences our guess.
    # By using weight * brightness, every time we change the weight, we change the output of the guess.
    #
    # Without this multiplication step, we'd have no way to adjust the guess in response to mistakes.
    # The input (brightness) itself doesn't change, so the only way to improve is by tuning the weight.
    # Each time we see how wrong we were and tweak the weight, we're effectively turning the dial so the same brightness leads to a closer-to-correct guess next time.

    average_brightness = sum(image) / len(image)
    guess = weight * average_brightness

    print(f"Image Data: {image}")
    print(f"True Label: {label} (1 = Cat, 0 = Not a Cat)")
    print("Current Weight:", weight)
    print(f"Average Brightness: {average_brightness:.3f}")

    # Here is the core idea:
    # We combine brightness (the input) with weight (our adjustable factor).
    # The guess = (input) * (weight).
    # If guess is close to 1, it means with this weight, brightness suggests 'cat'.
    # If guess is close to 0, it suggests 'not cat'.
    print(f"Initial Guess (Weight * Brightness): {guess:.3f}")
    if guess > 0.5:
        print("  - Guess > 0.5, leaning towards 'cat'.")
    else:
        print("  - Guess <= 0.5, leaning towards 'not cat'.")

    # Step 2: Check how wrong we are.
    # error = label - guess
    # If error is positive, we were too low, so we should increase the weight.
    # If error is negative, we were too high, so we should decrease the weight.
    error = label - guess
    print(f"Error (Label - Guess): {error:.3f}")
    print("  - Positive error: we under-guessed 'cat-likeness'. We'll increase weight.")
    print("  - Negative error: we over-guessed 'cat-likeness'. We'll decrease weight.")

    # Step 3: Adjust the weight.
    # This is where learning happens.
    # By changing weight, next time we multiply the brightness by a slightly different number.
    # Over multiple examples, this shifts our guesses closer to correct answers.
    old_weight = weight
    weight += learning_rate * error
    print(f"Updated Weight: {weight:.3f} (Old: {old_weight:.3f} + (Learning Rate: {learning_rate} * Error: {error:.3f}))")
    print("  - Notice: The input (brightness) didn't change, the label didn't change,")
    print("    but the weight did. On the next guess, the same brightness will produce a different guess,")
    print("    hopefully closer to the truth because we adjusted the weight.\n")

    print("---\n")

print("Training complete.\n")
print(f"Final Weight after seeing all examples: {weight:.3f}\n")
print("This final weight is our 'learned' understanding of how brightness relates to being a cat.")
print("By adjusting the weight each time, we used the exact same input data but got closer to the correct answer.")
print("No input was changed, we just tuned the weight to improve future guesses.\n")