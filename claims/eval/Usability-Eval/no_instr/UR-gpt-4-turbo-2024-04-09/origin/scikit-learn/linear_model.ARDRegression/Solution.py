from sklearn.linear_model import ARDRegression
import numpy as np

# Example data
X = np.array([[1, 1], [2, 2], [3, 3]])
y = np.array([1, 2, 3])

# Create and fit the ARD Regression model
model = ARDRegression()
model.fit(X, y)

# Display the estimated parameters
print("Estimated coefficients:", model.coef_)
print("Estimated intercept:", model.intercept_)
print("Lambda (precision of the weights):", model.lambda_)
print("Alpha (precision of the noise):", model.alpha_)
