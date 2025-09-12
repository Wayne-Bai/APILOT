from sklearn.decomposition import PCA
import numpy as np

# Assuming X is your input data
X = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Center the data
X_centered = X - np.mean(X, axis=0)

# Apply PCA
pca = PCA(n_components=2)  # Reducing to 2 dimensions
X_pca = pca.fit_transform(X_centered)

print(X_pca)
