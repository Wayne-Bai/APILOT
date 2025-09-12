import numpy as np
from sklearn.datasets import make_swiss_roll
from sklearn.manifold import Isomap
import matplotlib.pyplot as plt

# Generate a swiss roll dataset
X, color = make_swiss_roll(n_samples=1500)

# Initialize Isomap with 2 components
isomap = Isomap(n_components=2)

# Fit and transform the data
X_transformed = isomap.fit_transform(X)

# Plot the original swiss roll
fig = plt.figure(figsize=(12, 6))
ax1 = fig.add_subplot(121, projection='3d')
ax1.scatter(X[:, 0], X[:, 1], X[:, 2], c=color, cmap=plt.cm.Spectral)
ax1.set_title("Original Swiss Roll")

# Plot the Isomap embedding
ax2 = fig.add_subplot(122)
ax2.scatter(X_transformed[:, 0], X_transformed[:, 1], c=color, cmap=plt.cm.Spectral)
ax2.set_title("Isomap Embedding")

plt.show()
