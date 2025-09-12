from sklearn.linear_model import Lasso
from sklearn.datasets import make_sparse_coded_signal
from sklearn.metrics import mean_squared_error

# Generate a sparse coded signal
X, y = make_sparse_coded_signal(n_samples=1000, n_features=100, n_sparsity=10, noise=0.1)

# Convert the data to a sparse matrix
from scipy.sparse import lil_matrix
X_sparse = lil_matrix(X)

# Define the regularization parameter
alpha = 0.1

# Fit the L1-penalized estimator
estimator = Lasso(alpha=alpha, max_iter=10000, copy_X=True, warm_start=False, positive=False, precompute=False, max_iter_predict=1000, tol=0.0001, verbose=0, warm_start_predict=False, positive_threshold=0.0, random_state=None, selection='cyclic')
estimator.fit(X_sparse)

# Get the coefficients
coefficients = estimator.coef_

# Generate a synthetic target variable
y_synthetic = X @ coefficients + 0.1 * y

# Calculate the mean squared error
mse = mean_squared_error(y, y_synthetic)

print("Mean Squared Error:", mse)
