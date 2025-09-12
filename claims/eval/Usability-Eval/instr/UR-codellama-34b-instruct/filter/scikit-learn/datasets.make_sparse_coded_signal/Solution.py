import numpy as np
from sklearn.feature_extraction import DictionaryLearning
from sklearn.linear_model import SparseCoder

# Generate a random signal
n_samples = 1000
x = np.random.randn(n_samples)

# Define the dictionary elements
dict_elements = np.array([[1, 0], [0, 1]])

# Initialize the DictionaryLearning object with the dictionary elements and the signal
dictionary = DictionaryLearning(dict_elements, n_components=2)

# Fit the dictionary to the signal
dictionary.fit(x)

# Extract the sparse representation of the signal
sparse_representation = SparseCoder(dictionary.components_, alpha=0.1).transform(x)
