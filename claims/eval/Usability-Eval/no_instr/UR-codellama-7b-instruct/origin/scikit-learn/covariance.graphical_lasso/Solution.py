from sklearn.covariance import CovarianceEstimator
from sklearn.metrics.pairwise import euclidean_distances

# Define the number of clusters and the regularization parameter
n_clusters = 3
reg_param = 1.0

# Generate random data
X = np.random.rand(100, 5)

# Initialize the CovarianceEstimator class with the desired parameters
cov = CovarianceEstimator(n_clusters=n_clusters, reg_param=reg_param)

# Compute the covariance matrix using the L1-penalized approach
cov.fit(X)

# Get the estimated covariance matrix
cov_matrix = cov.get_cov_mat()
