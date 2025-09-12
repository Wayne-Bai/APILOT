from sklearn.metrics.pairwise import manhattan_distances
import numpy as np

def compute_l1_distances(X, Y):
    X = np.array(X)
    Y = np.array(Y)
    distances = manhattan_distances(X, Y)
    return distances

# Example usage
X = [[1, 2, 3], [4, 5, 6]]
Y = [[7, 8, 9], [10, 11, 12]]
distances = compute_l1_distances(X, Y)
print(distances)
