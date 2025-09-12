import numpy as np
from sklearn.manifold import Isomap
from sklearn.datasets import make_swiss_roll
import matplotlib.pyplot as plt

# Generate a swiss roll dataset
X, color = make_swiss_roll(n_samples=1500)

# Initialize Isomap with 2 components
isomap = Isomap(n_components=2)

# Fit and transform the data
X_reduced = isomap.fit_transform(X)

# Plot the results
plt.figure(figsize=(8, 6))
plt.scatter(X_reduced[:, 0], X_reduced[:, 1], c=color, cmap=plt.cm.Spectral)
plt.title('Isomap Embedding of the Swiss Roll')
plt.show()
