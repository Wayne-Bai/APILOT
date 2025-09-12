import numpy as np
from sklearn.covariance import LedoitWolf
from sklearn.linear_model import Lasso

# Example data
X = np.random.randn(100, 5)

# Ledoit-Wolf shrinkage estimator to get a robust covariance matrix
lw = LedoitWolf().fit(X)
cov_matrix = lw.covariance_

# Convert covariance matrix to precision matrix
precision_matrix = np.linalg.inv(cov_matrix)

# L1-penalized covariance estimation using Lasso
lasso = Lasso(alpha=0.1)
lasso.fit(precision_matrix, np.eye(precision_matrix.shape[0]))

# Extract the L1-penalized precision matrix
l1_precision_matrix = lasso.coef_

print("L1-penalized precision matrix:\n", l1_precision_matrix)
