import numpy as np
from sklearn.covariance import Lasso
from sklearn.linear_model import Lasso as LassoRegressor

# Example data
np.random.seed(0)
n_samples, n_features = 60, 50
X = np.random.randn(n_samples, n_features)

# Estimate the covariance matrix
cov_estimator = Lasso(alpha=0.01)
cov_estimator.fit(X)
covariance = cov_estimator.covariance_

# Estimate the precision matrix (inverse covariance)
precision = np.linalg.inv(covariance)

# Apply Lasso to the precision matrix estimation
lasso_estimator = LassoRegressor(alpha=0.01)
lasso_estimator.fit(precision, np.eye(n_features))
sparse_precision = lasso_estimator.coef_

print("Estimated Precision Matrix (Sparse):\n", sparse_precision)
