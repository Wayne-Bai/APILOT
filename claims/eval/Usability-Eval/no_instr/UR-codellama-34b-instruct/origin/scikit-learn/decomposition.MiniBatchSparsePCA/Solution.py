import numpy as np
from sklearn.decomposition import sparse_pca

# Generate some random data
n_samples, n_features = 100, 10
data = np.random.rand(n_samples, n_features)

# Perform SparsePCA with L1 penalty of 0.1
sparse_pca = sparse_pca.SparsePCA(alpha=0.1, n_components=5)
sparse_pca.fit(data)

# Get the sparse components
sparse_components = sparse_pca.components_

# Reconstruct the data from the sparse components
reconstruction = np.dot(sparse_components, data)

print("Sparse components:")
print(sparse_components)
print("\nReconstruction error:")
print(np.linalg.norm(data - reconstruction))
