import tensorflow as tf

def levenshtein_distance(s1, s2):
    """
    Computes the Levenshtein distance between two strings s1 and s2.

    Args:
    s1: A Tensor of strings.
    s2: A Tensor of strings.

    Returns:
    A Tensor of shape `[batch_size]`, where each entry is the Levenshtein distance
    between the corresponding strings in `s1` and `s2`.
    """
    m = tf.shape(s1)[-1]
    n = tf.shape(s2)[-1]
    padded_s1 = tf.pad(s1, [[0, 0], [0, m]], mode='CONSTANT')
    padded_s2 = tf.pad(s2, [[0, 0], [0, n]], mode='CONSTANT')
    row = tf.range(0, m+1)
    matrix = tf.linalg.add(tf.expand_dims(row, 0), tf.transpose(tf.linalg.add(row, tf.range(0, n+1))))
    distance_matrix = tf.edit_distance(padded_s1, padded_s2) # Turn-key op
    result = distance_matrix[:,  [m, n]]
    return tf.reshape(result, [-1])

# Example usage:
s1 = tf.constant(["kitten"])
s2 = tf.constant(["sitting"])
print(levenshtein_distance(s1, s2))
