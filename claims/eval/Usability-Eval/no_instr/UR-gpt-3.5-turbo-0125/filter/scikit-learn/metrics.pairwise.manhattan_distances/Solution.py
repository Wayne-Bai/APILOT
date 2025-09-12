
import numpy as np

def l1_distance(X, Y):
    # Ensure X and Y are NumPy arrays
    X = np.array(X)
    Y = np.array(Y)

    # Compute L1 distances between vectors in X and Y
    distances = np.sum(np.abs(X[:, np.newaxis] - Y), axis=-1)

    return distances

# Example usage
X = np.array([[1, 2], [3, 4], [5, 6]])
Y = np.array([[2, 2], [4, 4]])
distances = l1_distance(X, Y)
print(distances)
