import numpy as np
from sklearn.linear_model import Lars
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import GridSearchCV

# Generate some random data for demonstration purposes
X = np.random.rand(100, 10)
y = np.random.rand(100)

# Define the Lasso model with Lars and AIC or BIC for model selection
lasso_lars = Lars(fit_intercept=True)
model_selection = GridSearchCV(lasso_lars, cv=5, scoring='neg_mean_squared_error')

# Fit the model to the data and print the best parameters
model_selection.fit(X, y)
print('Best alpha value:', model_selection.best_params_)
