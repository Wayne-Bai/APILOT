import scipy.linalg

def pseudo_inverse_hermitian(matrix):
    return scipy.linalg.pinvh(matrix)

# Example usage:
matrix = [[1, 2], [2, 3]]  # Replace this with your Hermitian matrix
pseudo_inv = pseudo_inverse_hermitian(matrix)
print("Pseudo-inverse: ", pseudo_inv)
