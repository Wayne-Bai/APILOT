# Import necessary libraries
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np

# Generate a random dataset for demonstration purposes
np.random.seed(0)
X = np.random.rand(100, 3)
y = 3 * X[:, 0] + 2 * X[:, 1] + np.random.randn(100)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train a decision tree regressor
tree = DecisionTreeRegressor(random_state=42)
tree.fit(X_train, y_train)

# Make predictions using the trained decision tree regressor
y_pred = tree.predict(X_test)

# Evaluate the performance of the decision tree regressor
mse = mean_squared_error(y_test, y_pred)
print(f"Mean squared error: {mse}")
