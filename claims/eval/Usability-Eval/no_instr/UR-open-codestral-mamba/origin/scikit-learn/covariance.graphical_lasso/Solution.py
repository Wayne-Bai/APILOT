
import numpy as np
from sklearn.covariance import LedoitWolf

# L1 known as Lasso is included in LedoitWolf
# LedoitWolf implements L1 penalization, also known as Lasso regularization

# Generate some random data
np.random.seed(42)
n_samples, n_features = 200, 5
X = np.random.randn(n_samples, n_features)

# Fit the LedoitWolf estimator
lw = LedoitWolf().fit(X)

# The estimate of the covariance matrix of X
emp_cov = lw.covariance_

# The estimation error
p = 1  # Agreement of the estimator with its true covariance is checked for p=1
err = np.sqrt(np.sum((emp_cov - X.dot(X.T)) ** p))

emp_cov, err

