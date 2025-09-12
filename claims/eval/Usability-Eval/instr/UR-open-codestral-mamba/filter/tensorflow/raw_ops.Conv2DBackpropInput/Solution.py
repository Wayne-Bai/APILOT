import tensorflow as tf

# Define the input tensor and filter tensor
input_tensor = tf.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=tf.float32)
filter_tensor = tf.constant([[1, 0, -1], [1, 0, -1], [1, 0, -1]], dtype=tf.float32)

# Reshape the input tensor to add a batch dimension
input_tensor = tf.expand_dims(input_tensor, 0)

# Add a dimension to the filter tensor to represent the batch
filter_tensor = tf.expand_dims(filter_tensor, 0)

# Perform the convolution operation
conv_output = tf.nn.conv2d(input_tensor, filter_tensor, strides=[1, 1, 1, 1], padding='SAME')

# Compute gradients of convolution with respect to the input
with tf.GradientTape() as g:
    g.watch(input_tensor)
    output = conv_output
gradients = g.gradient(output, input_tensor)

# Print the gradients
print(gradients)
