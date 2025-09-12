import numpy as np
from sklearn.covariance import Lasso
from sklearn.linear_model import Lasso as LassoRegressor
from sklearn.preprocessing import StandardScaler

# Example data
np.random.seed(0)
n_samples, n_features = 60, 50
X = np.random.randn(n_samples, n_features)

# Standardize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Estimate the covariance matrix
cov_estimator = Lasso(alpha=0.01)
cov_estimator.fit(X_scaled)
cov_matrix = cov_estimator.covariance_

# Estimate the precision matrix (inverse covariance matrix)
precision_matrix = np.linalg.inv(cov_matrix)

# Apply Lasso to the precision matrix estimation
lasso = LassoRegressor(alpha=0.01)
precision_matrix_lasso = np.zeros_like(precision_matrix)
for i in range(precision_matrix.shape[1]):
    lasso.fit(precision_matrix[:, i].reshape(-1, 1), precision_matrix[i, i])
    precision_matrix_lasso[:, i] = lasso.coef_

print("Estimated Precision Matrix with Lasso:")
print(precision_matrix_lasso)
