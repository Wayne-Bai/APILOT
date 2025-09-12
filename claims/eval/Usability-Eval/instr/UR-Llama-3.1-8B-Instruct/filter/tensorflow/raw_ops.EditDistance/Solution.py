import tensorflow as tf

# Define a function to calculate the edit distance using dynamic programming
def edit_distance(s1, s2, normalize=False):
    # Create a matrix to store the edit distances
    matrix = tf.Variable(tf.zeros((len(s2) + 1, len(s1) + 1)))

    # Initialize the first row and column
    matrix[0, :] = tf.cast(tf.range(0, len(s1) + 1), dtype=tf.int32)
    matrix[:, 0] = tf.cast(tf.range(0, len(s2) + 1), dtype=tf.int32)

    # Fill in the rest of the matrix
    for i in tf.range(1, len(s2) + 1):
        for j in tf.range(1, len(s1) + 1):
            # Cost of substitution
            cost = 0 if s1[j - 1] == s2[i - 1] else 1

            matrix[i, j] = tf.math.minimum(
                tf.math.minimum(
                    matrix[i - 1, j - 1] + cost,
                    matrix[i - 1, j] + 1),
                matrix[i, j - 1] + 1)

    # If normalization is required, calculate the maximum number of operations
    if normalize:
        max_ops = tf.math.reduce_max(matrix)
        if max_ops > 0:
            return matrix / max_ops
        else:
            return matrix
    else:
        return matrix[-1, -1]

# Test the function
s1 = 'kitten'
s2 ='sitting'

dist = edit_distance(s1, s2)
print(f'Edit distance without normalization: {dist}')

dist = edit_distance(s1, s2, normalize=True)
print(f'Edit distance with normalization: {dist}')
