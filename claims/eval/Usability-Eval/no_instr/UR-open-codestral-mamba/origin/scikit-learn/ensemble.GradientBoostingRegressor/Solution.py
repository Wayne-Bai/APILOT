from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import GradientBoostingRegressor
import numpy as np

# Generate a random regression problem
X, y = make_regression(n_samples=1000, n_features=10, noise=0.1, random_state=42)

# Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define the Gradient Boosting Regressor
gbr = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=1, random_state=42)

# Fit the model
gbr.fit(X_train, y_train)

# Make predictions using the test set
y_pred = gbr.predict(X_test)

# Calculate mean_squared_error
mse = mean_squared_error(y_test, y_pred)

print(f"Mean Squared Error: {mse}")
