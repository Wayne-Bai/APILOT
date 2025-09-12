from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np

# Create sample data
X = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])
y = np.array([1, 3, 5, 7, 9])

# Splitting the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the DecisionTreeRegressor
tree_regressor = DecisionTreeRegressor(random_state=42)

# Train the regressor
tree_regressor.fit(X_train, y_train)

# Make predictions
predictions = tree_regressor.predict(X_test)

# Calculate the mean squared error 
mse = mean_squared_error(y_test, predictions)

print(f"Predictions: {predictions}")
print(f"Mean Squared Error: {mse}")
