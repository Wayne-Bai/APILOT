
import tensorflow as tf

# Example input ragged tensor
ragged_tensor = tf.ragged.constant([[1, 2, 3], [4], [5, 6]])

# Define the dense tensor using tf.raw_ops.RaggedTensorToTensor
dense_tensor = tf.raw_ops.RaggedTensorToTensor(
    ragged_tensor=ragged_tensor,
    default_value=0,
    dtype=tf.int32,
    row_splits_dtype=tf.int64
)

# Print the dense tensor
print(dense_tensor)
