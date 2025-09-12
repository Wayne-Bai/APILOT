import tensorflow as tf

# Sample data
input_tensor = tf.constant([[1, 2, 3, 4, 5],
                            [6, 7, 8, 9, 10],
                            [11, 12, 13, 14, 15]], dtype=tf.int32)

# Sequence lengths (for each batch)
seq_lengths = tf.constant([3, 4, 5], dtype=tf.int32)

# Reverse variable length slices
reversed_slices = tf.reverse_sequence(input_tensor, seq_lengths, seq_axis=1, batch_axis=0)

# Execute the tensor
result = reversed_slices.numpy()

print(result)
