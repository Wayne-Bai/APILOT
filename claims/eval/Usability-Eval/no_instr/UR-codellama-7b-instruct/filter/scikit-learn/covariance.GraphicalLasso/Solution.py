
from sklearn.linear_model import SparseInverseCovariance
import numpy as np

# Generate a random dataset
X = np.random.rand(10, 5)

# Compute the inverse covariance matrix using an L1-penalized estimator
inv_cov = SparseInverseCovariance().fit(X).covariance_
