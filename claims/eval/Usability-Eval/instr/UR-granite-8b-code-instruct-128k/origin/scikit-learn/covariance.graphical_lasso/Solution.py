from sklearn.linear_model import LinearRegression
import numpy as np

# Create some example data
X = np.array([[1, 2], [3, 4], [5, 6]])
y = np.array([1, 2, 3])

# Create a LinearRegression object
model = LinearRegression()

# Fit the model to the data
model.fit(X, y)

# Make some predictions
predictions = model.predict(X)

# Print the coefficients of the model
print("Coefficients:", model.coef_)
