# Import the required libraries
from sklearn.preprocessing import normalize
from sklearn.metrics import pairwise_distances
import numpy as np

# Function to compute L1 distances between X and Y
def compute_l1_distances(X, Y):
    """
    Compute the L1 distances between the vectors in X and Y.

    Args:
        X (np.array): The first set of vectors.
        Y (np.array): The second set of vectors.

    Returns:
        list: A list of L1 distances between the vectors in X and Y.
    """
    # Normalize the vectors in X and Y
    X_normalized = normalize(X)
    Y_normalized = normalize(Y)

    # Compute the L1 distances using pairwise_distances
    distances = pairwise_distances(X_normalized, Y_normalized, metric='minkowski', p=1)

    # Return the L1 distances
    return distances

# Usage example
if __name__ == "__main__":
    # Define the vectors X and Y
    X = np.array([[1, 2], [3, 4], [5, 6]])
    Y = np.array([[7, 8], [9, 10], [11, 12]])

    # Compute the L1 distances
    distances = compute_l1_distances(X, Y)

    # Print the L1 distances
    print(distances)
