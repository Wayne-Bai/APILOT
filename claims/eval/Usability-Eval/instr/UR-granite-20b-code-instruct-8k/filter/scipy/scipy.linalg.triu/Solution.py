import scipy

def zero_out_below_diagonal(matrix, k):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if j < i - k:
                matrix[i][j] = 0
    return matrix

# Example usage:
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
k = 1
result = zero_out_below_diagonal(matrix, k)
print(result)
