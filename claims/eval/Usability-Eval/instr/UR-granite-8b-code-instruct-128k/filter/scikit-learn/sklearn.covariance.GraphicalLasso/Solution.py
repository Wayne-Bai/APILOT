
from sklearn.covariance import GraphLassoCV
from sklearn.datasets import make_sparse_spd_matrix
import numpy as np
import matplotlib.pyplot as plt

# Generate a sparse, symmetric positive-definite matrix
n_features = 10
rng = np.random.RandomState(42)
cov = make_sparse_spd_matrix(n_features, random_state=rng)

# Generate data from the multivariate normal distribution
mean = np.zeros(n_features)
X = rng.multivariate_normal(mean, cov, 1000)

# Fit the GraphLassoCV estimator to the data
estimator = GraphLassoCV(cv=5)
estimator.fit(X)

# Plot the inverse covariance matrix
plt.spy(estimator.inverse_covariance_)
plt.show()
