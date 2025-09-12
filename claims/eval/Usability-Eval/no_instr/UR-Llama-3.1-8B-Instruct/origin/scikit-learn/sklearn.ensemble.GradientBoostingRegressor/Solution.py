# Import necessary libraries
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import GridSearchCV
import numpy as np

# Load Boston housing dataset
boston = load_boston()

# Split the dataset into features and target variable
X = boston.data
y = boston.target

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Gradient Boosting regressor
gbr = GradientBoostingRegressor()

# Define the hyperparameters to tune
param_grid = {
    'n_estimators': [50, 100, 150],
    'learning_rate': [0.1, 0.05, 0.01],
   'max_depth': [3, 6, 9],
   'min_samples_split': [2, 5, 10],
   'min_samples_leaf': [1, 5, 10]
}

# Initialize the GridSearchCV object
grid_search = GridSearchCV(estimator=gbr, param_grid=param_grid, cv=5, scoring='neg_mean_squared_error')

# Perform grid search
grid_search.fit(X_train, y_train)

# Get the best parameters and the best estimator
best_params = grid_search.best_params_
best_estimator = grid_search.best_estimator_

# Make predictions on the test set
y_pred = best_estimator.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print(f'Best Parameters: {best_params}')
print(f'NB Test MSE: {mse}')
