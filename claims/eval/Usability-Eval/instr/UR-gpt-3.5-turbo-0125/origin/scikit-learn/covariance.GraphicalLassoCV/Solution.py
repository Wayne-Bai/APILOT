
from sklearn.covariance import GraphicalLassoCV
import numpy as np

# Initialize the GraphicalLassoCV estimator
estimator = GraphicalLassoCV()

# Fit the estimator on your data
estimator.fit(your_data)

# Retrieve the sparse inverse covariance matrix
sparse_inv_cov = estimator.precision_
