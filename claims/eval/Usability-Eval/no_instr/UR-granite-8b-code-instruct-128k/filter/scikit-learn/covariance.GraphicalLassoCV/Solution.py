import numpy as np
from sklearn.covariance import GraphLassoCV

# Generate sample data
np.random.seed(42)
n_samples = 100
n_features = 200
data = np.random.normal(size=(n_samples, n_features))

# Create a Sparse inverse covariance model with cross-validated choice of the l1 penalty
model = GraphLassoCV()

# Fit the model to the data
model.fit(data)

# Get the estimated covariance matrix
estimated_covariance = model.covariance_

# Get the estimated precision matrix
estimated_precision = model.precision_
