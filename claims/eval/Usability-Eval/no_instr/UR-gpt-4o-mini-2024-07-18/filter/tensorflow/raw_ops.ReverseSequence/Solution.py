import tensorflow as tf

# Define the function to reverse variable length slices
def reverse_variable_length_slices(input_tensor, start_indices, lengths):
    # Using tf.raw_ops.ReverseSequence as a replacement
    return tf.raw_ops.ReverseSequence(input=input_tensor, seq_dim=0, batch_dim=0, seq_lengths=lengths)

# Example usage
input_tensor = tf.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
start_indices = tf.constant([0, 2])  # Not used in this context
lengths = tf.constant([3, 1])  # Lengths of sequences to reverse

reversed_tensor = reverse_variable_length_slices(input_tensor, start_indices, lengths)
print(reversed_tensor.numpy())
