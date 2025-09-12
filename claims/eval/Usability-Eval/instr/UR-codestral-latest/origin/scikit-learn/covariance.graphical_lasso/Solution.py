from sklearn.covariance import GraphicalLassoCV
import numpy as np

# Generate some sample data
np.random.seed(0)
n_samples = 600
n_features = 10

X = np.random.randn(n_samples, n_features)

# Use GraphicalLassoCV for the L1-penalized covariance estimator
model = GraphicalLassoCV()

# Fit the model to the data
model.fit(X)

# The estimated covariance matrix can be accessed via `model.covariance_`
covariance_matrix = model.covariance_
