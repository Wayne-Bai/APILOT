import tensorflow as tf

def compute_edit_distance(A: tf.Tensor, B: tf.Tensor, normalized: bool = False):

    m, n = tf.shape(A)[0], tf.shape(B)[0]

    # Initialize a 2D matrix filled with zeros
    matrix = tf.zeros((m+1, n+1), dtype=tf.int32)

    # Fill the first row and column with incrementing values
    for i in range(1, m+1):
        matrix[i][0] = i

    for j in range(1, n+1):
        matrix[0][j] = j

    # Compute the Levenshtein distance and fill the rest of the matrix
    for i in range(1, m+1):
        for j in range(1, n+1):
            if A[i-1] == B[j-1]:
                cost = 0
            else:
                cost = 1

            matrix[i][j] = tf.minimum(tf.minimum(matrix[i-1][j] + 1, matrix[i][j-1] + 1), matrix[i-1][j-1] + cost)

    # Normalize the edit distance
    if normalized:
        matrix = tf.divide(matrix, tf.maximum(m, n))

    return matrix

A = tf.constant(['math', 'magic'])
B = tf.constant(['magic', 'mit'])

print(compute_edit_distance(A, B))
