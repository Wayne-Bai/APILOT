import tensorflow as tf

def reverse_variable_length_slices(tensor, seq_lengths, seq_dim, batch_dim=0):
    # Calculate the full indices for each dimension
    shape = tf.shape(tensor)
    batch_size = shape[batch_dim]
    max_seq_length = shape[seq_dim]

    # Create a range tensor that would act as a sequence index
    seq_indices = tf.range(max_seq_length)

    # Create a mask where sequences should be reversed
    mask = seq_indices < tf.expand_dims(seq_lengths, 1)

    # Perform the reversing operation
    tensor_reversed = tf.where(mask, 
                               tf.gather(tensor, seq_indices[::-1], axis=seq_dim),
                               tf.gather(tensor, seq_indices, axis=seq_dim))

    return tensor_reversed

# Example usage
# Create a 3D tensor: (batch_size, seq_length, features)
tensor = tf.constant([[[1, 2], [3, 4], [5, 6], [0, 0]],
                      [[7, 8], [9, 10], [0, 0], [0, 0]]])
seq_lengths = tf.constant([3, 2])  # sequences lengths for each batch

# Reverse the variable length slices
reversed_tensor = reverse_variable_length_slices(tensor, seq_lengths, seq_dim=1)
print(reversed_tensor)
