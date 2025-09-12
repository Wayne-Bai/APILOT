from scipy.sparse import diags
import numpy as np

def construct_matrix(N, M, k):
    # Create a list of ones arrays for each diagonal up to the k-th diagonal
    diagonals = [np.ones(min(N, M - i)) for i in range(k + 1)]
    
    # Specify the offsets for each diagonal
    offsets = range(k + 1)
    
    # Create sparse matrix with specified diagonals and offsets
    A = diags(diagonals, offsets, shape=(N, M), format='array')
    
    return A

# Example usage
N = 5
M = 5
k = 1
matrix = construct_matrix(N, M, k)
print(matrix)
