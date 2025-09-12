# Import necessary libraries
from sklearn.decomposition import NMF
import numpy as np
import matplotlib.pyplot as plt

# Create a sample non-negative matrix X
np.random.seed(0)
X = np.random.rand(4, 5)

# Print the original matrix
print("Original Matrix X:")
print(X)

# Perform NMF with 2 components
model = NMF(n_components=2, init='random', random_state=0)
W = model.fit_transform(X)
H = model.components_

# Print the factorized matrices W and H
print("\nMatrix W:")
print(W)
print("\nMatrix H:")
print(H)

# Reconstruct the original matrix from W and H
X_reconstructed = np.dot(W, H)

# Print the reconstructed matrix
print("\nReconstructed Matrix X:")
print(X_reconstructed)

# Plot the original and reconstructed matrices
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.imshow(X, cmap='viridis', interpolation='nearest')
plt.colorbar()
plt.title("Original Matrix X")

plt.subplot(1, 2, 2)
plt.imshow(X_reconstructed, cmap='viridis', interpolation='nearest')
plt.colorbar()
plt.title("Reconstructed Matrix X")

plt.show()
