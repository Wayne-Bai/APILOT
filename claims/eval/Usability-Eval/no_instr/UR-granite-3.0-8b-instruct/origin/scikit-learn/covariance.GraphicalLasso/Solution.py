from sklearn.sparse import l1_regularized_covariance

# Assuming X is your data
# X = ...

# Define the regularization parameter
alpha = 0.1

# Estimate the sparse inverse covariance matrix
sparse_inv_cov = l1_regularized_covariance(X, alpha=alpha)
