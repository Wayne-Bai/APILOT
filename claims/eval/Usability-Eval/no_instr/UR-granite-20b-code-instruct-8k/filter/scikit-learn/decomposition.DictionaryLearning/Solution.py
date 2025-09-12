from sklearn.decomposition import SparseDictionaryLearning
import numpy as np

# Generate random data
n_samples = 100
n_features = 200
X = np.random.rand(n_samples, n_features)

# Perform dictionary learning
dict_learning = SparseDictionaryLearning(n_components=10, alpha=0.1)
dict_learning.fit(X)

# Get the dictionary
dictionary = dict_learning.components_

# Get the sparse coding
sparse_coding = dict_learning.transform(X)
