from sklearn.covariance import Lasso
from sklearn.datasets import make_sparse_spd_matrix

# Generate a sparse symmetric positive definite matrix
n_features = 10
prec = make_sparse_spd_matrix(n_features, alpha=0.95, random_state=42)

# Threshold small values to exactly zero
prec[abs(prec) < 0.1] = 0

# Generate data from multivariate normal
from sklearn.datasets import make_spd_matrix
cov = make_spd_matrix(n_features, random_state=42)
mean = np.zeros(n_features)
from scipy.stats import multivariate_normal
data = multivariate_normal.rvs(mean=mean, cov=cov, size=300)

# Fit the Lasso model
lasso = Lasso(alpha=0.1)
lasso.fit(data)

print("Estimated precision matrix:")
print(lasso.coef_)
