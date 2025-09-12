import numpy as np
from sklearn.linear_model import BayesianRidge

# Generate some sample data
np.random.seed(0)
X = np.random.randn(100, 10)
y = X @ np.random.randn(10) + np.random.randn(100) * 0.1  # Linear relationship with noise

# Create and fit the Bayesian Ridge regression model with ARD
model = BayesianRidge(compute_score=True)
model.fit(X, y)

# Output the model parameters
print("Weights (coef):", model.coef_)
print("Alpha (noise precision):", model.alpha_)
print("Lambda (weights precision):", model.lambda_)
