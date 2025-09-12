# Import necessary libraries
from sklearn.covariance import GraphLassoCV
import numpy as np

# Generate sample data
np.random.seed(0)
n_samples = 100
n_features = 10
data = np.random.randn(n_samples, n_features)

# Create an instance of GraphLassoCV with L1-penalized
glcv = GraphLassoCV(alphas=5)

# Fit the data
glcv.fit(data)

# Print the estimated covariance
print("Estimated covariance:")
print(glcv.covariance_)

# Print the estimated precision
print("Estimated precision:")
print(glcv.precision_)
