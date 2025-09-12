import numpy as np
from sklearn.covariance import GraphicalLassoCV

# Generate synthetic data
np.random.seed(0)
n_samples, n_features = 100, 10
X = np.random.randn(n_samples, n_features)

# Create a GraphicalLassoCV instance with cross-validation for the choice of the l1 penalty
model = GraphicalLassoCV(alphas=np.logspace(-1, 1, 10))

# Fit the model to the data
model.fit(X)

# Get the estimated sparse inverse covariance matrix
inverse_covariance_matrix = model.precision_

print("Estimated Sparse Inverse Covariance Matrix:")
print(inverse_covariance_matrix)
