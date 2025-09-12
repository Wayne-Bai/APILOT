# Import necessary libraries from scikit-learn
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_boston
from sklearn.linear_model import BayesianRidge
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import StandardScaler
import numpy as np

# Load Boston housing dataset
boston_dataset = load_boston()

# Split data into features and target
X = boston_dataset.data
y = boston_dataset.target

# Create a StandardScaler object to scale the features
scaler = StandardScaler()

# Fit the scaler to the data and transform it
X_scaled = scaler.fit_transform(X)

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Define the hyperparameter grid for tuning
param_grid = {'alpha_1': [1e-4, 1e-3, 1e-2],
              'alpha_2': [1e-4, 1e-3, 1e-2],
              'lambda_1': [1e-5, 1e-4, 1e-3],
              'lambda_2': [1e-5, 1e-4, 1e-3]}

# Initialize the Bayesian Ridge model and a GridSearchCV object
model = BayesianRidge()
grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=5, n_jobs=-1)

# Perform grid search to optimize the hyperparameters
grid_search.fit(X_train, y_train)

# Get the optimized hyperparameters and the best model
optimized_params = grid_search.best_params_
best_model = grid_search.best_estimator_

# Print the optimized hyperparameters
print("Optimized Hyperparameters:")
print(optimized_params)

# Evaluate the best model on the test data
y_pred = best_model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print("\nMean Squared Error on Test Data:", mse)
