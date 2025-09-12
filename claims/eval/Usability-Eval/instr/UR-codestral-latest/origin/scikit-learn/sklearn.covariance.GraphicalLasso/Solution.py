import numpy as np
from sklearn.covariance import EmpiricalCovariance, GraphicalLasso

# Generate some data
np.random.seed(0)
n_features = 10
n_samples = 500
X = np.random.randn(n_samples, n_features)

# Compute the empirical covariance matrix
emp_cov = EmpiricalCovariance().fit(X)

# Fit the GraphicalLasso model with an l1-penalty
model = GraphicalLassoCV(alphas=10)
model.fit(X)

# The estimated precision matrix
precision = model.precision_

print(precision)
