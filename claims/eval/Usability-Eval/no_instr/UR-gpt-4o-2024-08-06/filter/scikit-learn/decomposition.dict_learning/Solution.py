import numpy as np
from sklearn.decomposition import DictionaryLearning

# Generate synthetic data
np.random.seed(0)
n_samples = 10
n_features = 8
X = np.random.randn(n_samples, n_features)

# Set the parameters for dictionary learning
n_components = 4  # Number of dictionary atoms
alpha = 1.0       # Sparsity controlling parameter

# Create a DictionaryLearning model
dict_learning = DictionaryLearning(n_components=n_components, alpha=alpha, max_iter=500, random_state=0)

# Fit the model to the data
X_transformed = dict_learning.fit_transform(X)

# Get the learned dictionary
dictionary = dict_learning.components_

# Output the results
print("Transformed Features:")
print(X_transformed)
print("\nDictionary:")
print(dictionary)
