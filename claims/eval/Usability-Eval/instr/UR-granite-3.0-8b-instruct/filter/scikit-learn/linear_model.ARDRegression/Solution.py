from sklearn.linear_model import Ridge
from sklearn.model_selection import GridSearchCV
import numpy as np

# Generate some data
X = np.random.rand(100, 5)
y = np.dot(X, np.array([1, 2, 0, -1, 3])) + np.random.randn(100)

# Initialize the Ridge regression model with ARD prior
ridge_ard = Ridge(alpha=1.0, fit_intercept=True, normalize=False, copy_X=True, max_iter=None, tol=0.001, solver='sag', random_state=None)

# Define the grid of alpha values to search over
alpha_grid = np.logspace(-4, 4, 100)

# Define the grid of lambda values to search over
lambda_grid = np.logspace(-4, 4, 100)

# Define the grid of alpha and lambda values to search over
param_grid = {'alpha': alpha_grid, 'lambda_': lambda_grid}

# Use GridSearchCV to find the best alpha and lambda values
grid_search = GridSearchCV(ridge_ard, param_grid, cv=5, scoring='neg_mean_squared_error', verbose=2, n_jobs=-1)
grid_search.fit(X, y)

# Print the best alpha and lambda values
print("Best alpha: ", grid_search.best_params_['alpha'])
print("Best lambda: ", grid_search.best_params_['lambda_'])

# Print the best model
print("Best model: ", grid_search.best_estimator_)
