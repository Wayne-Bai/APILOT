import numpy as np
from sklearn import covariance
from sklearn.model_selection import GridSearchCV

# Generate random data (replace this with your actual data)
np.random.seed(0)
n_samples = 800
n_features = 10
data = np.dot(np.random.randn(n_samples, n_features), np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# Build a covariance matrix
precision = covariance.graph_lasso(data, assume_centered=False)

# Use grid search cross-validation to find the best l1 penalty
Cs = np.logspace(-4, 4, 10)
param_grid = dict(alpha=Cs)

model = covariance.GraphLassoCV( cv=5)
model.fit(data)

print("Best parameters found: ", model.best_params_)
print("Best cross-validation score: ", model.best_score_)
