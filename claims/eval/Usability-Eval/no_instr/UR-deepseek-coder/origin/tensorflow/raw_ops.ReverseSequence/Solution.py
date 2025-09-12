import tensorflow as tf

def reverse_variable_length_slices(input_tensor, seq_lengths):
    # Ensure seq_lengths is a 1D tensor
    seq_lengths = tf.cast(seq_lengths, tf.int32)
    
    # Create a mask to identify valid elements in each sequence
    max_length = tf.shape(input_tensor)[1]
    batch_size = tf.shape(input_tensor)[0]
    range_tensor = tf.range(max_length)
    mask = tf.less(range_tensor, tf.expand_dims(seq_lengths, 1))
    
    # Reverse the valid elements in each sequence
    reversed_tensor = tf.reverse_sequence(input_tensor, seq_lengths, seq_axis=1, batch_axis=0)
    
    # Apply the mask to keep only the valid reversed elements
    result = tf.where(mask, reversed_tensor, input_tensor)
    
    return result

# Example usage:
# input_tensor: [batch_size, max_sequence_length, ...]
# seq_lengths: [batch_size]
input_tensor = tf.constant([[1, 2, 3, 4], [5, 6, 7, 0], [8, 9, 0, 0]])
seq_lengths = tf.constant([4, 3, 2])

reversed_slices = reverse_variable_length_slices(input_tensor, seq_lengths)
print(reversed_slices.numpy())
