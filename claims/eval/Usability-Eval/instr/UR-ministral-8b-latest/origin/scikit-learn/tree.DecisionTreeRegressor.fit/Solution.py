import numpy as np
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.tree import export_text

# Example data: Replace with your actual dataset
# X = np.array([[1, 1], [1, 2], [2, 2], [2, 3]])
# y = np.array([1, 2, 3, 4])

# For this example, using some dummy data
# X = np.random.rand(100, 10)
# y = np.random.rand(100)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a decision tree regressor model
tree_reg = DecisionTreeRegressor(random_state=42)

# Fit the model to the training data
tree_reg.fit(X_train, y_train)

# Make predictions on the testing data
y_pred = tree_reg.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

# Optional: Print the decision tree rules
tree_rules = export_text(tree_reg, feature_names=['feature1', 'feature2'])
print(tree_rules)
