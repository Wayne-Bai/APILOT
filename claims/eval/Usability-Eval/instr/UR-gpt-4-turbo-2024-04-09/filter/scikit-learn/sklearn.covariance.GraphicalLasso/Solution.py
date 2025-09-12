import numpy as np
from sklearn.covariance import GraphicalLasso

# Generate some data: observations from a Gaussian distribution
np.random.seed(0)
n_samples = 60
n_features = 20

# Artificially create covariance with off-diagonal structure
true_cov = np.eye(n_features)
true_cov[0:5, 0:5] = 2

X = np.random.randn(n_samples, n_features)
X[:, 0:5] += np.random.normal(size=(n_samples, 5))

# Fit the GraphicalLasso model
model = GraphicalLasso(alpha=0.25, max_iter=200)
model.fit(X)

# Estimated covariance and precision matrices
estimated_covariance = model.covariance_
estimated_precision = model.precision_

print("Estimated Covariance:\n", estimated_covariance)
print("Estimated Precision:\n", estimated_precision)
