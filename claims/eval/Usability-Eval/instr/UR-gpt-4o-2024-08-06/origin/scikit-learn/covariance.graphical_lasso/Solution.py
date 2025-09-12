import numpy as np
from sklearn.covariance import GraphicalLassoCV

# Generate synthetic data
n_samples = 60
n_features = 20
np.random.seed(42)  # For reproducibility

# Simulate some data with a covariance structure
X = np.random.randn(n_samples, n_features)

# Initialize the GraphicalLassoCV model for automatic cross-validation
model = GraphicalLassoCV()

# Fit the model to the data
model.fit(X)

# Retrieve the estimated covariance and the precision (inverse covariance)
covariance = model.covariance_
precision = model.precision_

# Display the results
print("Estimated covariance matrix:")
print(covariance)
print("Estimated precision matrix:")
print(precision)
