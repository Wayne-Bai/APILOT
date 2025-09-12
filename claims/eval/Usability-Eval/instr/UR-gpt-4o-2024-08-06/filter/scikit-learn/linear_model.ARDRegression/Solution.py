from sklearn.linear_model import ARDRegression
import numpy as np

# Generate some synthetic data for demonstration
np.random.seed(0)
X = np.random.randn(100, 2)
w = np.array([1.5, -2.0])
y = np.dot(X, w) + np.random.normal(0, 0.5, size=X.shape[0])

# Initialize and fit the ARD Regression model
ard = ARDRegression()
ard.fit(X, y)

# Output the estimated coefficients, lambda and alpha values
print("Estimated coefficients:", ard.coef_)
print("Lambda (precision of the weights):", ard.lambda_)
print("Alpha (precision of the noise):", ard.alpha_)
