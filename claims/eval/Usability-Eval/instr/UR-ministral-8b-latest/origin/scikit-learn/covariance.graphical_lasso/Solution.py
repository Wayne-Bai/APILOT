import numpy as np
from sklearn.linear_model import Lars

# Generating sample data
np.random.seed(42)
X = np.random.rand(100, 5)

# Fitting L1-penalized covariance estimator
lars = Lars(cv=5, precompute='auto', random_state=42)
lars.fit(X)
cov_matrix = lars.coef_.T @ lars.coef_

cov_matrix
