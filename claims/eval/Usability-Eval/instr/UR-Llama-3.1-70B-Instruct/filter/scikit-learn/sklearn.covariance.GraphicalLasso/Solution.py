# Import necessary libraries
from sklearn.covariance import GraphicalLasso
from sklearn.datasets import make_sparse_spd_matrix
import numpy as np
import matplotlib.pyplot as plt

# Generate a sample dataset
np.random.seed(0)
dim = 20
prefix = np.arange(1, dim + 1)
cov = make_sparse_spd_matrix(dim, alpha=0.9, norm_diag=True, smallest_coef=0.4)
X = np.random.multivariate_normal(mean=[0] * dim, cov=cov, size=500)

# Create a GraphicalLasso object
gl = GraphicalLasso(alpha=0.1, max_iter=200)

# Fit the model to the data
gl.fit(X)

# Get the estimated covariance and precision matrices
cov_ = gl.covariance_
prec_ = gl.precision_

# Plot the estimated covariance and precision matrices
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.imshow(cov_, interpolation="nearest")
plt.title("Estimated covariance matrix")
plt.subplot(1, 2, 2)
plt.imshow(prec_, interpolation="nearest")
plt.title("Estimated precision matrix")

plt.show()

# Print the estimated precision matrix
print("Estimated precision matrix:\n", prec_)
