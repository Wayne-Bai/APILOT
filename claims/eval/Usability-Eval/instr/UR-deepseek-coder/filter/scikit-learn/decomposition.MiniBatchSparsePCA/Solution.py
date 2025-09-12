import numpy as np
from sklearn.decomposition import SparsePCA

# Example data
X = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Initialize SparsePCA with desired parameters
sparse_pca = SparsePCA(n_components=2, alpha=1.0, random_state=42)

# Fit the model to the data
sparse_pca.fit(X)

# Transform the data to the sparse components
X_transformed = sparse_pca.transform(X)

# Get the sparse components
components = sparse_pca.components_

print("Transformed Data:", X_transformed)
print("Sparse Components:", components)
