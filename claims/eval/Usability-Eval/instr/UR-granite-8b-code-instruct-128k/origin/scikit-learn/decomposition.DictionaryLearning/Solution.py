from sklearn.decomposition import DictionaryLearning
import numpy as np

# Generate some sample data
n_samples, n_features = 100, 1000
X = np.random.randn(n_samples, n_features)

# Initialize the DictionaryLearning object
dict_learning = DictionaryLearning(n_components=100, alpha=1, max_iter=1000)

# Fit the dictionary to the data
dict_learning.fit(X)

# Transform the data using the learned dictionary
X_transformed = dict_learning.transform(X)

# Inverse transform the data using the learned dictionary
X_inverse = dict_learning.inverse_transform(X_transformed)
