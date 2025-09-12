
from sklearn.covariance import GraphLassoCV
import numpy as np

# Generate sample data
n_samples = 1000
n_features = 200
np.random.seed(42)
data = np.random.normal(size=(n_samples, n_features))

# Compute the estimate
cov = GraphLassoCV().fit(data).covariance_
