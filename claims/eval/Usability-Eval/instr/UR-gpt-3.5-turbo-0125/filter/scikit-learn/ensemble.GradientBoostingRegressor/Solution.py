
# Import necessary libraries
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor

# Generate random data for demonstration purposes
np.random.seed(0)
X = np.random.rand(100, 1)
y = 2.0 + 3.0 * X.ravel() + np.random.normal(0, 1, 100)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Create a Gradient Boosting Regressor model
params = {'n_estimators': 500, 'max_depth': 4, 'min_samples_split': 5,
          'learning_rate': 0.01, 'loss': 'ls'}
gb_regressor = GradientBoostingRegressor(**params)

# Fit the model on the training data
gb_regressor.fit(X_train, y_train)

# Predict on the test data
y_pred = gb_regressor.predict(X_test)

# Print the first 5 true values and predictions
print("True Values:", y_test[:5])
print("Predictions:", y_pred[:5])
