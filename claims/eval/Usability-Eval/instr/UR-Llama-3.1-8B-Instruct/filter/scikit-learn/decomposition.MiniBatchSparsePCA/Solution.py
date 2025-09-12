# Import necessary libraries
from sklearn.decomposition import SparsePCA
import numpy as np

# Generate a sample dataset
np.random.seed(0)
X = np.random.rand(100, 10)  # 100 samples, 10 features

# Create a Sparse PCA object with 5 components
sparse_pca = SparsePCA(n_components=5, alpha=1.0, max_iter=1000)

# Fit the model to the data
sparse_pca.fit(X)

# Get the transformed data (i.e., the sparse components)
T = sparse_pca.transform(X)

# Get the coefficients of the sparse components
components = sparse_pca.components_

# Print the explained variance ratio for each component
print("Explained variance ratio:")
print(sparse_pca.explained_variance_ratio_)

# Print the number of non-zero features in each component
print("\nNumber of non-zero features in each component:")
for i in range(sparse_pca.n_components_):
    print(f"Component {i+1}: {np.count_nonzero(components[i])}")
