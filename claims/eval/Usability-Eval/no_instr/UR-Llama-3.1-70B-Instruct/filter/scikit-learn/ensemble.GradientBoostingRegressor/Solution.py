# Import necessary libraries
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.datasets import make_regression
import numpy as np
import pandas as pd

# Generate a regression dataset
X, y = make_regression(n_samples=1000, n_features=10, n_informative=5, noise=0.1)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Gradient Boosting Regressor model
gbr_model = GradientBoostingRegressor(
    n_estimators=100,
    learning_rate=0.1,
    max_depth=3,
    min_samples_split=2,
    min_samples_leaf=1,
    subsample=1,
    random_state=42
)

# Train the model on the training data
gbr_model.fit(X_train, y_train)

# Make predictions on the test data
y_pred = gbr_model.predict(X_test)

# Evaluate the model using different metrics
mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print("Mean Squared Error: %.2f" % mse)
print("Mean Absolute Error: %.2f" % mae)
print("R-squared: %.2f" % r2)
