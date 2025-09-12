import numpy as np
from sklearn.covariance import GraphicalLassoCV
from sklearn.datasets import make_sparse_spd_matrix

# Generate a sparse positive definite matrix
X = make_sparse_spd_matrix(n_dim=10, random_state=42)

# Fit the Graphical Lasso with cross-validated choice of the l1 penalty
model = GraphicalLassoCV()
model.fit(X)

# Obtain the estimated covariance matrix
covariance_matrix = model.covariance_
