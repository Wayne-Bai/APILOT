import numpy as np
from sklearn.covariance import ShrunkCovariance
from sklearn.linear_model import LassoLarsIC
from sklearn.datasets import load_iris
from sklearn.metrics import mean_squared_error

# Load the iris dataset
iris = load_iris()
X = iris.data[:, :2]  # we only take the first two features.

# Create a random sparse covariance matrix
n_features = X.shape[1]
cov = np.random.rand(n_features, n_features)
np.fill_diagonal(cov, 0)  # set diagonal to zero

# Shrink the covariance matrix towards the identity matrix using LassoLarsIC
shrunk_cov = ShrunkCovariance(alpha=1).fit(X)

# Perform inverse covariance estimation with L1-penalized estimator
estimator = LassoLarsIC(alpha=0.1, tol=0.01)
inverse_cov = estimator.fit(shrunk_cov).cov_

# Calculate the mean squared error between the true and estimated covariance matrices
mse = np.mean((cov - inverse_cov) ** 2)
print("MSE:", mse)
