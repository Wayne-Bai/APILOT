from sklearn.ensemble import GradientBoostingRegressor

# Creating the model
model = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42)

# Example data
X = [[1, 2], [3, 4], [5, 6], [7, 8]]  # Feature vectors
y = [1, 2, 3, 4]  # Target values

# Training the model
model.fit(X, y)

# Making predictions
predictions = model.predict([[5, 5], [2, 1]])
print(predictions)
