import numpy as np
from sklearn.covariance import GraphicalLasso

# Generate some synthetic data
np.random.seed(42)
n_samples = 100
n_features = 10
X = np.random.rand(n_samples, n_features)

# Create a GraphicalLasso estimator
alpha = 0.1  # Regularization strength
model = GraphicalLasso(alpha=alpha, max_iter=100)

# Fit the model to the data
model.fit(X)

# Get the estimated inverse covariance matrix
inverse_covariance_matrix = model.get_precision()

print("Estimated Inverse Covariance Matrix:")
print(inverse_covariance_matrix)
