import tensorflow as tf

def levenshtein_distance(x, y):
    # Convert the strings to tensors
    x = tf.convert_to_tensor(x, dtype=tf.string)
    y = tf.convert_to_tensor(y, dtype=tf.string)

    # Get the length of both strings
    len_x = tf.shape(x)[0]
    len_y = tf.shape(y)[0]

    # Initialize a matrix of shape (len_x + 1, len_y + 1) with zeros
    distance_matrix = tf.zeros((len_x + 1, len_y + 1), dtype=tf.int32)

    # Fill the first row and column with the range values
    distance_matrix = tf.tensor_scatter_nd_update(distance_matrix, tf.expand_dims(tf.range(len_x + 1), 1), tf.range(len_x + 1))
    distance_matrix = tf.tensor_scatter_nd_update(distance_matrix, tf.expand_dims(tf.range(len_y + 1), 0), tf.range(len_y + 1))

    # Compute the Levenshtein distance
    for i in tf.range(1, len_x + 1):
        for j in tf.range(1, len_y + 1):
            deletion = distance_matrix[i-1, j] + 1
            insertion = distance_matrix[i, j-1] + 1
            substitution = distance_matrix[i-1, j-1] + tf.cast(tf.not_equal(x[i-1], y[j-1]), dtype=tf.int32)
            distance_matrix = tf.tensor_scatter_nd_update(distance_matrix, [[i, j]], tf.minimum(deletion, tf.minimum(insertion, substitution)))

    return distance_matrix[len_x, len_y]

# Test the function
distance = levenshtein_distance('kitten', 'sitting')
tf.print(distance)
