# Import required libraries
import numpy as np
from sklearn.decomposition import NMF
import matplotlib.pyplot as plt

# Generate a random non-negative matrix X
np.random.seed(0)
X = np.random.rand(6, 4)

print("Original Matrix X:")
print(X)

# Create an instance of NMF model
model = NMF(n_components=2, init='random', random_state=0)

# Fit the model to X
W = model.fit_transform(X)
H = model.components_

print("\nMatrix W:")
print(W)

print("\nMatrix H:")
print(H)

# Reconstruct the original matrix
X_reconstructed = np.dot(W, H)

print("\nReconstructed Matrix X:")
print(X_reconstructed)

# Plot the original and reconstructed matrices
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(X, cmap='gray')
plt.title('Original Matrix')

plt.subplot(1, 2, 2)
plt.imshow(X_reconstructed, cmap='gray')
plt.title('Reconstructed Matrix')

plt.show()
