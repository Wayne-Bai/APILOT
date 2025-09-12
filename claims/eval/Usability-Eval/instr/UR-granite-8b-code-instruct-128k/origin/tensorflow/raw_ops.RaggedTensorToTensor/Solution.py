
import tensorflow as tf

# Create a ragged tensor
ragged_tensor = tf.ragged.constant([[1, 2, 3], [4], [5, 6]])

# Convert the ragged tensor to a dense tensor
dense_tensor = tf.raw_ops.RaggedTensorToTensor(
    ragged_tensor=ragged_tensor,
    default_value=0,
    dtype=tf.int32
)

# Print the dense tensor
print(dense_tensor)
