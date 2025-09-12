
from sklearn.covariance import graphical_lasso
import numpy as np

# Generate some random data
np.random.seed(0)
n_samples = 50
n_features = 20
data = np.random.randn(n_samples, n_features)

# Perform sparse inverse covariance estimation
cov_, precision_ = graphical_lasso(data, alpha=0.9)

# Print the covariance matrix
print("Covariance matrix:")
print(cov_)

# Print the precision matrix
print("Precision matrix:")
print(precision_)
