
import tensorflow as tf

# Create a ragged tensor with shape (2, None) and values [1, 2], [3, 4]
ragged_tensor = tf.ragged.constant([[1, 2], [3, 4]], dtype=tf.int64)

# Convert the ragged tensor to a dense tensor with shape (2, 2)
dense_tensor = tf.raw_ops.ragged_tensor_to_tensor(ragged_tensor, padding=-1)

print("Dense tensor:", dense_tensor)
