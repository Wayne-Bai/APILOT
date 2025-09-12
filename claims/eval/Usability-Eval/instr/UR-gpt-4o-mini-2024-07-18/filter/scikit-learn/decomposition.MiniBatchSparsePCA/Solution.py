from sklearn.decomposition import SparsePCA

# Example data
import numpy as np

# Generating random data
X = np.random.rand(100, 10)

# Applying Sparse PCA
alpha = 1.0  # Penalty term for sparsity
sparsity = 5  # Number of components to extract

sparse_pca = SparsePCA(n_components=sparsity, alpha=alpha)
sparse_pca.fit(X)

# Getting the components
components = sparse_pca.components_

# Transforming the data
X_sparse_pca = sparse_pca.transform(X)

print("Sparse PCA Components:\n", components)
print("Transformed Data:\n", X_sparse_pca)
