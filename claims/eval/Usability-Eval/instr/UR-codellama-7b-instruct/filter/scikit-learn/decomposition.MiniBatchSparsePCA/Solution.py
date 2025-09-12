from sklearn.decomposition import PCA
from sklearn.linear_model import LassoLars
from sklearn.preprocessing import normalize
import numpy as np

# Input data
n_samples, n_features = 100, 5
data = np.random.rand(n_samples, n_features)

# Perform PCA on the data to obtain the sparse components
pca = PCA(n_components=2)
sparse_components = pca.fit_transform(data)

# Add L1 regularization to the PCA coefficients and find the optimal set of coefficients
alpha = 0.5
lasso_lassars = LassoLars(alpha=alpha, random_state=42)
sparse_coefs = lasso_lassars.fit(sparse_components).coefs_

# Reconstruct the data using the sparse components and optimal coefficients
reconstructed_data = np.dot(sparse_components, sparse_coefs)
