
import numpy as np

def zero_above_kth_diagonal(matrix, k):
    m_shape = matrix.shape
    result = np.copy(matrix)
    
    for i in range(m_shape[0]):
        for j in range(m_shape[1]):
            if i - j > k:
                result[i, j] = 0
                
    return result

# Test the function
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
k = 1
result_matrix = zero_above_kth_diagonal(matrix, k)
print(result_matrix)
