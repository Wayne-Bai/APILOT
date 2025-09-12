# Import necessary libraries
from sklearn.linear_model import BayesianRidge
import numpy as np
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split

# Generate a random regression dataset
X, y = make_regression(n_samples=100, n_features=10, n_targets=1, noise=0.1, random_state=42)

# Split the dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a BayesianRidge object with default parameters
bayesian_ridge = BayesianRidge()

# Fit the BayesianRidge model to the training data
bayesian_ridge.fit(X_train, y_train)

# Print the coefficients of the model
print("Coefficients: ", bayesian_ridge.coef_)

# Print the intercept of the model
print("Intercept: ", bayesian_ridge.intercept_)

# Print the log marginal likelihood of the model
print("Log marginal likelihood: ", bayesian_ridge.slog_)

# Make predictions on the test set
y_pred = bayesian_ridge.predict(X_test)

# Print the predicted values
print("Predicted values: ", y_pred)
