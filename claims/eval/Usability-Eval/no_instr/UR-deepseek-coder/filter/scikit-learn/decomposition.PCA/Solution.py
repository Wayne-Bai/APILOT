import numpy as np
from sklearn.decomposition import PCA

# Example data
X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])

# Initialize PCA with the desired number of components
pca = PCA(n_components=2, svd_solver='full')

# Fit the PCA model to the data
pca.fit(X)

# Transform the data to the lower dimensional space
X_transformed = pca.transform(X)

print("Original shape:", X.shape)
print("Transformed shape:", X_transformed.shape)
print("Transformed data:", X_transformed)
