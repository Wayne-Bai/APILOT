# Import necessary libraries
from sklearn.utils import check_random_state
from sklearn.utils.linear_assignment_ import linear_assignment
import numpy as np

# Define the function to generate sparse signal
def generate_sparse_signal(n_components, n_samples, n_features, n_nonzero_coefs):
    """
    Generate a signal as a sparse combination of dictionary elements.

    Parameters:
    - n_components: The number of atoms in the dictionary
    - n_samples: The number of samples
    - n_features: The number of features
    - n_nonzero_coefs: The number of non-zero coefficients per sample

    Returns:
    - D: Dictionary (n_features, n_components)
    - X: Non-zero coefficients (n_components, n_samples)
    - Y: Reconstructed signal (n_features, n_samples)
    """
    # Set random seed for reproducibility
    random_state = check_random_state(None)

    # Generate random dictionary elements
    D = random_state.randn(n_features, n_components)

    # Initialize non-zero coefficients matrix
    X = np.zeros((n_components, n_samples))

    # Generate sparse coefficients for each sample
    for i in range(n_samples):
        # Get indices of non-zero coefficients
        indices = random_state.choice(n_components, size=n_nonzero_coefs, replace=False)
        
        # Set non-zero coefficients to random values
        X[indices, i] = random_state.randn(n_nonzero_coefs)

    # Reconstruct signal using dictionary and coefficients
    Y = np.dot(D, X)

    return D, X, Y

# Example usage
n_components = 100
n_samples = 10
n_features = 200
n_nonzero_coefs = 5

D, X, Y = generate_sparse_signal(n_components, n_samples, n_features, n_nonzero_coefs)

print("Dictionary shape:", D.shape)
print("Coefficients shape:", X.shape)
print("Reconstructed signal shape:", Y.shape)
