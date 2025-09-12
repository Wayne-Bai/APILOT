# Import necessary modules from scikit-learn
from sklearn.metrics.pairwise import pairwise_distances

# Function to compute L1 distances between vectors in X and Y
def compute_l1_distances(X, Y):
    """
    Compute the L1 distances between the vectors in X and Y.

    Parameters:
    X (array-like): First set of vectors.
    Y (array-like): Second set of vectors.

    Returns:
    matrix: A matrix of L1 distances between the vectors in X and Y.
    """
    # Compute pairwise L1 distances
    distances = pairwise_distances(X, Y, metric='l1')

    return distances


# Example usage
if __name__ == "__main__":
    # Import numpy for numerical operations
    import numpy as np

    # Create two datasets of vectors
    X = np.array([[1, 2], [3, 4], [5, 6]])
    Y = np.array([[7, 8], [9, 10], [11, 12]])

    # Compute L1 distances
    distances = compute_l1_distances(X, Y)

    # Print the distances
    print(distances)
