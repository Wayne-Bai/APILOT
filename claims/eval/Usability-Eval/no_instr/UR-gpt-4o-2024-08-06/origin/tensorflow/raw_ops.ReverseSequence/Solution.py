import tensorflow as tf

# Define a tensor with variable length slices
inputs = tf.constant([
    [1, 2, 3, 0],
    [4, 5, 0, 0],
    [6, 0, 0, 0]
], dtype=tf.int32)

# Define the lengths for each slice (non-zero values count)
seq_lengths = tf.constant([3, 2, 1], dtype=tf.int32)

# Reverse the slices using the latest tensorflow function
reversed_slices = tf.reverse_sequence(inputs, seq_lengths, seq_axis=1, batch_axis=0)

# To view the result
print(reversed_slices.numpy())
