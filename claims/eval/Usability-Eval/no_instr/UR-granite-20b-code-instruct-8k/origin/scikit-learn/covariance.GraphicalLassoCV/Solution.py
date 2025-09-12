from sklearn.covariance import sparse_inverse_covariance
from sklearn.model_selection import GridSearchCV
from sklearn.datasets import make_sparse_spd_matrix

# Generate a sparse random positive-definite matrix
np.random.seed(0)
n_samples, n_features = 50, 20
random_matrix = make_sparse_spd_matrix(n_features, alpha=0.98)

# Create a ground truth covariance matrix
ground_truth = np.cov(np.dot(np.random.randn(n_samples, n_features), random_matrix))

# Define the parameter grid for the GridSearchCV
param_grid = {'penalize_cholesky': [True, False], 'tol': [1e-3, 1e-6]}

# Initialize the GridSearchCV with the sparse_inverse_covariance estimator and the parameter grid
grid = GridSearchCV(sparse_inverse_covariance, param_grid=param_grid)

# Fit the GridSearchCV on the ground truth covariance matrix
grid.fit(ground_truth)

# Print the best parameters found by the GridSearchCV
print("Best parameters:", grid.best_params_)
