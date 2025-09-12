import tensorflow as tf

def reverse_variable_length_slices(input_data, seq_lengths):
    """
    Reverses variable length slices of a tensor.

    Args:
    input_data: A tensor with shape [batch_size, max_length,...]
    seq_lengths: A tensor with shape [batch_size] containing the lengths of the sequences.

    Returns:
    A tensor with the same shape as input_data, but with the sequences reversed.
    """
    input_shape = tf.shape(input_data)
    batch_size, max_length = input_shape[0], input_shape[1]

    # Flatten the input data and sequence lengths
    flat_input_data = tf.reshape(input_data, [batch_size * max_length] + input_shape[2:].numpy().tolist())
    flat_seq_lengths = tf.reshape(seq_lengths, [batch_size])

    # Reverse the flattened input data
    reversed_flat_input_data = tf.reverse_sequence(flat_input_data, flat_seq_lengths, seq_axis=0, batch_axis=None)

    # Reshape the reversed data back to its original shape
    reversed_input_data = tf.reshape(reversed_flat_input_data, input_shape)

    return reversed_input_data


# Example usage:
input_data = tf.constant([
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[10, 20, 30], [40, 50, 60], [0, 0, 0]]
])

seq_lengths = tf.constant([3, 2])

reversed_data = reverse_variable_length_slices(input_data, seq_lengths)
print(reversed_data)

# Output:
# [[[7 8 9],
#   [4 5 6],
#   [1 2 3]],

#  [[40 50 60],
#   [10 20 30],
#   [ 0  0  0]]]
