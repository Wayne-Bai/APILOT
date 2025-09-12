import tensorflow as tf

# Define the sparse tensor input
sparse_input = tf.sparse.constant([[0, 0], [1, 2], [2, 3]], value_dtype=tf.int32)

# Perform sparse-output bin counting
output = tf.raw_ops.SparseBinCount(sparse_input=sparse_input, weights=None, minlength=0, maxlength=10, dtype=tf.int32)

print(output)
