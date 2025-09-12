
import numpy as np

def L1_distance(X, Y):
    return np.sum(np.abs(X - Y), axis=1)

# Example Usage
X = np.array([[1, 2, 3],
              [4, 5, 6]])
Y = np.array([[2, 3, 4],
              [5, 6, 7]])

distances = L1_distance(X, Y)
print(distances)
