
from sklearn.covariance import GraphicalLasso
import numpy as np

# Generate random data
np.random.seed(42)
n_samples = 100
n_features = 20
X = np.random.randn(n_samples, n_features)

# Sparse inverse covariance estimation with an l1-penalized estimator
alpha = 0.01  # Regularization parameter
model = GraphicalLasso(alpha=alpha)
model.fit(X)

# Precisions matrix from the model
precision_matrix = model.precision_
print("Precision matrix:")
print(precision_matrix)
