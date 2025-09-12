from sklearn.neighbors import RadiusNeighborsClassifier
import numpy as np

# Sample data: features (X) and labels (y)
X = np.array([[1, 2], [2, 3], [3, 4], [5, 5], [6, 7]])
y = np.array([0, 0, 0, 1, 1])

# Initialize the RadiusNeighborsClassifier with a specified radius
radius_classifier = RadiusNeighborsClassifier(radius=1.5)

# Fit the classifier to the data
radius_classifier.fit(X, y)

# Sample new data to classify
new_data = np.array([[2, 2], [5, 6]])

# Predict the labels for the new data
predictions = radius_classifier.predict(new_data)

print(predictions)
