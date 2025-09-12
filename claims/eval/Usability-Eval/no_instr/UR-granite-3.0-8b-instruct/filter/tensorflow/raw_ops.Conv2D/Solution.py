import tensorflow as tf

# Define the input tensor
input_tensor = tf.random.normal([1, 5, 5, 1])

# Define the filter tensor
filter_tensor = tf.random.normal([3, 3, 1, 1])

# Perform 2D convolution
convolved_tensor = tf.nn.conv2d(input_tensor, filter_tensor, strides=[1, 1, 1, 1], padding='SAME')

# Print the convolved tensor
print(convolved_tensor)
