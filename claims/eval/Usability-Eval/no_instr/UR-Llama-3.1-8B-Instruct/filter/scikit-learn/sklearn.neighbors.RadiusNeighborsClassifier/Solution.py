# Import necessary libraries from scikit-learn
from sklearn.neighbors import KNeighborsClassifier
from sklearn import datasets
import numpy as np
import matplotlib.pyplot as plt

# Load iris dataset
iris = datasets.load_iris()
X = iris.data
y = iris.target

# Define a grid of x and y values
h =.02  # step size in the mesh
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                     np.arange(y_min, y_max, h))

# Create a KNN classifier
knn = KNeighborsClassifier(n_neighbors=5, weights='distance', radius=1.5)

# Train the classifier
knn.fit(X, y)

# Make predictions on the grid
Z = knn.predict(np.c_[xx.ravel(), yy.ravel()])

# Plot the grid
plt.contourf(xx, yy, Z.reshape(xx.shape), alpha=0.8)
plt.scatter(X[:, 0], X[:, 1], c=y)
plt.show()
