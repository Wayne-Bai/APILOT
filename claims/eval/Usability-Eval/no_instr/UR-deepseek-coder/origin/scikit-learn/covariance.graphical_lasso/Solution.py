import numpy as np
from sklearn.covariance import GraphicalLasso

# Example data
np.random.seed(0)
n_samples, n_features = 50, 10
X = np.random.randn(n_samples, n_features)

# L1-penalized covariance estimator
alpha = 0.01  # Regularization parameter
cov_estimator = GraphicalLasso(alpha=alpha)
cov_estimator.fit(X)

# Estimated covariance matrix
estimated_covariance = cov_estimator.covariance_

# Estimated precision matrix (inverse covariance matrix)
estimated_precision = cov_estimator.precision_

print("Estimated Covariance Matrix:\n", estimated_covariance)
print("Estimated Precision Matrix:\n", estimated_precision)
