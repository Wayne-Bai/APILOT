import numpy as np
from sklearn.decomposition import DictionaryLearning

# Generate a random dictionary
np.random.seed(0)
n_components = 100
n_features = 200
dictionary = np.random.rand(n_components, n_features)

# Generate a random sparse signal
n_samples = 100
signal = np.zeros((1, n_features))
sparse_weights = np.random.rand(n_components)
sparse_weights[sparse_weights < .95] = 0
active_components = np.random.randint(0, n_components, size=10)
signal[:, :n_components] = np.dot(sparse_weights[active_components, np.newaxis], dictionary[active_components, :])

# Instantiate the DictionaryLearning model
model = DictionaryLearning(n_components=n_components, random_state=0)

# Fit the model to the data
model.fit(signal)

# Generate a sparse combination of dictionary elements
sparse_signal = model.transform(signal)
sparse_signal
