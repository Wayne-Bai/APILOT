
from sklearn.linear_model import LinearRegression
import numpy as np

# Create a dataset for training
X = np.array([[0, 0], [1, 1], [2, 2]])
y = np.array([0, 1, 2])

# Create a simple regressor with the LinearRegression class
regressor = LinearRegression()

# Train the regressor on the training data
regressor.fit(X, y)

# Use the trained regressor to make predictions on new data
new_data = np.array([[3, 4]])
predictions = regressor.predict(new_data)
print("Predictions:", predictions)
