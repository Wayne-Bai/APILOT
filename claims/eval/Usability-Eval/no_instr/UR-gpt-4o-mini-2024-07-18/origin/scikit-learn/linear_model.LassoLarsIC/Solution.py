import numpy as np
import pandas as pd
from sklearn.linear_model import LassoLarsCV
from sklearn.datasets import make_regression

# Generate sample data
X, y = make_regression(n_samples=100, n_features=10, noise=0.1)

# Initialize LassoLarsCV with BIC for model selection
lasso = LassoLarsCV(cv=5, criterion='bic')

# Fit the model
lasso.fit(X, y)

# Get the best alpha
best_alpha = lasso.alpha_
print(f"Best alpha value selected: {best_alpha}")

# Coefficients of the fitted model
coefficients = lasso.coef_
print(f"Coefficients: {coefficients}")
