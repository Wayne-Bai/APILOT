import tensorflow as tf

# Define the input sequence tensor
sequence = tf.constant([[1, 2, 3, 4], [5, 6, 7, 8]], dtype=tf.int32)

# Define the sequence length tensor
sequence_length = tf.constant([4, 2], dtype=tf.int32)

# Reverse the sequence length-slices
reversed_sequence = tf.raw_ops.ReverseSequence(
    seq=sequence,
    seq_lengths=sequence_length,
    seq_dim=1,
    batch_dim=0
)

# Print the reversed sequence tensor
print(reversed_sequence)
