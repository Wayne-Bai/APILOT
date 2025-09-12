from sklearn import datasets
from sklearn.manifold import Isomap
import matplotlib.pyplot as plt

# Load the dataset
iris = datasets.load_iris()
X = iris.data
y = iris.target

# Perform Isomap Embedding
isomap = Isomap(n_components=2, n_neighbors=5)
X_2d = isomap.fit_transform(X)

# Plot the results
plt.scatter(X_2d[:, 0], X_2d[:, 1], c=y)
plt.colorbar()
plt.show()
