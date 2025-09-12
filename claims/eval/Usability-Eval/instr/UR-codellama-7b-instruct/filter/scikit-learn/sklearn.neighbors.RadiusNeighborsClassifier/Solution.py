
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

# Load the iris dataset
iris = datasets.load_iris()
X = iris.data[:, :2]  # we only take the first two features.
y = iris.target

# Train a KNeighborsClassifier on the dataset
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X, y)

# Use the trained model to make predictions on new data
new_samples = np.array([[6.4, 3.2]])
print("Predictions:", knn.predict(new_samples))
