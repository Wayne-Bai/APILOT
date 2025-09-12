from sklearn.covariance import GraphicalLasso
from sklearn.datasets import make_sparse_spd_matrix

# Generate a dataset with a sparse inverse covariance structure
n_samples = 1000
n_features = 20
cov, prec = make_sparse_spd_matrix(n_features, alpha=0.95, random_state=42)

# Generate samples from the sparse covariance graphical model
X = np.random.multivariate_normal(mean=np.zeros(n_features), cov=cov, size=n_samples)

# Initialize the GraphicalLasso estimator
estimator = GraphicalLasso(alpha=0.1, max_iter=100)

# Fit the estimator to the data
estimator.fit(X)

# Print the estimated inverse covariance matrix
print(estimator.precision_)
