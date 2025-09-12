from sklearn.decomposition import SparsePCA
import numpy as np

# Assuming X is your data
X = np.random.rand(100, 500)  # replace this with your actual data

# Initialize the SparsePCA object with the desired number of components and alpha
sparse_pca = SparsePCA(n_components=50, alpha=0.1)

# Fit the model to the data
sparse_pca.fit(X)

# Get the sparse components
sparse_components = sparse_pca.components_

# Get the explained variance
explained_variance = sparse_pca.explained_variance_
