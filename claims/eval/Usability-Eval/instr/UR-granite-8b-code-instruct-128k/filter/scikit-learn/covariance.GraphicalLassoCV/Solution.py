import numpy as np
from sklearn.covariance import GraphLassoCV

# Generate sample data
np.random.seed(42)
n_samples, n_features = 100, 200
X = np.random.randn(n_samples, n_features)

# Estimate covariance using GraphLassoCV
cov = GraphLassoCV().fit(X).covariance_

# Print the estimated covariance matrix
print(cov)
