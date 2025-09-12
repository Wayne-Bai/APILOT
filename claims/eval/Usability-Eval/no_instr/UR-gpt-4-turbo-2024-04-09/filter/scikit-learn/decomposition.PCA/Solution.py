import numpy as np
from sklearn.decomposition import PCA

# Sample data
X = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Initialize PCA and reduce dimensionality
pca = PCA(n_components=2)  # Reduce to 2 dimensions

# Fit and transform the input data
X_reduced = pca.fit_transform(X)

print("Reduced data:")
print(X_reduced)
