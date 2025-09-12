from sklearn.neighbors import RadiusNeighborsClassifier

# Create the RadiusNeighborsClassifier object
# radius defines the range to look for neighbors
radius = 5.0
classifier = RadiusNeighborsClassifier(radius=radius)

# Sample data
# X represents features and y represents labels
X = [[2, 3], [5, 4], [9, 6], [4, 7], [8, 1], [7, 2]]
y = [0, 1, 1, 0, 1, 1]

# Train the classifier
classifier.fit(X, y)

# Predicting new data points
new_points = [[3, 4], [7, 3]]
predictions = classifier.predict(new_points)

print("Predictions:", predictions)
