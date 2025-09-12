from sklearn.linear_model import LinearRegression
import numpy as np
# Create some example data
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 6, 8, 10])
# Create a Linear Regression model
regressor = LinearRegression()
# Fit the model to the data
regressor.fit(X, y)
# Make a prediction for a new value
new_value = [[6]]
prediction = regressor.predict(new_value)
print(prediction)
