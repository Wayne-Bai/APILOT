
from sklearn.datasets import make_sparse_spd_matrix
import numpy as np

def l1_penalized_covariance_estimator(X):
    n_features = X.shape[1]
    cov_estimator = np.dot(X.T, X) / X.shape[0]
    
    alpha = 1.0  # L1 regularization parameter
    cov_estimator.flat[::n_features + 1] += alpha
    
    return cov_estimator

# Example usage:
X = make_sparse_spd_matrix(n_samples=100, n_features=10, alpha=0.95)
estimated_cov = l1_penalized_covariance_estimator(X)
print(estimated_cov)
