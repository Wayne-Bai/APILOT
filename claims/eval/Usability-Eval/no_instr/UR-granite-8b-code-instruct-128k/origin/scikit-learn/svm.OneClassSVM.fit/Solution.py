from sklearn.datasets import make_moons
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# Generate the data
X, y = make_moons(n_samples=1000, noise=0.2)

# Reduce the dimensionality using PCA
pca = PCA(n_components=2)
X_2d = pca.fit_transform(X)

# Plot the results
plt.scatter(X_2d[:, 0], X_2d[:, 1], c=y)
plt.show()
