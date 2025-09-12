from sklearn.manifold import Isomap
from sklearn.datasets import make_swiss_roll
import matplotlib.pyplot as plt

# Generate a Swiss roll dataset
X, _ = make_swiss_roll(n_samples=1000, noise=0.1)

# Create an Isomap embedding
iso = Isomap(n_components=2, n_neighbors=10)
X_iso = iso.fit_transform(X)

# Plot the original and embedded data
fig, ax = plt.subplots()
ax.scatter(X[:, 0], X[:, 1], c=X[:, 2], cmap='viridis')
ax.scatter(X_iso[:, 0], X_iso[:, 1], c=X[:, 2], cmap='viridis')
plt.show()
