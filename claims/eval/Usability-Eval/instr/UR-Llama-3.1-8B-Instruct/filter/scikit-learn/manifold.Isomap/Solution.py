# Import necessary libraries from scikit-learn
from sklearn.datasets import load_iris
from sklearn.isomap import Isomap
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset (replace with your own dataset if needed)
iris = load_iris()
X = iris.data[:, :2]  # we only take the first two features.

# Create an Isomap instance with n_neighbors and n_components
n_neighbors = 5
n_components = 2
isomap = Isomap(n_neighbors=n_neighbors, n_components=n_components)

# Fit and transform the data
embedding = isomap.fit_transform(X)

# Print the embedding coordinates
print("Embedded coordinates:")
print(embedding)

# Plot the embedded data points
plt.figure(figsize=(8, 6))
plt.scatter(embedding[:, 0], embedding[:, 1], c=iris.target)
plt.xlabel('First isomap co-ordinate')
plt.ylabel('Second isomap co-ordinate')
plt.title('Isomap embedding of 2D Iris data')
plt.show()
