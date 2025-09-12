from sklearn.neighbors import RadiusNeighborsClassifier

# Example usage
# Create sample data
X_train = [[0, 0], [1, 1], [2, 2], [3, 3]]
y_train = [0, 0, 1, 1]

# Create the RadiusNeighborsClassifier
radius_clf = RadiusNeighborsClassifier(radius=1.5, weights='uniform')

# Fit the classifier
radius_clf.fit(X_train, y_train)

# Predict with new data
X_test = [[1.5, 1.5], [3, 3]]
predictions = radius_clf.predict(X_test)

print("Predictions:", predictions)
