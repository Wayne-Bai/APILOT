import tensorflow as tf

def reverse_variable_length_slices(tensor, seq_lengths, seq_axis, batch_axis):
    """
    Reverse variable length slices in a tensor.

    Args:
    tensor (tf.Tensor): The input tensor.
    seq_lengths (tf.Tensor): The lengths of the sequences in the tensor.
    seq_axis (int): The axis of the tensor that contains the sequences.
    batch_axis (int): The axis of the tensor that contains the batch size.

    Returns:
    tf.Tensor: The tensor with sequences reversed according to seq_lengths.
    """
    # Use tf.reverse_sequence to reverse each slice according to seq_lengths
    reversed_tensor = tf.reverse_sequence(
        tensor,
        seq_lengths=seq_lengths,
        seq_axis=seq_axis,
        batch_axis=batch_axis
    )
    return reversed_tensor

# Example usage:
# Create a 3D tensor (e.g., batch x time x features)
tensor = tf.constant([[[1, 2], [3, 4], [5, 6]], [[7, 8], [9, 10], [0, 0]]])
seq_lengths = tf.constant([3, 2])  # First batch has 3 items, second has 2 items

reversed_tensor = reverse_variable_length_slices(tensor, seq_lengths, seq_axis=1, batch_axis=0)
print(reversed_tensor)
