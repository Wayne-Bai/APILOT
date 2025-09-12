
import numpy as np

def soft_boundary_detection(X):
    # Calculate pairwise distance between samples
    pairwise_distance = np.linalg.norm(X[:, None] - X, axis=2)
    
    # Calculate median distance as the soft boundary
    soft_boundary = np.median(pairwise_distance)
    
    return soft_boundary

# Example usage
X = np.array([[0, 0], [1, 1], [2, 2], [3, 3]])
soft_boundary = soft_boundary_detection(X)
print("Soft Boundary:", soft_boundary)
