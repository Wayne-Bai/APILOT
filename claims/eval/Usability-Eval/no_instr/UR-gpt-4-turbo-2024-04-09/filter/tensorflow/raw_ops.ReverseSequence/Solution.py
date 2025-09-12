import tensorflow as tf

def reverse_variable_length_slices(tensor, seq_lengths, seq_axis):
    # Create a tensor of indices to map each element of the input tensor to its reversed position
    # with respect to the last axis.
    batch_size = tf.shape(tensor)[0]
    max_seq_length = tf.shape(tensor)[seq_axis]

    # Generates masks for each sequence
    masks = tf.sequence_mask(seq_lengths, maxlen=max_seq_length)

    # Creates range tensor and reverses it based on the masks
    reversed_sequences = tf.map_fn(
        lambda x: tf.reverse_sequence(x[0], seq_lengths=x[1], seq_dim=seq_axis, batch_dim=0), 
        (tensor, seq_lengths), 
        dtype=tensor.dtype
    )

    return reversed_sequences

# Example usage:
# Define a tensor and sequence lengths
input_tensor = tf.constant([[1, 2, 3, 0, 0], [4, 5, 0, 0, 0], [6, 7, 8, 9, 10]])
sequence_lengths = tf.constant([3, 2, 5])

# Reverse the variable-length slices
reversed_tensor = reverse_variable_length_slices(input_tensor, sequence_lengths, seq_axis=1)
print(reversed_tensor)
