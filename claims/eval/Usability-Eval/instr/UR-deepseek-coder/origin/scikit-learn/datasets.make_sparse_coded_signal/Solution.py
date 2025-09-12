import numpy as np
from sklearn.decomposition import DictionaryLearning

# Generate a random dictionary with 5 atoms
n_components = 5
dictionary = np.random.randn(100, n_components)

# Initialize DictionaryLearning model
dl = DictionaryLearning(n_components=n_components, transform_algorithm='omp', random_state=42)

# Fit the model to the dictionary
dl.fit(dictionary)

# Generate a sparse signal as a combination of dictionary elements
sparse_signal = dl.transform(np.random.randn(1, 100))

# Reconstruct the signal using the dictionary
reconstructed_signal = np.dot(sparse_signal, dl.components_)

print("Sparse Signal:", sparse_signal)
print("Reconstructed Signal:", reconstructed_signal)
