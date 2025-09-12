
import tensorflow as tf

# Define the ragged tensor
row_splits = tf.constant([0, 2, 3, 4], tf.int64)
values = tf.constant([1, 2, 3, 4], tf.int32)
data = tf.RaggedTensor.from_row_splits(values, row_splits)

# Create a dense tensor from the ragged tensor
dense_tensor = tf.raw_ops.DenseToRagged(data=data)

print(dense_tensor)
