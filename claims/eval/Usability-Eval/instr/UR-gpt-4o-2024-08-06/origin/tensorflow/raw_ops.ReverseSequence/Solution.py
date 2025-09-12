import tensorflow as tf

def reverse_sequence(input_tensor, seq_lengths, seq_axis, batch_axis):
    """
    Reverses variable length slices within a batch.

    :param input_tensor: Tensor with shape [batch_size, max_time, ...].
    :param seq_lengths: 1-D tensor with length batch_size, containing
                        the actual lengths for each sequence in the batch.
    :param seq_axis: Axis over which to apply the reversals.
    :param batch_axis: Axis of the batch.

    :return: A tensor with the same shape as input_tensor with the specified sequences reversed.
    """
    # Using tf.reverse_sequence to reverse slices
    reversed_tensor = tf.reverse_sequence(
        input_tensor,
        seq_lengths=seq_lengths,
        seq_axis=seq_axis,
        batch_axis=batch_axis
    )

    return reversed_tensor

# Example usage
# Create a sample input tensor
input_data = tf.constant([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
], dtype=tf.int32)

# Define sequence lengths for each sequence in the batch
sequence_lengths = tf.constant([3, 4, 2], dtype=tf.int32)

# Reverse the sequences
output = reverse_sequence(input_data, sequence_lengths, seq_axis=1, batch_axis=0)

# Print the resulting tensor
tf.print(output)
