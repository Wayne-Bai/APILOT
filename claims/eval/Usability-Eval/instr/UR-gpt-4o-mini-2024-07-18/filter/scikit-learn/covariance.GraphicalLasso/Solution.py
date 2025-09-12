import numpy as np
from sklearn.covariance import GraphicalLasso

# Sample data generation
np.random.seed(0)
X = np.random.randn(100, 10)

# Sparse inverse covariance estimation using GraphicalLasso with l1-penalty
model = GraphicalLasso(alpha=0.1)
model.fit(X)

# Retrieve the estimated inverse covariance matrix
inverse_covariance_matrix = model.precision_

print("Estimated Inverse Covariance Matrix:")
print(inverse_covariance_matrix)
