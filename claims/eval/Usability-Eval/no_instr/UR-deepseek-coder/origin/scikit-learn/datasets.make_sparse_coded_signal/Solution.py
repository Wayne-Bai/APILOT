import numpy as np
from sklearn.decomposition import DictionaryLearning

# Generate a random dictionary with 10 elements and 20 features
n_components = 10
n_features = 20
dictionary = np.random.randn(n_components, n_features)

# Initialize the DictionaryLearning model
dl = DictionaryLearning(n_components=n_components, transform_algorithm='omp', random_state=42)

# Fit the model to the dictionary
dl.fit(dictionary)

# Generate a sparse signal as a combination of dictionary elements
sparse_signal = dl.transform(np.random.randn(1, n_features))

print("Sparse signal:", sparse_signal)
