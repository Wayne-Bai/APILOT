from sklearn.decomposition import DictionaryLearning
import numpy as np

# Generate a random dictionary and a sparse code
n_samples, n_features = 100, 500
dictionary = np.random.random((n_features, 10))
code = np.random.random((n_samples, 10))

# Generate a data matrix from the dictionary and the sparse code
data = np.dot(dictionary, code)

# Initialize the DictionaryLearning object with the correct shape
model = DictionaryLearning(n_components=10, algorithm='lasso_lars', alpha=1, max_iter=1000)

# Fit the model to the data matrix
model.fit(data)

# Print the learned dictionary
print("Learned dictionary:")
print(model.components_)
