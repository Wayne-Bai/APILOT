# Import necessary libraries
from sklearn.datasets import make_moons
from sklearn.manifold import Isomap
import matplotlib.pyplot as plt
import numpy as np

# Generate the sample data
np.random.seed(0)
X, _ = make_moons(n_samples=200, noise=0.05, random_state=0)

# Perform Isomap embedding
isomap = Isomap(n_neighbors=10, n_components=2)
isomap_X = isomap.fit_transform(X)

# Plot the original and Isomap-embedded data
plt.figure(figsize=(10, 5))
plt.subplot(121)
plt.scatter(X[:, 0], X[:, 1])
plt.title('Original Data')

plt.subplot(122)
plt.scatter(isomap_X[:, 0], isomap_X[:, 1])
plt.title('Isomap-Embedded Data')
plt.show()
