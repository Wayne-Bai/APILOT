import tensorflow as tf

# Dummy inputs
input_data = tf.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
seq_lengths = tf.constant([3, 2, 3])  # lengths of input sequences

# Reverse variable length slices
reversed_data = tf.raw_ops.ReverseSequence(
    input=input_data,
    seq_lengths=seq_lengths,
    seq_dim=1,
    batch_dim=0
)

# Print the result
with tf.Session() as sess:
    print(sess.run(reversed_data))
