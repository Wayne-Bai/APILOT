import numpy as np
from sklearn.covariance import GraphicalLassoCV

# Generate sample data
np.random.seed(0)
n_samples = 60
n_features = 20

# Create a random symmetric, positive definite matrix
random_matrix = np.random.randn(n_features, n_features)
cov = np.dot(random_matrix, random_matrix.T)

# Generate observations with noise
X = np.random.multivariate_normal(np.zeros(n_features), cov, size=n_samples)

# Apply the GraphicalLassoCV estimator
model = GraphicalLassoCV()
model.fit(X)

# Estimated precision matrix (inverse covariance)
precision_matrix = model.precision_
print("Estimated Precision Matrix:")
print(precision_matrix)
