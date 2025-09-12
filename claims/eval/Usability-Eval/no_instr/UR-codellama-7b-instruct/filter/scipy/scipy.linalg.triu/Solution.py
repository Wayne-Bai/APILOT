
from scipy import linalg

def zero_below_diag(matrix, k):
    # Get the shape of the input matrix
    n = matrix.shape[0]
    m = matrix.shape[1]

    # Create a copy of the input matrix
    out = np.copy(matrix)

    # Loop over the rows and columns of the output matrix
    for i in range(n):
        for j in range(m):
            if abs(i - j) < k:
                out[i,j] = 0

    return out
