# Import necessary libraries
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import numpy as np

# Sample data (you can replace this with your own data)
X = np.array([[2, 2], [2, 3], [3, 1], [4, 4], [4, 5]])

# Standardize features by removing the mean and scaling to unit variance
scaler = StandardScaler()
X_std = scaler.fit_transform(X)

# Apply PCA for dimensionality reduction
pca = PCA(n_components=0.95)  # retain 95% of the variance
X_pca = pca.fit_transform(X_std)

# Transform data back to its original space
X_back = pca.inverse_transform(X_pca)

print("Original Data: \n", X)
print("Data in Principal Component Space: \n", X_pca)
print("Transformed Data back to original space: \n", X_back)
