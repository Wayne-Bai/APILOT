import tensorflow as tf

# Create a 4-D input tensor
input = tf.random.normal([1, 2, 3, 3])

# Create a 4-D filter tensor
filter = tf.random.normal([2, 2, 3, 2])

# Compute the 2-D convolution
output = tf.nn.conv2d(input, filter, strides=[1, 1, 1, 1], padding='SAME')

# Print the output tensor
print(output)
