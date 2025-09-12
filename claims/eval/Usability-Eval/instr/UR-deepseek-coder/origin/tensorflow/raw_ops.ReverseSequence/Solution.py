import tensorflow as tf

def reverse_variable_length_slices(input_tensor, seq_lengths):
    # Create a mask to identify valid elements in each sequence
    max_length = tf.reduce_max(seq_lengths)
    batch_size = tf.shape(input_tensor)[0]
    mask = tf.sequence_mask(seq_lengths, maxlen=max_length, dtype=tf.bool)
    
    # Reverse the valid elements in each sequence
    reversed_tensor = tf.reverse_sequence(input_tensor, seq_lengths, seq_dim=1, batch_dim=0)
    
    # Apply the mask to keep only the valid reversed elements
    reversed_tensor = tf.where(mask, reversed_tensor, input_tensor)
    
    return reversed_tensor

# Example usage:
# input_tensor: [batch_size, max_sequence_length, ...]
# seq_lengths: [batch_size]
input_tensor = tf.constant([[1, 2, 3, 4], [5, 6, 7, 0], [8, 9, 0, 0]])
seq_lengths = tf.constant([4, 3, 2])

reversed_slices = reverse_variable_length_slices(input_tensor, seq_lengths)
print(reversed_slices.numpy())
