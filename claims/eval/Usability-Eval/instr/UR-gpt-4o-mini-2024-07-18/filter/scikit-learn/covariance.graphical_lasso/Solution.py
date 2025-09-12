from sklearn.covariance import GraphicalLasso

# Sample data (replace with your actual data)
import numpy as np

# Generate a random dataset
np.random.seed(0)
X = np.random.randn(100, 5)

# Create and fit the L1-penalized covariance estimator
model = GraphicalLasso(alpha=0.1)
model.fit(X)

# Retrieve the estimated covariance matrix
covariance_matrix = model.covariance_
print(covariance_matrix)
