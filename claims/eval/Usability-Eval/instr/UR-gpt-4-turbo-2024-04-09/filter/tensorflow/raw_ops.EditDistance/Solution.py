import tensorflow as tf

def levenshtein_distance(hypothesis, truth):
    """
    Calculating Levenshtein distance using a matrix.
    """
    # Create a matrix of size (len(hypothesis)+1)x(len(truth)+1)
    # for storing the edit distances.
    h_len, t_len = len(hypothesis) + 1, len(truth) + 1
    matrix = tf.Variable(tf.ones((h_len, t_len), dtype=tf.int32))
    tf.raw_ops.MatrixSetDiag(
        input=matrix,
        diagonal=tf.range(h_len),
        name="Initialize_hypothesis"
    )
    tf.raw_ops.MatrixSetDiag(
        input=tf.transpose(matrix),
        diagonal=tf.range(t_len),
        name="Initialize_truth"
    )

    # Populate the matrix with the edit distances
    for i in range(1, h_len):
        for j in range(1, t_len):
            if hypothesis[i-1] == truth[j-1]:
                cost = 0
            else:
                cost = 1
            # Set each cell to the minimum of (cell to the left+1,
            # cell above+1, diagonally left cell above+cost of substitution)
            matrix[i, j].assign(
                tf.minimum(tf.minimum(
                    matrix[i-1, j] + 1,  # deletion
                    matrix[i, j-1] + 1),  # insertion
                    matrix[i-1, j-1] + cost)  # substitution
            )

    return matrix[h_len-1, t_len-1]

# Example usage
hypothesis = "tensor"
truth = "tenser"

distance = levenshtein_distance(hypothesis, truth)
print("Levenshtein distance is:", distance.numpy())
