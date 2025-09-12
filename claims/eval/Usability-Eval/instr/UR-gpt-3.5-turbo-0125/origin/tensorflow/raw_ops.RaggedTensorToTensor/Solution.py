
import tensorflow as tf

# Define a ragged tensor
rt = tf.ragged.constant([[1, 2], [3, 4, 5], [6]])

# Create a dense tensor from the ragged tensor
dense_tensor = tf.raw_ops.TensorFromRagged(ragged_values=rt.values, ragged_row_splits=rt.row_splits)

print(dense_tensor)
