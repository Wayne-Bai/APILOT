# Import necessary libraries from scikit-learn
from sklearn.covariance import GraphLassoCV
from sklearn.datasets import make_sparse_spd_matrix
import numpy as np

# Generate a random sparse covariance matrix
dim = 20
A, _ = make_sparse_spd_matrix(dim, alpha=0.95, smallest_coef=0.4)

# Generate a sample from the multivariate normal distribution with this covariance
np.random.seed(0)
n_samples = 60
X = np.random.multivariate_normal(mean=np.zeros(dim), cov=np.linalg.inv(A), size=n_samples)

# Use cross-validation to determine the optimal L1 regularization for the sparse inverse covariance estimator
glcv = GraphLassoCV(alphas=5)
glcv.fit(X)

# Print the estimated sparse inverse covariance matrix
print("Estimated sparse inverse covariance matrix:")
print(glcv.precision_)
