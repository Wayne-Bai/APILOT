import tensorflow as tf
# Create a tensor of shape [2, 3, 5]
input_tensor = tf.random.normal([2, 3, 5])
# Create a tensor of shape [2] containing the sequence lengths
seq_lengths = tf.constant([1, 2], dtype=tf.int32)
# Create a tensor of shape [2, 1] containing the sequence axis
seq_axis = tf.constant([0], dtype=tf.int32)
# Reverse the variable length slices
output_tensor = tf.raw_ops.ReverseSequence(
    input=input_tensor,
    seq_lengths=seq_lengths,
    seq_axis=seq_axis,
)
