# Import necessary modules
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Sample data (replace these with your actual dataset)
X = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
y = [2.5, 3.5, 5.5, 7.5, 9.5]

# Split the dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Decision Tree Regressor
decision_tree_regressor = DecisionTreeRegressor(random_state=42)

# Train the model
decision_tree_regressor.fit(X_train, y_train)

# Make predictions on the test set
y_pred = decision_tree_regressor.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")
