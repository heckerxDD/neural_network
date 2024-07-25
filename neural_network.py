import numpy as np
from nnfs.datasets import spiral_data
import nnfs
import matplotlib.pyplot as plt

nnfs.init()

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def cost_function(expect, actual):
    return -np.mean(expect * np.log(actual) + (1-expect) * np.log(1-actual))

def get_weighted_sum(input, weights):
    # 1. Calculate the weighted sum of inputs and weights
    # weighted_sum = np.dot(weights, input)
    # rewrite above equation in terms of matrix multiplication 
    weighted_sum = np.dot(input, weights.T)
    return weighted_sum

# "layers" is a list containing the number of neurons in each layer
# i.e. [2, 3, 5] would be a network with 3 layers, 
# the first one having 2 neurons, 
# the second one having 3 and the third one having 5
def forward_propagation(inputs, layers):
    layer_output = []
    # print(f'Inputs: {inputs}')
    for n in range(len(layers)):
        # print(f'n is {n}\nlayer has {layers[n]} neurons')
        if n == 0:
            layer_input = inputs
        else:
            layer_input = layer_output
        # print(f'Layer input shape is {layer_input.shape}')
        weights = np.random.randn(layers[n] * layer_input.shape[1]) \
                        .reshape((layers[n], layer_input.shape[1]))
        # print(f'Weights shape is {weights.shape}')
        # weight matrix has the form of (no. of neurons) by (length of input vector)
        bias = np.random.randn(layers[n])
        layer_output_raw = np.add(get_weighted_sum(layer_input, weights), bias)
        layer_output = np.array([sigmoid(i) for i in layer_output_raw])
        # print(f'Layer output shape is {layer_output.shape}')
    return layer_output

input = np.random.randn(8).reshape(2, 4)
layers = [2, 3, 10, 5, 7]
print(forward_propagation(input, layers))

