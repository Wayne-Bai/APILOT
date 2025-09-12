import numpy as np
from sklearn.linear_model import ARDRegression

# Example data
X = np.array([[0, 0], [1, 1], [2, 2]])
y = np.array([0, 1, 2])

# Initialize the ARDRegression model
ard = ARDRegression()

# Fit the model
ard.fit(X, y)

# Get the estimated weights (coefficients)
weights = ard.coef_

# Get the estimated precision of the weights (lambda)
lambda_values = ard.lambda_

# Get the estimated precision of the noise (alpha)
alpha_value = ard.alpha_

print("Estimated Weights:", weights)
print("Estimated Lambda (precisions of the weights):", lambda_values)
print("Estimated Alpha (precision of the noise):", alpha_value)
