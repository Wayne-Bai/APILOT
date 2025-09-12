
import numpy as np
from sklearn.linear_model import BayesianRidge

# Generate some sample data
X = np.random.rand(100, 10)
y = np.random.rand(100)

# Fit a Bayesian Ridge regression model
bayesian_ridge = BayesianRidge()
bayesian_ridge.fit(X, y)
