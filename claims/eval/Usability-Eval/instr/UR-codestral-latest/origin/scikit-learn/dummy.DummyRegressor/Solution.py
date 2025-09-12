# Import necessary libraries
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Assuming you have your features in X and target variable in y
# Split your data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Decision Tree Regressor model
tree_regression_model = DecisionTreeRegressor(random_state=42)

# Fit the regressor model with the training data
tree_regression_model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = tree_regression_model.predict(X_test)

# Calculate the mean squared error of the predictions
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')
