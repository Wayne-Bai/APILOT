from sklearn.linear_model import LassoLars
from sklearn.model_selection import cross_val_score
from sklearn.datasets import make_regression
import numpy as np

# Generate a synthetic dataset
X, y = make_regression(n_samples=100, n_features=10, noise=0.1)

# Initialize the LassoLars model
lasso_lars = LassoLars()

# Fit the model with Lars using BIC for model selection
# We'll use cross-validation to estimate the BIC
cv_scores = cross_val_score(lasso_lars, X, y, cv=5, scoring='bic')
best_alpha = lasso_lars.alpha_

# Fit the final model with the best alpha
final_model = LassoLars(alpha=best_alpha)
final_model.fit(X, y)

# Print the best alpha and the coefficients of the final model
print("Best alpha:", best_alpha)
print("Coefficients:", final_model.coef_)
