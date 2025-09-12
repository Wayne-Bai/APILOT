from sklearn.covariance import GraphicalLassoCV
import numpy as np

# Generate synthetic data
np.random.seed(0)
n_samples = 100
n_features = 20
data = np.random.randn(n_samples, n_features)

# Fit the model
model = GraphicalLassoCV()
model.fit(data)

# Output the estimated precision matrix and covariance matrix
precision_matrix = model.precision_
covariance_matrix = model.covariance_

print("Estimated Precision Matrix:")
print(precision_matrix)

print("\nEstimated Covariance Matrix:")
print(covariance_matrix)
