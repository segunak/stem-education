# Let's assume you've read the Machine Learning example pseudo code.
# There, we took the input (e.g., brightness), multiplied by a weight, made a guess, and adjusted the weight.

# Now, a Neural Network does the same thing, but in layers:
# 1. The input goes into a first layer of "neurons"
# 2. That layer's output becomes the input to a second layer of neurons
# 3. The final layer makes a guess and we adjust weights in BOTH layers if we're wrong

image_data = [0.1, 0.5, 0.7]  # Example input
label = 1  # Correct answer: this image should be recognized as a cat (1 = cat)

# Two layers of weights:
# Layer 1 converts raw input into a simpler pattern
layer_1_weights = [0.2, 0.3, 0.1]  # One simple neuron

# Layer 2 takes that pattern and decides if it's a cat or not
layer_2_weights = [0.4]  # Another simple neuron

learning_rate = 0.1

def simple_neuron(inputs, weights):
    return sum(input_value * weight for input_value, weight in zip(inputs, weights))

# Step 1: Layer 1 processes the input
layer_1_output = [simple_neuron(image_data, layer_1_weights)]

# Step 2: Layer 2 processes Layer 1's output to produce a final guess
final_guess = simple_neuron(layer_1_output, layer_2_weights)

# Check how far off we are (error)
error = label - final_guess

print("Initial Conditions:")
print("  Image Data:", image_data)
print("  Desired Label (Correct Answer):", label)
print("  Layer 1 Weights:", layer_1_weights)
print("  Layer 2 Weights:", layer_2_weights)
print("\nFrom Input to Output:")
print("  Layer 1 Output (pattern from raw data):", layer_1_output)
print("  Final Guess before adjusting weights:", final_guess)
print("  Error (Label - Guess):", error)

# Adjust weights in Layer 2 based on the error
for i in range(len(layer_2_weights)):
    layer_2_weights[i] += learning_rate * error * layer_1_output[i]

# Adjust weights in Layer 1 based on the error and input
for i in range(len(layer_1_weights)):
    layer_1_weights[i] += learning_rate * error * image_data[i] * layer_2_weights[0]

print("\nAfter Adjustments:")
print("  Updated Layer 1 Weights:", layer_1_weights)
print("  Updated Layer 2 Weights:", layer_2_weights)

print("\nIf we passed the same input again now, our guess would likely be closer to the correct answer.")
print("This is how the network 'learns': by tweaking the weights at each layer so that next time,")
print("the same input leads to a guess closer to the correct label (cat in this case).")

print("\nRemember: This is extremely simplified.")
print("Real neural networks have many neurons per layer, more layers, and more complex calculations.")
print("But the idea remains: multiple layers refine the data step-by-step, and adjusting weights")
print("after seeing the error makes the model smarter over time.")