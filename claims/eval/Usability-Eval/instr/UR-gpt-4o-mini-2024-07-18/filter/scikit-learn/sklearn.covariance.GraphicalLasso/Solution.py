import numpy as np
from sklearn.covariance import GraphicalLasso

# Generate some sample data
np.random.seed(0)
n_samples, n_features = 100, 20
X = np.random.randn(n_samples, n_features)

# Fit the Graphical Lasso model
alpha = 0.1  # regularization strength
model = GraphicalLasso(alpha=alpha)
model.fit(X)

# Retrieve the sparse inverse covariance matrix
inverse_covariance_matrix = model.precision_

# Display the result
print("Sparse Inverse Covariance Matrix:\n", inverse_covariance_matrix)
