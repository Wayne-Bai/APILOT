import numpy as np
from sklearn.linear_model import LassoLarsIC

# Example data
X = np.array([[0, 0], [1, 1], [2, 2]])
y = np.array([0, 1, 2])

# Initialize the LassoLarsIC model with BIC criterion
lasso_lars_bic = LassoLarsIC(criterion='bic')

# Fit the model
lasso_lars_bic.fit(X, y)

# Print the selected alpha
print(f"Best alpha using BIC: {lasso_lars_bic.alpha_}")

# Initialize the LassoLarsIC model with AIC criterion
lasso_lars_aic = LassoLarsIC(criterion='aic')

# Fit the model
lasso_lars_aic.fit(X, y)

# Print the selected alpha
print(f"Best alpha using AIC: {lasso_lars_aic.alpha_}")
