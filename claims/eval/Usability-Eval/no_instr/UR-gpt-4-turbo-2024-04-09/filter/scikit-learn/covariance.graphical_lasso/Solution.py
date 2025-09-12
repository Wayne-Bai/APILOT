import numpy as np
from sklearn.covariance import GraphicalLasso

# Sample data generation
np.random.seed(0)
n_samples = 60
n_features = 20

# Generate a data matrix (normally distributed data)
X = np.random.randn(n_samples, n_features)

# Define the model, alpha is the regularization parameter
model = GraphicalLasso(alpha=0.1, max_iter=100)

# Fit the model to the data
model.fit(X)

# The estimated covariance and precision matrix
covariance_matrix = model.covariance_
precision_matrix = model.precision_

print("Estimated covariance matrix:")
print(covariance_matrix)

print("\nEstimated precision matrix (inverse covariance):")
print(precision_matrix)
