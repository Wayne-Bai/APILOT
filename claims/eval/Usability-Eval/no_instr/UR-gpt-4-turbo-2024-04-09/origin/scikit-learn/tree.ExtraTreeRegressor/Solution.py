from sklearn.ensemble import ExtraTreesRegressor

# Example data
X = [[0, 0], [1, 1], [2, 2], [3, 3]]  # Example features
y = [0, 1, 2, 3]                      # Corresponding targets

# Create the Extremely Randomized Trees regressor
etr = ExtraTreesRegressor(n_estimators=100, random_state=42)

# Fit the model
etr.fit(X, y)

# Predict using the model
predictions = etr.predict([[1.5, 1.5]])

print(predictions)
