import numpy as np
from sklearn.covariance import graphical_lasso
from sklearn.datasets import make_sparse_spd_matrix

# Generating a synthetic sparse positive definite matrix as the true covariance
true_covariance = make_sparse_spd_matrix(dim=10, alpha=0.95, random_state=42)

# Generating sample data using the true covariance matrix
n_samples = 100
X = np.random.multivariate_normal(np.zeros(10), true_covariance, size=n_samples)

# Estimating the sparse inverse covariance using l1 regularization
alpha = 0.01  # Regularization parameter
covariance_estimated, precision_estimated = graphical_lasso(emp_cov=np.cov(X, rowvar=False), alpha=alpha)

print("Estimated Covariance Matrix:\n", covariance_estimated)
print("Estimated Precision (Inverse Covariance) Matrix:\n", precision_estimated)
