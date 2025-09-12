# Import necessary libraries
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import GridSearchCV
import numpy as np

# Generate sample data ( replace with your actual data )
# For this example, let's generate some random data
np.random.seed(0)
X = np.random.rand(100, 5)
y = 3 * X[:, 0] + 2 * X[:, 1] + np.random.randn(100)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale the features using StandardScaler
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Initialize the DecisionTreeRegressor model
tree_regressor = DecisionTreeRegressor(random_state=42)

# Define hyperparameters to tune
param_grid = {
   'max_depth': [3, 5, 10, None],
   'min_samples_split': [2, 5, 10],
   'min_samples_leaf': [1, 5, 10]
}

# Perform grid search to find the best hyperparameters
grid_search = GridSearchCV(tree_regressor, param_grid, cv=5, scoring='neg_mean_squared_error')
grid_search.fit(X_train_scaled, y_train)

# Get the best model and make predictions
best_tree = grid_search.best_estimator_
y_pred = best_tree.predict(X_test_scaled)

# Print the mean squared error to evaluate the model
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')

# Print the best hyperparameters found
print('Best Hyperparameters:', grid_search.best_params_)
