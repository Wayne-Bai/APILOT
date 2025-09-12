import numpy as np

def create_matrix(N, M, k):
    # Create an empty matrix of shape (N, M)
    matrix = np.zeros((N, M))

    # Fill the matrix with ones where the condition j <= i + k is satisfied
    for i in range(N):
        for j in range(M):
            if j <= i + k:
                matrix[i, j] = 1

    return matrix

# Example usage
N = 5
M = 6
k = 2
matrix = create_matrix(N, M, k)
print(matrix)
