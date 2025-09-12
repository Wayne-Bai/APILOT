# Import necessary libraries
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.datasets import load_diabetes
import numpy as np

# Load the diabetes dataset
diabetes = load_diabetes()
X = diabetes.data
y = diabetes.target

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a simple regressor that makes predictions using simple rules
class SimpleRegressor:
    def __init__(self):
        pass

    def fit(self, X, y):
        # Calculate the mean of the target variable
        self.mean_y_ = np.mean(y)

    def predict(self, X):
        # Predict the target variable using the mean
        return np.full(X.shape[0], self.mean_y_)

# Train the simple regressor
simple_regressor = SimpleRegressor()
simple_regressor.fit(X_train, y_train)

# Make predictions on the test set
y_pred_simple = simple_regressor.predict(X_test)

# Calculate the mean squared error of the simple regressor
mse_simple = mean_squared_error(y_test, y_pred_simple)
print(f"Mean Squared Error of Simple Regressor: {mse_simple}")

# Compare with a random forest regressor
rf_regressor = RandomForestRegressor(random_state=42)
rf_regressor.fit(X_train, y_train)

y_pred_rf = rf_regressor.predict(X_test)
mse_rf = mean_squared_error(y_test, y_pred_rf)
print(f"Mean Squared Error of Random Forest Regressor: {mse_rf}")
