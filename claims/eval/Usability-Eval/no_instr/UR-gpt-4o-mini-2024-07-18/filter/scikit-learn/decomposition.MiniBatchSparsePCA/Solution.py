from sklearn.decomposition import SparsePCA
import numpy as np

# Example data
X = np.random.rand(10, 5)  # 10 samples, 5 features

# Set the sparsity level with alpha
alpha = 1.0  # Adjust this value to control sparsity
sparse_pca = SparsePCA(alpha=alpha, n_components=3)

# Fit the Sparse PCA model
sparse_pca.fit(X)

# Transform the data
X_sparse = sparse_pca.transform(X)

# Display the components
print("Sparse Components:\n", sparse_pca.components_)
print("Transformed Data:\n", X_sparse)
