from sklearn.covariance import LedoitWolf
from sklearn.datasets import make_sparse_spd_matrix

# Generating a sparse SPD matrix
n_samples = 30
factor = 1. / n_samples

# small perturbation on the diagonal for numerical stability
cov = factor * make_sparse_spd_matrix(n_samples, alpha=.98)

# LedoitWolf estimator
lew = LedoitWolf(store_precision=False, assume_centered=False)
lew.fit(cov)

# Get the sparse inverse covariance estimate
sparse_inverse_cov = lew.covariance_

print("Sparse inverse covariance:\n", sparse_inverse_cov)
