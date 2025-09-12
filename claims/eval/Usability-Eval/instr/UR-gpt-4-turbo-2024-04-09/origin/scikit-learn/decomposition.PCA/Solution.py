import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# Sample data: rows are samples, columns are features
X = np.array([[1, 2], [3, 4], [5, 6]])

# Centering the data
scaler = StandardScaler(with_mean=True, with_std=False)
X_centered = scaler.fit_transform(X)

# Applying PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_centered)

print("Original Data:")
print(X)
print("PCA Transformed Data:")
print(X_pca)
