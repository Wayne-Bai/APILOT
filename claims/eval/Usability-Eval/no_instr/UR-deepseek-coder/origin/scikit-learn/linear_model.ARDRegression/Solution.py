import numpy as np
from sklearn.linear_model import ARDRegression

# Example data
X = np.array([[0, 0], [1, 1], [2, 2]])
y = np.array([0, 1, 2])

# Initialize ARDRegression model
ard = ARDRegression()

# Fit the model
ard.fit(X, y)

# Get the weights (coefficients)
weights = ard.coef_

# Get the precision of the weights (lambda)
lambda_values = ard.lambda_

# Get the precision of the noise (alpha)
alpha_value = ard.alpha_

print("Weights:", weights)
print("Lambda values:", lambda_values)
print("Alpha value:", alpha_value)
