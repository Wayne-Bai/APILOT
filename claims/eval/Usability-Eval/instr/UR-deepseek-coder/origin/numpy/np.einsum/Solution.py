import numpy as np

def einstein_sum(operands, indices):
    # Parse the indices and operands
    index_dict = {}
    for i, idx in enumerate(indices):
        if idx not in index_dict:
            index_dict[idx] = []
        index_dict[idx].append(i)
    
    # Determine the shape of the result
    result_shape = tuple(max(len(operands[i].shape) for i in index_dict[idx]) for idx in index_dict)
    
    # Initialize the result array
    result = np.zeros(result_shape)
    
    # Perform the summation
    for idx in np.ndindex(result_shape):
        sum_value = 0
        for operand in operands:
            sum_value += operand[tuple(idx[index_dict[i][0]] for i in range(len(index_dict)))]
        result[idx] = sum_value
    
    return result

# Example usage:
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
C = np.array([[9, 10], [11, 12]])

# Einstein summation: A_ij * B_jk * C_ki
result = einstein_sum([A, B, C], 'ijk')
print(result)
