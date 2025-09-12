from sklearn.covariance import GraphLassoCV
import numpy as np

# Generate some random data
np.random.seed(0)
n_samples = 200
n_features = 20
data = np.random.normal(size=(n_samples, n_features))

# Initialize the model with an l1-penalized estimator
model = GraphLassoCV()

# Fit the model to the data
model.fit(data)

# Get the estimated precision matrix
precision = model.precision_

# Get the estimated covariance matrix
covariance = np.linalg.inv(precision)
