import tensorflow as tf

# Assuming 'input_tensor' is your input 2-D SparseTensor
input_tensor = tf.raw_ops.SparseTensor(
    indices=tf.constant([[0, 0], [1, 2]], dtype=tf.int64),
    values=tf.constant([1, 3], dtype=tf.int64),
    dense_shape=tf.constant([2, 3], dtype=tf.int64)
)

# Fill empty rows with a default value, let's say 0
filled_tensor = tf.raw_ops.sparse_fill_empty_rows(
    input_tensor,
    default_value=tf.constant(0, dtype=tf.int64)
)

print(filled_tensor)
