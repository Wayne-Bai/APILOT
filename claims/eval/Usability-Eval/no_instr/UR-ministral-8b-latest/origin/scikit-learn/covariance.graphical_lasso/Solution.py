import numpy as np
from sklearn.covariance import LedoitWolf
from sklearn.utils.validation import check_array

def penalized_covariance_matrix(X, alpha):
    """
    Compute the covariance matrix with L1-penalized regularization.

    Parameters:
    X (array-like): Data matrix with shape (n_samples, n_features)
    alpha (float): Regularization parameter alpha

    Returns:
    ndarray: Penalized covariance matrix
    """
    # Check if input data is a NumPy array
    X = check_array(X)

    # Compute the mean centering matrix
    mean_centered_X = X - np.mean(X, axis=0)

    # Compute the covariance matrix
    cov_matrix = np.cov(mean_centered_X, rowvar=False)

    # Adjust the covariance matrix with L1-penalized regularization
    l1_penalized_cov = ((1 - alpha) * cov_matrix + alpha * np.identity(cov_matrix.shape[0]))

    return l1_penalized_cov

# Example usage
X = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
alpha = 0.1

penalized_cov = penalized_covariance_matrix(X, alpha)
print(penalized_cov)
