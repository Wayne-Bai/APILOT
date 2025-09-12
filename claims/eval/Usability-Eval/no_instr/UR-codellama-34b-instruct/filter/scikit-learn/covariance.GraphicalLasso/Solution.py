
import numpy as np
from sklearn.covariance import LedoitWolf

# Generate some random data
n_samples, n_features = 100, 5
np.random.seed(0)
X = np.random.randn(n_samples, n_features)

# Initialize the sparse inverse covariance estimator with l1-penalized estimator
sparse_cov = LedoitWolf(alpha=0.05)

# Fit the model to the data
sparse_cov.fit(X)

# Get the estimated covariance matrix
sparse_cov_matrix = sparse_cov.get_covariance()
