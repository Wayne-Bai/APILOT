import numpy as np
import scipy.sparse as sp
from sklearn.covariance import GraphicalLasso

# Generate some sample data
np.random.seed(0)
data = np.random.randn(100, 5)

# Fit the GraphicalLasso model
gl = GraphicalLasso()
gl.fit(data)

# Get the inverse covariance matrix
inverse_covariance = gl.inverse_covariance_
print(inverse_covariance)
