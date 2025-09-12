from sklearn.neighbors import RadiusNeighborsClassifier

# Example configuration: radius set to 1.0
radius = 1.0
classifier = RadiusNeighborsClassifier(radius=radius)

# Sample training data (X_train with features and y_train with corresponding labels)
X_train = [[1, 1], [1.5, 1.8], [2, 2], [8, 8], [8.5, 8.5], [9, 9]]
y_train = [0, 0, 0, 1, 1, 1]

# Fitting the model with the training data
classifier.fit(X_train, y_train)

# Sample new data to classify
X_new = [[1, 1], [2, 2], [9, 9], [10, 10]]

# Making predictions
predictions = classifier.predict(X_new)
print("Predictions:", predictions)
