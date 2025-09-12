
import numpy as np

def zero_below_k_diagonal(matrix, k):
    result = np.array(matrix)
    rows, cols = result.shape

    for i in range(rows):
        for j in range(cols):
            if j - i > k:
                result[i][j] = 0
    
    return result

# Example usage
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
k = 1
modified_matrix = zero_below_k_diagonal(matrix, k)
print(modified_matrix)
