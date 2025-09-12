# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import Isomap
from sklearn.datasets import make_s_curve

# Generate a sample dataset (in this case, an S curve)
n_points = 500
X, color = make_s_curve(n_points, random_state=0)

# Perform Isomap embedding
n_neighbors = 10
n_components = 2
isomap = Isomap(n_neighbors=n_neighbors, n_components=n_components)
X_reduced = isomap.fit_transform(X)

# Plot the original and embedded data
fig, axs = plt.subplots(1, 2, figsize=(12, 6))
axs[0].scatter(X[:, 0], X[:, 1], c=color)
axs[0].set_title('Original Space')
axs[1].scatter(X_reduced[:, 0], X_reduced[:, 1], c=color)
axs[1].set_title('Isomap Embedding ({})'.format(n_neighbors))

plt.show()
