from sklearn.linear_model import LassoLars
from sklearn.metrics import log_likelihood
import numpy as np

# Assuming X is the feature matrix and y is the target variable
# X = ...
# y = ...

# Initialize LassoLars model
lasso_lars = LassoLars()

# Fit the model
lasso_lars.fit(X, y)

# Get the coefficients
coef = lasso_lars.coef_

# Calculate BIC and AIC
bic = np.log(len(y)) * len(coef) + 2 * np.sum(np.abs(coef))
aic = np.log(len(y)) - 2 * np.sum(np.log(np.abs(coef)))

print("BIC: ", bic)
print("AIC: ", aic)
