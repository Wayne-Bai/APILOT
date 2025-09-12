
import tensorflow as tf

# Assume params and indices are defined ragged tensors
params = tf.ragged.constant([[1.0, 2.0], [3.0, 4.0, 5.0]])
indices = tf.constant([0, 1])

# Gather ragged slices using tf.gather
result = tf.RaggedTensor.from_row_splits(
    tf.gather(params.flat_values, indices),
    tf.cast(tf.cumsum(params.row_lengths()), tf.int64)
)
print(result)
