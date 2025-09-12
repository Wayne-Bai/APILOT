# Import necessary libraries
from sklearn.decomposition import MiniBatchDictionaryLearning
import numpy as np

# Generate some random data
n_samples = 1000
n_features = 100
X = np.random.randn(n_samples, n_features)

# Initialize the dictionary learning model
dict_learning = MiniBatchDictionaryLearning(n_components=64, batch_size=32, alpha=1.0, n_iter=1000, random_state=42)

# Fit the model to the data
dict_learning.fit(X)

# Print the learned dictionary
print("Learned dictionary:\n", dict_learning.components_)
