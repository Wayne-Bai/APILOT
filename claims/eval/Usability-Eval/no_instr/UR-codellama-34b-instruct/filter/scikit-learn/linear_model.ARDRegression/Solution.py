
from sklearn.linear_model import BayesianARDRegression
from sklearn.datasets import load_boston

# Load the Boston housing dataset
X, y = load_boston(return_X_y=True)

# Initialize the Bayesian ARD regression model
model = BayesianARDRegression(compute_score=True)

# Fit the model to the data
model.fit(X, y)
