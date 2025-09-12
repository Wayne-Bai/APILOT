from sklearn.decomposition import MiniBatchKMeans
from sklearn.datasets import make_sparse_coded_signal
import numpy as np

# Generate synthetic data
X, _ = make_sparse_coded_signal(n_samples=1000, n_features=100, n_components=10, random_state=42)

# Initialize MiniBatchKMeans with the desired number of clusters (dictionary atoms)
dict_learning = MiniBatchKMeans(n_clusters=10, random_state=42)

# Fit the model to the data
dict_learning.fit(X)

# Get the learned dictionary
dictionary = dict_learning.cluster_centers_
