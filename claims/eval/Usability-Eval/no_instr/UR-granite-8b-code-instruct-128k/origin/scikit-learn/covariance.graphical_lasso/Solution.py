
from sklearn.covariance import LedoitWolf
import numpy as np
# Generate some random data
n_samples = 1000
n_features = 10
X = np.random.normal(size=(n_samples, n_features))
# Create a LedoitWolf object and fit it to the data
model = LedoitWolf()
model.fit(X)
# Get the estimated covariance matrix
cov_matrix = model.covariance_
# Get the precision matrix
precision_matrix = model.precision_
