from sklearn.sparse import RandomizedLasso
import numpy as np

# Generate some data
n_samples, n_features = 1000, 10
np.random.seed(0)
X = np.random.randn(n_samples, n_features)

# Fit the model
alpha = 0.1  # L1 penalty strength
estimator = RandomizedLasso(alpha=alpha, random_state=0)
estimator.fit(X)

# Print the estimated inverse covariance matrix
print(estimator.precision_)
