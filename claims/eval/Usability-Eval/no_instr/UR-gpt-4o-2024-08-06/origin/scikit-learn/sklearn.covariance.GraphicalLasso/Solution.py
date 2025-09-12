from sklearn.covariance import GraphicalLasso
import numpy as np

# Generate some data
np.random.seed(0)
n_samples, n_features = 100, 20
X = np.random.randn(n_samples, n_features)

# Fit the GraphicalLasso model
model = GraphicalLasso(alpha=0.01)
model.fit(X)

# Output the estimated covariance and precision matrices
covariance = model.covariance_
precision = model.precision_

print("Estimated covariance matrix:")
print(covariance)

print("\nEstimated precision (inverse covariance) matrix:")
print(precision)
