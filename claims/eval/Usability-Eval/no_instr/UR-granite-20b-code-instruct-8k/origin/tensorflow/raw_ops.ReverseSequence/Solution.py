import tensorflow as tf

def reverse_variable_length_slices(input_tensor, sequence_lengths):
    """
    Reverses variable length slices.

    Args:
    input_tensor: A tensor of shape [batch_size, max_sequence_length, ...].
    sequence_lengths: A tensor of shape [batch_size] containing the length of each sequence.

    Returns:
    A tensor of the same shape as input_tensor but with slices reversed along the second axis.

    Example:
    input_tensor = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    sequence_lengths = [3, 2, 3]
    output = [[3, 2, 1], [6, 5, 4], [9, 8, 7]]
    """
    with tf.name_scope("reverse_variable_length_slices"):
        reversed_tensor = tf.reverse_sequence(input_tensor, sequence_lengths, 1)
        return reversed_tensor

# Example usage
input_tensor = tf.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
sequence_lengths = tf.constant([3, 2, 3])
reversed_tensor = reverse_variable_length_slices(input_tensor, sequence_lengths)

with tf.Session() as sess:
    print(sess.run(reversed_tensor))
