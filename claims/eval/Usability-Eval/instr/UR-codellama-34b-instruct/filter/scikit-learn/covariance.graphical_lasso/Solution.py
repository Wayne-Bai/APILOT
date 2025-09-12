from sklearn.covariance import LedoitWolf
import numpy as np

# Generate some sample data
n_samples = 500
n_features = 3
X = np.random.rand(n_samples, n_features)

# Create a L1-penalized covariance estimator object
l1_cov_estimator = LedoitWolf(alpha=1)

# Fit the estimator to the data
l1_cov_estimator.fit(X)

# Get the estimated covariance matrix
l1_cov = l1_cov_estimator.get_covariance()
