import tensorflow as tf

# Define the input tensor
input_tensor = tf.constant([[1.0, 2.0], [3.0, 4.0]], dtype=tf.float32)

# Reshape the input tensor to 4D to match the requirements of tf.nn.conv2d
input_tensor = tf.reshape(input_tensor, [1, 2, 2, 1])

# Define the filter tensor
filter_tensor = tf.constant([[0.0, -1.0], [1.0, 0.0]], dtype=tf.float32)

# Reshape the filter tensor to 4D
filter_tensor = tf.reshape(filter_tensor, [2, 2, 1, 1])

# Define the convolution operation
convolution = tf.nn.conv2d(input_tensor, filter_tensor, strides=[1, 1, 1, 1], padding='VALID')

# Compute the gradients of the convolution operation with respect to the filter tensor
with tf.GradientTape() as tape:
    tape.watch(filter_tensor)
    output = convolution
gradients = tape.gradient(output, filter_tensor)

# Print the gradients
print(gradients)
