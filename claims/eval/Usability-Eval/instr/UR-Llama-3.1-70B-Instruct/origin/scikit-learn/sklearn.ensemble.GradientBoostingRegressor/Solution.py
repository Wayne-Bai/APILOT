# Import necessary libraries
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_regression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import GridSearchCV
import numpy as np

# Create a random regression dataset
X, y = make_regression(n_samples=1000, n_features=20, noise=0.1, random_state=1)

# Split the dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

# Define the hyperparameter tuning space
param_grid = {
    'n_estimators': [100, 200, 300],
    'learning_rate': [0.1, 0.05, 0.01],
   'max_depth': [3, 5, 7],
   'min_samples_split': [2, 5, 10]
}

# Perform grid search for hyperparameter tuning
gbr_model = GradientBoostingRegressor()
grid_search = GridSearchCV(gbr_model, param_grid, cv=5, scoring='neg_mean_squared_error')
grid_search.fit(X_train, y_train)

# Get the best model and its parameters
best_model = grid_search.best_estimator_
best_params = grid_search.best_params_

# Evaluate the best model
y_pred = best_model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)

# Print the results
print('Best Parameters:', best_params)
print('RMSE:', rmse)
