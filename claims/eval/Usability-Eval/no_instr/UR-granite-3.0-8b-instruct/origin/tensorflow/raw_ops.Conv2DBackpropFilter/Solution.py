import tensorflow as tf

# Define the input tensor
input_tensor = tf.random.normal([1, 5, 5, 1])

# Define the filter tensor
filter_tensor = tf.random.normal([3, 3, 1, 1])

# Compute the convolution
convolution = tf.nn.conv2d(input_tensor, filter_tensor, strides=[1, 1, 1, 1], padding='SAME')

# Compute the gradients of the convolution with respect to the filter
gradients = tf.gradients(convolution, filter_tensor)[0]

print(gradients)
