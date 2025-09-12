# Import necessary libraries
from sklearn.covariance import LedoitWolf, OAS
from sklearn.covariance import empirical_covariance
import numpy as np

# Generate some random multivariate data
np.random.seed(0)
n_samples = 200
n_features = 10
X = np.random.multivariate_normal(mean=[0] * n_features, cov=np.eye(n_features), size=n_samples)

# Use L1-penalized covariance estimator (also known as Graphical Lasso)
# Since 'GraphicalLasso' is outdated and not recommended by scikit-learn,
# we'll be using 'OracleApproximatingShrinkage' (OAS) as an alternative,
# which is similar but not the same, with a basic example

# OAS has no 'alpha' and'mode' parameters like 'GraphicalLasso'.
# You can manually set the'shrinkage' parameter of 'LedoitWolf' or
# use OAS for a separate tuning process and more experiments.

# Initialize Oracle Approximating Shrinkage object
cov_estimator = OAS(store_precision=True, assume_centered=False)

# Estimate the covariance matrix
cov_estimator.fit(X)

# Get the estimated covariance and precision matrices
cov = cov_estimator.covariance_
prec = cov_estimator.precision_

print("Estimated Covariance Matrix:")
print(cov)
print("\nEstimated Precision Matrix:")
print(prec)

# Initialize LedoitWolf object
ledoit_wolf = LedoitWolf(assume_centered=False)

# Estimate the covariance matrix using LedoitWolf
ledoit_wolf.fit(X)

# Get the estimated covariance matrix using LedoitWolf
cov_ledoit_wolf = ledoit_wolf.covariance_

print("\nEstimated Covariance Matrix using LedoitWolf:")
print(cov_ledoit_wolf)

# Use L1-penalized covariance estimator basic example through sklearn empirical_covariance
emp_cov = empirical_covariance(X)
