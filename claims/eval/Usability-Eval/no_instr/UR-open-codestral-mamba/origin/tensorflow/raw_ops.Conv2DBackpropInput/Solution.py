
import tensorflow as tf

# Define the input tensor
x = tf.random.normal([1, 10, 10, 3], mean=0.0, stddev=1.0, dtype=tf.dtypes.float32)

# Define the filter tensor
filter = tf.random.normal([3, 3, 3, 1], mean=0.0, stddev=1.0, dtype=tf.dtypes.float32)

# Convert the filter tensor to require_grad
filter = tf.Variable(filter)

# Perform the convolution operation
y = tf.nn.conv2d(x, filter, strides=[1, 1, 1, 1], padding='SAME')

# Compute gradients of y with respect to x
gradients = tf.gradients(y, x)
