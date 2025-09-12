from sklearn.decomposition import MiniBatchDictionaryLearning
from sklearn.datasets import make_sparse_coded_signal
import numpy as np

# Generate a random sparse coded signal
X, _ = make_sparse_coded_signal(n_samples=1000, n_features=100, n_components=10, random_state=0)

# Initialize MiniBatchDictionaryLearning with the desired number of components
mbdl = MiniBatchDictionaryLearning(n_components=10, random_state=0)

# Fit the model to the data
mbdl.fit(X)

# Get the learned dictionary
D = mbdl.components_

# Get the learned codes
C = mbdl.transform(X)
