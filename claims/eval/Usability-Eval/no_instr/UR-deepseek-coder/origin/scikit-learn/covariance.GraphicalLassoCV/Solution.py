import numpy as np
from sklearn.covariance import GraphicalLassoCV
from sklearn.datasets import make_sparse_spd_matrix

# Generate a sparse positive definite matrix
n_samples = 60
n_features = 20
prng = np.random.RandomState(1)
prec = make_sparse_spd_matrix(n_features, alpha=.98, smallest_coef=.4, largest_coef=.7, random_state=prng)
cov = np.linalg.inv(prec)
X = prng.multivariate_normal(np.zeros(n_features), cov, size=n_samples)
X -= X.mean(axis=0)
X /= X.std(axis=0)

# Estimate the sparse inverse covariance
model = GraphicalLassoCV()
model.fit(X)

# Estimated precision matrix
estimated_precision = model.precision_

# Estimated covariance matrix
estimated_covariance = model.covariance_

print("Estimated Precision Matrix:\n", estimated_precision)
print("Estimated Covariance Matrix:\n", estimated_covariance)
