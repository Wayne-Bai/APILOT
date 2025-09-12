import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# generate some sample data
np.random.seed(0)
X = np.random.randn(10, 5)  # 10 samples, 5 features

# Standardize features by removing the mean and scaling to unit variance
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Initialize PCA
pca = PCA(n_components=3)  # Reduce dimensions from 5 to 3
X_pca = pca.fit_transform(X_scaled)

# Inverse the PCA transformation to get back to the scaled data
X_inverted_pca = pca.inverse_transform(X_pca)

# Inversely transform scaling to get original data
X_original = scaler.inverse_transform(X_inverted_pca)

print("Original Data:\n", X)
print("Reconstructed Data from PCA:\n", X_original)
