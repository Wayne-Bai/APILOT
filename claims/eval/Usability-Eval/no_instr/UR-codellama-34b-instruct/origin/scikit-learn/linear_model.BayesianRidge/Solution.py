from sklearn.linear_model import BayesianRidge
import numpy as np

# Generate some sample data
X = np.random.rand(100, 10)
y = np.random.rand(100)

# Fit the Bayesian ridge model
br = BayesianRidge()
br.fit(X, y)

# Print the coefficients and intercept
print(f"Coefficients: {br.coef_}")
print(f"Intercept: {br.intercept_}")
