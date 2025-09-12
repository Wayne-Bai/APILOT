import numpy as np
from sklearn.covariance import GraphicalLasso

# Example data
np.random.seed(0)
n_samples, n_features = 60, 20
X = np.random.randn(n_samples, n_features)

# Estimate the sparse inverse covariance
alpha = 0.01  # Regularization parameter
estimator = GraphicalLasso(alpha=alpha)
estimator.fit(X)

# Estimated inverse covariance matrix
precision_matrix = estimator.precision_

# Estimated covariance matrix
covariance_matrix = estimator.covariance_

print("Estimated Precision Matrix:\n", precision_matrix)
print("Estimated Covariance Matrix:\n", covariance_matrix)
