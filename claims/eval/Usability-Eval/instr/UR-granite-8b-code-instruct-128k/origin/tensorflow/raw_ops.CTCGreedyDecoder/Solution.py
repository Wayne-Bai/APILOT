import tensorflow as tf

# Assume inputs is a tensor of shape [batch_size, max_time, num_classes]
inputs = ...

decoded, _ = tf.raw_ops.CTCGreedyDecoder(
    inputs=inputs,
    sequence_length=tf.shape(inputs)[1],
    merge_repeated=False
)

decoded_sparse = tf.sparse.to_dense(decoded[0], default_value=-1)
decoded_dense = tf.sparse.to_dense(decoded[1], default_value=-1)

with tf.Session() as sess:
    decoded_sparse_out, decoded_dense_out = sess.run([decoded_sparse, decoded_dense])
