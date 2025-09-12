
import tensorflow as tf

# Create a scalar value to fill the tensor with
scalar_value = 5

# Create a tensor filled with the scalar value
tensor = tf.constant(scalar_value, shape=[3, 3], dtype=tf.float32)
