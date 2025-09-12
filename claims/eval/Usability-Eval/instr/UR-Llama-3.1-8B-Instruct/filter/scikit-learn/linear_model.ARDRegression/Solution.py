# Import required libraries
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from scipy.optimize import minimize
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

# Generate some sample data
np.random.seed(0)
X = np.sort(np.random.rand(100, 2))
y = 2 + 1.5 * np.sin(1.3 * X[:, 0]) + 2.7 * np.sin(0.9 * X[:, 1]) + np.random.randn(100)

# Fit a polynomial regression
poly = PolynomialFeatures(interaction_only=True)
X_poly = poly.fit_transform(X)
model = LinearRegression()
model.fit(X_poly, y)

# Use the weights from the polynomial regression as the initial guess
n_features = X.shape[1]
initial_weights = model.coef_
initial_alpha = 1e-4
initial_lambda = np.ones(n_features) * 1e-4
