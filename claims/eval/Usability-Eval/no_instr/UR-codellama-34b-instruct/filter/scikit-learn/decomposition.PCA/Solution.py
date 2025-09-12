from sklearn.decomposition import PCA
import numpy as np

# Generate some sample data
np.random.seed(0)
n_samples = 1000
n_features = 10
X = np.random.rand(n_samples, n_features)

# Center the data but not scale it for each feature
X_centered = X - X.mean(axis=0)

# Perform PCA on the centered data
pca = PCA(n_components=2, whiten=False)
X_transformed = pca.fit_transform(X_centered)
