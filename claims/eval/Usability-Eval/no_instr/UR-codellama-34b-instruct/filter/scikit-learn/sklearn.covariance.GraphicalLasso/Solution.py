import numpy as np
from sklearn.covariance import LedoitWolfEstimator, OasEstimator

# Generate some sample data
n_samples = 1000
X = np.random.rand(n_samples, n_samples)

# Compute the inverse covariance matrix using the Ledoit-Wolf estimator
lw_estimator = LedoitWolfEstimator()
lw_inverse = lw_estimator.fit(X).inverse_covariance_

# Compute the inverse covariance matrix using the OAS estimator
oas_estimator = OasEstimator()
oas_inverse = oas_estimator.fit(X).inverse_covariance_

# L1-penalized estimator with alpha=0.5
l1_alpha = 0.5
l1_estimator = LedoitWolfEstimator(L1_alpha=l1_alpha)
l1_inverse = l1_estimator.fit(X).inverse_covariance_
