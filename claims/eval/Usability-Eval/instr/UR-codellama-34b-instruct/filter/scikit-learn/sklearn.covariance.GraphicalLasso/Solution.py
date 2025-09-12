
import numpy as np
from sklearn.linear_model import Lasso
from sklearn.covariance import GraphLasso

# Generate some random data for the example
n_samples = 100
n_features = 5
np.random.seed(0)
X = np.random.randn(n_samples, n_features)

# Create a GraphLasso object and fit it to the data
gl = GraphLasso()
gl.fit(X)

# Get the inverse covariance matrix using Lasso
inv_cov = gl.get_inverse_covariance()

# Create a Lasso object and set the regularization parameter to 1
lasso = Lasso(alpha=1)

# Fit the Lasso model to the data using the inverse covariance matrix as the penalty term
lasso.fit(inv_cov, X)

# Get the estimated coefficients using the Lasso object
coefs = lasso.coef_
