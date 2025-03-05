# In our Machine Learning example, we had one layer.
# In our Neural Networks example, we had two layers.
# In Deep Learning, we have many layers, each doing the same "multiply inputs by weights and add them up" step.

# Example input (just pretend it's some data, like image pixels or text embeddings)
input_data = [0.1, 0.5, 0.7]

# Instead of 1 or 2 layers, let's say we have multiple layers.
# Each layer has its own set of weights.
# (In reality, you might have dozens or hundreds of layers, each with many neurons, but we'll keep it tiny.)

layer_1_weights = [0.2, 0.3, 0.1]
layer_2_weights = [0.4, 0.6]
layer_3_weights = [0.5, 0.5]
# Imagine more layers if needed, many, many, many more layers…

def simple_neuron(inputs, weights):
    return sum(i * w for i, w in zip(inputs, weights))

# Process the data step-by-step through each layer:
layer_1_output = [simple_neuron(input_data, layer_1_weights)]
layer_2_output = [simple_neuron(layer_1_output, layer_2_weights)]
layer_3_output = [simple_neuron(layer_2_output, layer_3_weights)]
# …and so on, until a final layer gives us a final_guess.

# final_guess is the model's prediction after passing through all these layers.
final_guess = layer_3_output[0]

label = 1  # Suppose the correct answer is still "cat"
error = label - final_guess

# Adjusting weights (just like before, but now we do it for every layer):
learning_rate = 0.1

# For simplicity, let's just show one adjustment:
for i in range(len(layer_3_weights)):
    layer_3_weights[i] += learning_rate * error * layer_2_output[i]

# And similarly, we'd adjust layer_2_weights and layer_1_weights based on their inputs and the error feedback.

print("Deep Learning:")
print("  We passed data through multiple layers.")
print("  Each layer transforms the data a bit more, allowing the model to learn very complex patterns.")
print("  If we find an error, we adjust the weights in all these layers, gradually improving the model's predictions.")
print("  This is how deep learning models, like those powering ChatGPT, get so good at their tasks over time.")