
import tensorflow as tf

# Create input tensor
input_tensor = tf.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]], dtype=tf.float32)
input_tensor = tf.expand_dims(tf.expand_dims(input_tensor, axis=0), axis=3)

# Create filter tensor
filter_tensor = tf.constant([[1, 0, -1], [1, 0, -1], [1, 0, -1]], dtype=tf.float32)
filter_tensor = tf.expand_dims(tf.expand_dims(filter_tensor, axis=2), axis=3)

# Conv2D operation using tf.raw_ops
output_tensor = tf.raw_ops.Conv2D(input=input_tensor, filter=filter_tensor, strides=[1, 1, 1, 1], padding="VALID")
print(output_tensor)
