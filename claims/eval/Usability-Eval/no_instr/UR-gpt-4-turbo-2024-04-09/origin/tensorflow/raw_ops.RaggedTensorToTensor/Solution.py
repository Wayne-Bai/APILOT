import tensorflow as tf

# Create a RaggedTensor
ragged_tensor = tf.ragged.constant([[1, 2], [3], [], [4, 5, 6]])

# Convert RaggedTensor to a dense tensor
dense_tensor = tf.raw_ops.RaggedTensorToTensor(
    shape=tf.constant([-1, -1], dtype=tf.int64),
    values=ragged_tensor.values,
    row_splits=ragged_tensor.row_splits,
    default_value=tf.constant(0)
)

print(dense_tensor)
