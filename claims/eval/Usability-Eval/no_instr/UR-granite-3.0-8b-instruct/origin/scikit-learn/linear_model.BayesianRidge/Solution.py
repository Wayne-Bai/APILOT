from sklearn.linear_model import BayesianRidge
import numpy as np

# Assuming X and y are your feature matrix and target variable
X = np.array([[1], [2], [3], [4]])
y = np.array([2, 4, 6, 8])

# Initialize the BayesianRidge model
bayesian_ridge = BayesianRidge()

# Fit the model to the data
bayesian_ridge.fit(X, y)

# Print the coefficients and intercept
print("Coefficients: ", bayesian_ridge.coef_)
print("Intercept: ", bayesian_ridge.intercept_)
