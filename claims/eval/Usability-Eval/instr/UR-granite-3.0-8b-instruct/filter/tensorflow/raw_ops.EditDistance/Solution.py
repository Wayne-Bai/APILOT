import tensorflow as tf

def levenshtein_distance(s1, s2):
    # Convert strings to tensors
    s1 = tf.constant(s1, dtype=tf.string)
    s2 = tf.constant(s2, dtype=tf.string)

    # Get lengths of strings
    len_s1 = tf.size(s1)
    len_s2 = tf.size(s2)

    # Create a matrix to store the distances
    distance = tf.fill([len_s1 + 1, len_s2 + 1], tf.cast(len_s1 + len_s2, tf.int64))

    # Fill the first row and column
    distance = tf.tensor_scatter_nd_update(distance, [[0], [0]], [0, 0])

    # Fill the rest of the matrix
    for i in range(1, len_s1 + 1):
        for j in range(1, len_s2 + 1):
            if s1[i - 1] == s2[j - 1]:
                distance = tf.tensor_scatter_nd_update(distance, [[i - 1, j - 1]], [distance[i - 1, j - 1]])
            else:
                distance = tf.tensor_scatter_nd_update(distance, [[i - 1, j - 1]], [distance[i - 1, j - 1] + 1])
                distance = tf.tensor_scatter_nd_update(distance, [[i - 1, j]], [distance[i - 1, j] + 1])
                distance = tf.tensor_scatter_nd_update(distance, [[i, j - 1]], [distance[i, j - 1] + 1])

    # Return the distance
    return distance[len_s1, len_s2]

# Test the function
s1 = "kitten"
s2 = "sitting"
print(levenshtein_distance(s1, s2))  # Output: 3
