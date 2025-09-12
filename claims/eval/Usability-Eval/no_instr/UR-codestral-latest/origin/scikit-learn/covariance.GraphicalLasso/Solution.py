# Importing necessary libraries
from sklearn.covariance import GraphicalLasso
from sklearn.datasets import make_sparse_spd_matrix
import numpy as np

# Generating a sparse inverse covariance matrix
np.random.seed(0)
precision = make_sparse_spd_matrix(100)
covariance = np.linalg.inv(precision)

# Generating data from the covariance matrix
n_samples = 200
X = np.random.multivariate_normal(np.zeros(100), covariance, size=n_samples)

# Fitting the Graphical Lasso model with an l1-penalization
model = GraphicalLasso(alpha=0.01)
model.fit(X)

# Getting the estimated precision matrix
precision_estimate = model.precision_

print("Estimated precision matrix:")
print(precision_estimate)
