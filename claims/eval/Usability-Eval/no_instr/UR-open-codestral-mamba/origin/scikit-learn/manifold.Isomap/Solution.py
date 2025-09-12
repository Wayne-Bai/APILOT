from sklearn.manifold import Isomap
from sklearn import datasets
import matplotlib.pyplot as plt

# Load some test data
iris = datasets.load_iris()
X = iris.data
y = iris.target

# Apply Isomap embedding
isomap = Isomap(n_components=2)
iso_X = isomap.fit_transform(X)

# Plot the results
plt.scatter(iso_X[:, 0], iso_X[:, 1], c=y)
plt.show()
