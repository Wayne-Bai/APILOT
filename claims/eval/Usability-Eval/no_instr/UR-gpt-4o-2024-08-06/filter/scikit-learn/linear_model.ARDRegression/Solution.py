from sklearn.linear_model import ARDRegression
import numpy as np

# Generate some sample data
np.random.seed(0)
X = np.random.randn(100, 2)  # 100 samples, 2 features
w = np.array([1.5, -3.0])    # True weights
noise = np.random.normal(0, 0.1, size=100)  # Generate some noise

# Generate target data with noise
y = np.dot(X, w) + noise

# Initialize and fit the ARD Regression model
model = ARDRegression()
model.fit(X, y)

# Output the learned parameters
print("Estimated Weights:", model.coef_)
print("Intercept:", model.intercept_)
print("Precision of the weights (Lambda):", model.lambda_)
print("Precision of the noise (Alpha):", model.alpha_)
