import tensorflow as tf

def reverse_slices(input_tensor, seq_lengths, batch_axis=0, seq_axis=1):
    """
    Reverses slices of the input tensor along the specified sequence axis according to the provided sequence lengths.
    
    Parameters:
    - input_tensor: The input tensor to reverse.
    - seq_lengths: A 1-D tensor containing the sequence lengths for each batch item.
    - batch_axis: Axis along which the batch dimension is represented.
    - seq_axis: Axis along which sequences are arranged and need to be reversed.
    
    Returns:
    A tensor with the same shape as input_tensor, but with each slice reversed according to seq_lengths.
    """

    if not isinstance(input_tensor, tf.Tensor):
        input_tensor = tf.convert_to_tensor(input_tensor)

    if not isinstance(seq_lengths, tf.Tensor):
        seq_lengths = tf.convert_to_tensor(seq_lengths, dtype=tf.int32)

    # Transpose the input_tensor to make the seq_axis the last dimension
    perm = list(range(tf.rank(input_tensor)))
    perm[seq_axis], perm[-1] = perm[-1], perm[seq_axis]
    transposed_input = tf.transpose(input_tensor, perm)

    # Reverse each batch item according to seq_lengths
    reversed_transposed = tf.reverse_sequence(transposed_input, seq_lengths, seq_axis=-1, batch_axis=batch_axis)

    # Reverse the transposition to restore the original order of axes
    reversed_output = tf.transpose(reversed_transposed, perm)
    
    return reversed_output

# Example Usage
input_tensor = tf.constant([
    [[1, 2, 3, 4],    # Batch 0
     [5, 6, 7, 8],
     [9, 10, 11, 12]],
    
    [[13, 14, 15, 16], # Batch 1
     [17, 18, 19, 20],
     [21, 22, 23, 24]]
])

seq_lengths = tf.constant([2, 3])
output = reverse_slices(input_tensor, seq_lengths)

print(output.numpy())
