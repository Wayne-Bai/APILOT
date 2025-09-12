from sklearn.utils import check_random_state
import numpy as np

def generate_sparse_signal(n_sparse, n_features, n_samples, random_state=None):
    """
    Generate a signal as a sparse combination of dictionary elements.

    Parameters:
    - n_sparse: int, number of non-zero elements in each signal.
    - n_features: int, number of features.
    - n_samples: int, number of samples.
    - random_state: int or None, random_state for generating random numbers.

    Returns:
    - Y: A matrix of size (n_features, n_samples) where each row has exactly n_sparse non-zero elements.
    """
    n_components = n_features
    n_nonzero_coefs = n_sparse

    random_state = check_random_state(random_state)
    X = random_state.rand(n_components, n_samples)
    Y = np.dot(X, np.eye(n_components))

    return Y

# Example usage:
n_sparse = 3
n_features = 10
n_samples = 5
random_state = 42

signal = generate_sparse_signal(n_sparse, n_features, n_samples, random_state)
print(signal)
