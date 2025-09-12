from sklearn.covariance import GraphicalLasso

# Sample data: Replace this with your own dataset
import numpy as np

# Generate a random covariance matrix for demonstration
np.random.seed(0)
X = np.random.randn(100, 5)

# Fit the L1-penalized covariance estimator
model = GraphicalLasso(alpha=0.1)
model.fit(X)

# Get the estimated covariance matrix
covariance_matrix = model.covariance_
print("Estimated covariance matrix:\n", covariance_matrix)
