import numpy as np
import scipy.sparse as sparse

def initialize_from_quaternions(q):
    w, x, y, z = q
    A = np.array([[w, x, y, -z], [-x, w, -z, y], [-y, z, w, -x], [-z, -y, x, w]])
    return A

# Example usage
quaternions = np.array([1, 2, 3, 4])
matrix = initialize_from_quaternions(quaternions)
print(matrix)
