# Import necessary libraries from scikit-learn
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import GridSearchCV
import numpy as np

# Generate random data
np.random.seed(0)
X = np.random.rand(100, 1)
y = 3 + 2 * X + np.random.randn(100, 1)

# Split dataset into features (X) and labels (y)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the decision tree regressor
regr = DecisionTreeRegressor(random_state=42)

# Update the code below for the new decision tree regressor in scikit-learn
# parameters to tweak for hyperparameter tuning 
param_grid = {
   'max_depth': np.arange(1, 11),
   'min_samples_split': np.arange(2, 11),
   'min_samples_leaf': np.arange(1, 11),
}
# Perform grid search for the best parameters
grid_search = GridSearchCV(regr, param_grid, cv=5)
grid_search.fit(X_train, y_train.squeeze())  # Update the code here

# Predict on the test set
y_pred = grid_search.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error (MSE):", mse)

# Print the best parameters found by the grid search
print("Best Parameters:", grid_search.best_params_)
