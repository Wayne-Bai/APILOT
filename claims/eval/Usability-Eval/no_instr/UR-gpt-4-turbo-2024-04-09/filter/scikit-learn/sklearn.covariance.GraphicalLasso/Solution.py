from sklearn.covariance import GraphicalLasso
import numpy as np

# Example data: Generate some data that is well-suited for sparse inverse covariance estimation
np.random.seed(0)
n_samples = 60
n_features = 20

# Create a symmetric positive definite matrix with some small non-zero entries
X = np.random.normal(size=(n_samples, n_features))
X[:, 2] += X[:, 0] + X[:, 1]
X[:, 4] += X[:, 0]
X *= 0.1

# Define the Graphical Lasso model
model = GraphicalLasso(alpha=0.25, max_iter=100, verbose=True)

# Fit the model
model.fit(X)

# The estimated precision (inverse covariance) matrix
precision_matrix = model.precision_

# Show the precision matrix
print("Estimated Precision Matrix:")
print(precision_matrix)
