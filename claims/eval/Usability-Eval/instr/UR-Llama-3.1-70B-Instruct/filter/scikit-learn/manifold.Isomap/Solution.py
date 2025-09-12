# Import necessary libraries
from sklearn.manifold import MDS
from sklearn.datasets import make_s_curve
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create a 3D S-curve dataset
n_points = 1000
X, color = make_s_curve(n_points, random_state=0)

# Perform Isomap embedding using MDS with dense metric as 'precomputed' 
# is not a valid option. The dense metric 'euclidean' is used by default.
n_components = 2
n_neighbors = 10

# Note: sklearn.manifold.Isomap was deprecated in version 1.2.0 and will be 
# removed in 1.4.0. We use MDS as a replacement.

mds = MDS(n_components=n_components)
pos = mds.fit_transform(X)

# We then plot the position of the points in the 2D-dimensional space.
plt.figure(figsize=(15, 8))
plt.subplot(121, projection='3d')
plt.scatter(X[:, 0], X[:, 1], X[:, 2], c=color, cmap=plt.cm.rainbow)
plt.title("Original Space")

plt.subplot(122)
plt.scatter(pos[:, 0], pos[:, 1], c=color, cmap=plt.cm.rainbow)
plt.title("Projected Space via MDS")

plt.show()
