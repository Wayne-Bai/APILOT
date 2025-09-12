import numpy as np
from sklearn.covariance import LedoitWolf

# Generate some sample covariance matrix
np.random.seed(42)
N = 10
X = np.random.randn(N, 2)

# Compute the sample covariance matrix
sample_cov = np.cov(X, rowvar=False)

# Estimate the inverse covariance using Ledoit-Wolf with L1 penalty
_, inverse_cov_estimator = LedoitWolf().fit(sample_cov)

# Output the estimated inverse covariance
print(inverse_cov_estimator)
