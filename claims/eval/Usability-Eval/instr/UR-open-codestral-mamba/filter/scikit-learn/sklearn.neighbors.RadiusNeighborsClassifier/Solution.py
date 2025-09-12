from sklearn.neighbors import RadiusNeighborsClassifier

# Sample data
X = [[1., 2.], [2., 2.], [2., 3.], [3., 1.], [3., 2.], [3., 3.]]
Y = [0, 0, 1, 1, 1, 1]

# Create a RadiusNeighborsClassifier with radius 1.5
model = RadiusNeighborsClassifier(radius=1.5)

# Fit the model to the training data
model.fit(X, Y)

# Predict the class for a given point [2., 3.]
predicted_class = model.predict([[2., 3.]])

print(predicted_class)
