# Import necessary libraries
import numpy as np
from sklearn.decomposition import NMF
import matplotlib.pyplot as plt

# Generate a random non-negative matrix X
np.random.seed(0)
X = np.random.rand(3, 4)

print("Original Matrix X:")
print(X)

# Create an NMF instance
model = NMF(n_components=2, init='random', random_state=0)

# Fit the model to the data
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
fig, ax = plt.subplots(1, 2, figsize=(12, 6))

ax[0].imshow(X, cmap='viridis')
ax[0].set_title('Original Matrix X')

ax[1].imshow(X_reconstructed, cmap='viridis')
ax[1].set_title('Reconstructed Matrix X')

plt.show()
