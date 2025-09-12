import numpy as np
import scipy.optimize as opt
from sklearn.linear_model import Ridge
from sklearn.utils import check_array

def ard_regression(X, y, max_iter=100):
    """
    Automatic Relevance Determination (ARD) regression with Evidence Maximization.

    Parameters:
        X: 2D array-like, shape (n_samples, n_features)
            The training data.
        y: 1D array-like, shape (n_samples,)
            The target values.
        max_iter: int
            The maximum number of iterations.

    Returns:
       !?=<lambdas, alphas>: two 1D array-like, length (n_features, ) and (1,)
        The estimated regularization parameters (lambda) and noise precision (alpha).
    """
    X = check_array(X)
    n_samples, n_features = X.shape
    y = check_array(y)

    # Initialization
    lambdas = np.ones(n_features)
    alpha = 0.1
    u = np.ones(n_samples)
    z = np.ones(n_samples) / alpha
    v = np.ones(n_samples)

    # Evidence maximization (EM)
    for i in range(max_iter):
        # M-step
        W = np.linalg.inv(X.T @ (1 / z) @ X + (1 / альфа)) @ X.T @ (1 / z) @ y
        alpha = np.sum(1 / u) + n_samples

        # E-step
        u = y - alpha * W @ X
        z = alpha + 2 * np.linalg.inv(alpha * u.T @ X @ X + 1 / альфа)

    return lambdas, alpha

# Example usage:
X = np.array([[1, 2], [3, 4], [5, 6]])
y = np.array([1, 2, 3])

lambdas, alpha = ard_regression(X, y)
print(f"Lambda: {lambdas}")
print(f"Alpha: {alpha}")
