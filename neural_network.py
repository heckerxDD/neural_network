import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def cost_function(expect, actual):
    return -np.mean(expect * np.log(actual) + (1-expect) * np.log(1-actual))

def get_weighted_sum(input, weights):
    # 1. Calculate the weighted sum of inputs and weights
    weighted_sum = np.dot(weights, input)
    return weighted_sum

# "layers" is a list containing the number of neurons in each layer
# i.e. [2, 3, 5] would be a network with 3 layers, 
# the first one having 2 neurons, 
# the second one having 3 and the third one having 5
def forward_propagation(inputs, layers):
    layer_output = []
    for n in range(len(layers)):
        if n == 0:
            layer_input = inputs
        else:
            layer_input = layer_output
        weights = np.random.randn(layers[n] * len(layer_input)) \
                        .reshape((layers[n], len(layer_input)))
        # weight matrix has the form of (no. of neurons) by (length of input vector)
        bias = np.random.randn(layers[n])
        layer_output_raw = np.add(get_weighted_sum(layer_input, weights), bias)
        layer_output = [sigmoid(i) for i in layer_output_raw]
    return layer_output

input = np.random.randn(8)
layers = [2, 3, 5, 10, 4, 1]
print(forward_propagation(input, layers))

