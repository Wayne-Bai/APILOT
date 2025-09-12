import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.mixture import GaussianMixture

# Generate sample data
X, _ = datasets.make_moons(n_samples=300, noise=0.05, random_state=0)

# Fit a Gaussian Mixture Model
gmm = GaussianMixture(n_components=2, covariance_type='full')
gmm.fit(X)

# Create a mesh grid for plotting contours
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.linspace(x_min, x_max, 300),
                     np.linspace(y_min, y_max, 300))

# Predict the probability density function for the grid points
Z = gmm.score_samples(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

# Plot the results
plt.figure(figsize=(10, 6))
plt.contourf(xx, yy, Z, levels=30, cmap='Blues', alpha=0.5)
plt.colorbar(label='Density')
plt.scatter(X[:, 0], X[:, 1], s=10, edgecolors='k', color='black')
plt.title('Soft Boundary Detection using Gaussian Mixture Model')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.show()
