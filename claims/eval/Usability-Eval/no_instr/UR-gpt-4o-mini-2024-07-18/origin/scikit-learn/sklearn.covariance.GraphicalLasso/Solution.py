import numpy as np
from sklearn.covariance import GraphicalLasso

# Simulate some data
np.random.seed(42)
n_samples = 100
n_features = 10
X = np.random.randn(n_samples, n_features)

# Fit the Graphical Lasso model
alpha = 0.1  # Regularization strength
model = GraphicalLasso(alpha=alpha)
model.fit(X)

# Get the estimated covariance matrix
estimated_covariance = model.covariance_
estimated_precision = model.precision_

print("Estimated Covariance Matrix:\n", estimated_covariance)
print("Estimated Precision Matrix:\n", estimated_precision)
