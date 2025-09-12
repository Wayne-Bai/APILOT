
import tensorflow as tf

# Define input tensor
input_tensor = tf.constant([[[[1.0], [2.0], [3.0]],
                             [[4.0], [5.0], [6.0]],
                             [[7.0], [8.0], [9.0]]]], dtype=tf.float32)

# Define filter tensor
filter_tensor = tf.constant([[[[1.0]], [[1.0]]],
                             [[[1.0]], [[1.0]]]], dtype=tf.float32)

# Perform 2D convolution
output = tf.nn.conv2d(input_tensor, filter_tensor, strides=[1, 1, 1, 1], padding='VALID')

# Print the output
print(output)
