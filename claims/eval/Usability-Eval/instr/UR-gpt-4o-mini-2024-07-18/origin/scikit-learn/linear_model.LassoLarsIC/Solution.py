from sklearn.linear_model import LassoCV
from sklearn.datasets import make_regression
import numpy as np

# Generate synthetic data for demonstration
X, y = make_regression(n_samples=100, n_features=20, noise=0.1)

# Fit Lasso model using Cross-Validation
lasso = LassoCV(cv=5, random_state=0, selection='random', n_alphas=100)
lasso.fit(X, y)

# Get the best alpha using the model
best_alpha = lasso.alpha_
print(f"Best alpha (lambda) selected by LassoCV: {best_alpha}")

# Get the coefficients from the best model
coef = lasso.coef_
print(f"Coefficients from the Lasso model: {coef}")
