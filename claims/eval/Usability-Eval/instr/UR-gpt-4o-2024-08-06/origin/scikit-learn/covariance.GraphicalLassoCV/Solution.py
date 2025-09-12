import numpy as np
from sklearn.model_selection import GridSearchCV
from sklearn.covariance import GraphicalLasso
from sklearn.datasets import make_sparse_spd_matrix

# Generate a random sparse matrix
n_features = 10
precision = make_sparse_spd_matrix(n_features, alpha=0.95, random_state=42)
covariance = np.linalg.inv(precision)
data = np.random.multivariate_normal(np.zeros(n_features), covariance, size=100)

# Cross-validated choice of the l1 penalty
param_grid = {'alpha': np.logspace(-4, 0, 50)}
graphical_lasso_model = GraphicalLasso()

# Using GridSearchCV to find the best alpha
cv = GridSearchCV(graphical_lasso_model, param_grid, cv=5)
cv.fit(data)

best_model = cv.best_estimator_

# Output best found alpha
print("Best alpha found:", cv.best_params_['alpha'])
# Output precision matrix
print("Estimated precision matrix:\n", best_model.precision_)
