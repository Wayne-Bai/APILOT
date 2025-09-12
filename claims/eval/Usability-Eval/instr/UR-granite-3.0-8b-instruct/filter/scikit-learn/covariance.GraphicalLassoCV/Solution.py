import numpy as np
from sklearn.covariance import GraphicalLasso
from sklearn.datasets import make_sparse_undetected_covariance

# Generate a random sparse and undetected covariance matrix
X, _ = make_sparse_undetected_covariance(n_samples=100, n_features=20, random_state=42)

# Initialize the GraphicalLassoCV estimator with cross-validation
graphical_lasso = GraphicalLassoCV(cv=5, random_state=42)

# Fit the estimator to the data
graphical_lasso.fit(X)

# Print the estimated inverse covariance matrix
print("Estimated inverse covariance matrix:\n", graphical_lasso.covariance_)
