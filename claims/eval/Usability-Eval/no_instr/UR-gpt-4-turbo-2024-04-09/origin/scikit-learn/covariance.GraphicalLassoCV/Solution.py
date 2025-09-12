import numpy as np
from sklearn.covariance import GraphicalLassoCV
from sklearn.datasets import make_sparse_spd_matrix

# Generate synthetic data
np.random.seed(0)
n_samples = 60
n_features = 20

# Generate a sparse symmetric positive definite matrix
prec = make_sparse_spd_matrix(n_features, alpha=.98, smallest_coef=.4, largest_coef=.7)
cov = np.linalg.inv(prec)
X = np.random.multivariate_normal(np.zeros(n_features), cov, size=n_samples)

# Apply GraphicalLassoCV to estimate the sparse inverse covariance matrix
model = GraphicalLassoCV()
model.fit(X)

# Sparse inverse covariance matrix estimation
estimated_inv_covariance = model.precision_

print("Estimated inverse covariance matrix:")
print(estimated_inv_covariance)
