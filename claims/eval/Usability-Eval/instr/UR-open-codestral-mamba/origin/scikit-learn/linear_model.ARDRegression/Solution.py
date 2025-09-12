# Import necessary libraries
from sklearn.linear_model import BayesianRidge
from sklearn.datasets import make_regression

# Generate a regression dataset
X, y, coef = make_regression(n_samples=100, n_features=20, n_informative=5, coef=True, random_state=0)

# Initialize Bayesian Ridge Regression object with ARD
br = BayesianRidge(compute_score=True)

# Fit the model to the data
br.fit(X, y)

# Print the learned weights
print("Learned Weights: \n", br.coef_)

# Print the learned precision
print("Learned Precision: \n", br.lambda_)

# Print the learned noise precision
print("Learned Noise Precision: \n", br.alpha_)
