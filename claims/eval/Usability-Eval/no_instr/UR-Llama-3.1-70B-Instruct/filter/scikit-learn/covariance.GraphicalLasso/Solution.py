# Import required libraries
from sklearn.covariance import GraphLassoCV
import numpy as np
import matplotlib.pyplot as plt

# Generate random data
np.random.seed(0)
n_samples = 200
n_features = 20
X = np.random.normal(size=(n_samples, n_features))

# Create an instance of the GraphLassoCV class with defaults
gl_source = GraphLassoCV()

# Fit the model to the data
gl_source.fit(X)

# Get the sparse inverse covariance matrix
sparse_inverse_cov = gl_source.precision_

# Print the shape and non-zero elements of the sparse inverse covariance matrix
print("Sparse inverse covariance matrix shape:", sparse_inverse_cov.shape)
print("Non-zero elements in sparse inverse covariance matrix:", np.count_nonzero(sparse_inverse_cov))

# Plot the sparse inverse covariance matrix as a heatmap
plt.imshow(sparse_inverse_cov, cmap='hot', interpolation='nearest')
plt.title("Sparse Inverse Covariance Matrix")
plt.show()
