from sklearn.covariance import GraphicalLasso
import numpy as np

# Generate some sample data
n_samples, n_features = 100, 30
np.random.seed(42)
X = np.random.normal(size=(n_samples, n_features))

# Estimate the covariance matrix
alpha = 0.01  # Regularization parameter
model = GraphicalLasso(alpha=alpha)
model.fit(X)

# Get the precision matrix (sparse inverse covariance)
precision_matrix = model.precision_
print(precision_matrix)
