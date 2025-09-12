from sklearn import datasets
from sklearn.manifold import Isomap

# Load the iris dataset
iris = datasets.load_iris()
X = iris.data[:, :2]  # we only take the first two features.

# Create an Isomap model with 2 components
model = Isomap(n_components=2)

# Fit the model to the data
model.fit(X)

# Plot the resulting low-dimensional embeddings
import matplotlib.pyplot as plt
plt.scatter(model.embedded[:, 0], model.embedded[:, 1])
plt.xlabel("Isomap 1")
plt.ylabel("Isomap 2")
plt.show()
