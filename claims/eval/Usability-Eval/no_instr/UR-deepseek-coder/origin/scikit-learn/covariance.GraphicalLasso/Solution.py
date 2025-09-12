import numpy as np
from sklearn.covariance import GraphicalLasso

# Generate some example data
np.random.seed(0)
n_samples, n_features = 60, 20
X = np.random.randn(n_samples, n_features)

# Estimate the sparse inverse covariance matrix
alpha = 0.01  # Regularization parameter
estimator = GraphicalLasso(alpha=alpha)
estimator.fit(X)

# Retrieve the estimated inverse covariance matrix
precision_matrix = estimator.precision_

print("Estimated Precision Matrix:\n", precision_matrix)
