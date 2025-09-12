
from sklearn.covariance import GraphicalLassoCV
from sklearn.model_selection import GridSearchCV

# Define parameter grid for the graphical lasso with cross-validated choice of l1 penalty
param_grid = {'alpha': np.logspace(-3, 3, 5)}

# Perform grid search over the parameter grid
cv = GridSearchCV(GraphicalLassoCV(), param_grid, cv=5)
cv.fit(X)

# Extract best estimator and best parameters from the grid search result
best_estimator = cv.best_estimator_
best_params = cv.best_params_

# Print the best estimator and best parameters
print("Best Estimator:", best_estimator)
print("Best Parameters:", best_params)
