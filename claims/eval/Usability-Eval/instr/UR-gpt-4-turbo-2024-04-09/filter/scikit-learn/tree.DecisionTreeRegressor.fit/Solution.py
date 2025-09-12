from sklearn.tree import DecisionTreeRegressor

# Sample dataset
X = [[0, 0], [2, 2], [3, 3], [5, 5]]
y = [0.5, 2.5, 3.5, 5.5]

# Create Decision Tree regressor object
regressor = DecisionTreeRegressor()

# Train the model using the training sets
regressor.fit(X, y)
