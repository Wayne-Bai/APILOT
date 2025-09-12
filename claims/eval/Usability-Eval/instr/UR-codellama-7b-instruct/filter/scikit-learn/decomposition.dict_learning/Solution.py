
import numpy as np
from sklearn.decomposition import DictionaryLearning

# Generate sample data
n_samples = 100
n_features = 50
n_components = 3
X = np.random.rand(n_samples, n_features)

# Create the dictionary learning model
dictionary_learning = DictionaryLearning(n_components=n_components, random_state=42)

# Fit the model to the data
dictionary_learning.fit(X)

# Generate a new matrix of samples from the learned dictionary
new_samples = dictionary_learning.transform(n_samples)
