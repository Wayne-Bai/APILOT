import numpy as np
from sklearn.decomposition import SparsePCA

# Create a random dictionary
np.random.seed(42)
dictionary = np.random.rand(100, 20)

# Generate a random sparse combination of dictionary elements
sparse_signal = np.dot(np.random.normal(size=(20, 50)), dictionary)

# Perform sparse PCA
sparse_pca = SparsePCA(n_components=5)
sparse_pca.fit(sparse_signal)

# Transform the sparse signal
transformed_signal = sparse_pca.transform(sparse_signal)

transformed_signal
