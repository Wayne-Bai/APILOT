from sklearn.dummy import DummyRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import numpy as np

# Sample data: Features (X) and target (y)
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([1.2, 2.3, 3.1, 4.5, 5.1])

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Dummy Regressor
# Using the 'mean' strategy which predicts the mean of the training targets
regressor = DummyRegressor(strategy='mean')

# Fit the model to the training data
regressor.fit(X_train, y_train)

# Make predictions on the test set
y_pred = regressor.predict(X_test)

# Calculate the mean squared error of the model
mse = mean_squared_error(y_test, y_pred)

print("Predictions:", y_pred)
print("Mean Squared Error:", mse)
