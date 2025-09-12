import numpy as np
from sklearn.decomposition import SparsePCA
import matplotlib.pyplot as plt

# Example data matrix
X = np.array([[1, 2, 3, 4, 5],
              [5, 4, 3, 2, 1],
              [2, 3, 4, 5, 6],
              [6, 5, 4, 3, 2]])

# Create a SparsePCA model
# n_components is the number of sparse components to extract
# alpha is the sparsity controlling parameter
n_components = 2
alpha = 1.0

sparse_pca = SparsePCA(n_components=n_components, alpha=alpha, random_state=42)

# Fit the model and transform the data
X_sparse_pca = sparse_pca.fit_transform(X)

# Print results
print("Original Data:")
print(X)
print("\nSparse PCA Components:")
print(sparse_pca.components_)
print("\nTransformed Data:")
print(X_sparse_pca)

# Plot the transformed data
plt.scatter(X_sparse_pca[:, 0], X_sparse_pca[:, 1])
plt.title('Sparse PCA Result')
plt.xlabel('Component 1')
plt.ylabel('Component 2')
plt.show()
