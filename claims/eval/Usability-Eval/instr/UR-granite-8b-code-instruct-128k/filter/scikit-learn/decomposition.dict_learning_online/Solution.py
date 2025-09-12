from sklearn.decomposition import DictionaryLearning
import numpy as np

# Generate a random data matrix
X = np.random.random((100, 1000))

# Create a DictionaryLearning object
model = DictionaryLearning(n_components=10, alpha=1, n_iter=500)

# Fit the model to the data
model.fit(X)

# Get the dictionary and the sparse code
dictionary = model.components_
sparse_code = model.transform(X)
