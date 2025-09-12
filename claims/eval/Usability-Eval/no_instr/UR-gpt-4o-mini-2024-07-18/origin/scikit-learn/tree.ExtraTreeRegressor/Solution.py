from sklearn.ensemble import ExtraTreesRegressor

# Create an instance of the Extremely Randomized Tree Regressor
regressor = ExtraTreesRegressor(n_estimators=100, random_state=42)

# Example data - Replace with your own dataset
X_train = [[1, 2], [3, 4], [5, 6], [7, 8]]
y_train = [1, 2, 3, 4]

# Fit the model
regressor.fit(X_train, y_train)

# Make predictions - Replace with your own test data
X_test = [[2, 3], [6, 7]]
predictions = regressor.predict(X_test)

print(predictions)
