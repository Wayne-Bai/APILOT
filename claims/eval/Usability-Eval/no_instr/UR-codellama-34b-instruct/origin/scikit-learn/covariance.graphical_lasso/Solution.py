
import numpy as np
from sklearn.covariance import GraphLassoCV

# Generate some random data
n_samples = 1000
n_features = 5
X = np.random.rand(n_samples, n_features)

# Fit the L1-penalized covariance estimator
clf = GraphLassoCV(alpha=0.1, tol=1e-6)
clf.fit(X)

# Get the estimated covariance matrix
C = clf.covariance_
