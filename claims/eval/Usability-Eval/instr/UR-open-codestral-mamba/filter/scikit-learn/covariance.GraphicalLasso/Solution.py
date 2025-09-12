from sklearn.covariance import LedoitWolf
from sklearn.linear_model import LassoCV
from sklearn.datasets import make_spd_matrix

# Generate a random SPD (symmetric positive definite) matrix
random_state = 42
n_samples, n_features = 50, 60
label = "SPD"
cov = make_spd_matrix(n_features, random_state=random_state)
X = np.random.RandomState(random_state).randn(n_samples, n_features)
X = np.dot(X, np.linalg.cholesky(cov).T)

# Sparse inverse covariance with an L1-penalized estimator
model = LedoitWolf(store_precision=False, assume_centered=False)
model.fit(X)

# Print the resulting covariance matrix
print("Covariance matrix:\n", model.covariance_)

# L1-penalized estimator with SparseInverseCovariance
model = LassoCV()
model.fit(X)

# Print the resulting coefficients
print("Coefficients:\n", model.coef_)
