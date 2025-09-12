# Importing necessary libraries
from sklearn.decomposition import NMF
import numpy as np
import matplotlib.pyplot as plt

# Creating a random non-negative matrix X
np.random.seed(0)
X = np.random.rand(40, 10)

# Applying NMF to factorize the matrix X
model = NMF(n_components=2, init='random', random_state=0)
W = model.fit_transform(X)
H = model.components_

# Verifying the approximation of X
approx_X = np.dot(W, H)
assert np.all(approx_X >= 0)  # All elements in approx_X should be non-negative

# Printing the factorized matrices
print("Matrix X:")
print(X)
print("\nMatrix W:")
print(W)
print("\nMatrix H:")
print(H)
print("\nApproximation of X:")
print(approx_X)

# Measuring the quality of the approximation
reconstruction_error = np.linalg.norm(X - approx_X, 'fro') / np.linalg.norm(X, 'fro')
print(f"\nReconstruction error: {reconstruction_error}")

# Example use case: dimensionality reduction
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.scatter(X[:, 0], X[:, 1])
plt.title("Original Data")

plt.subplot(1, 2, 2)
plt.scatter(approx_X[:, 0], approx_X[:, 1])
plt.title("Reconstructed Data")
plt.show()
