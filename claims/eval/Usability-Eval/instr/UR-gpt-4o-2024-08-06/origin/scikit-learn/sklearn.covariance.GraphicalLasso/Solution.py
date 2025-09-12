import numpy as np
from sklearn.covariance import graphical_lasso

# Generate synthetic data
n_samples = 100
n_features = 20
np.random.seed(0)

# Create some data with covariance
X = np.random.randn(n_samples, n_features)
X -= X.mean(axis=0)

# Estimate the sparse inverse covariance
alpha = 0.01  # regularization parameter
covariance, precision = graphical_lasso(np.cov(X, rowvar=False), alpha)

print("Estimated covariance matrix: \n", covariance)
print("Estimated precision matrix (inverse covariance): \n", precision)
