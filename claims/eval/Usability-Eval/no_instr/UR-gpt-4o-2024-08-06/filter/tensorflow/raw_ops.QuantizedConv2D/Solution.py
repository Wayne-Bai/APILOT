import tensorflow as tf

# Define the quantized 4D input tensor and filter tensor
input_tensor = tf.constant([[[[1], [2]], [[3], [4]]]], dtype=tf.qint8)
filter_tensor = tf.constant([[[[1]], [[1]]], [[[1]], [[1]]]], dtype=tf.qint8)

# Specify convolution parameters
strides = [1, 1, 1, 1]  # Stride specifications for each dimension
padding = 'VALID'       # Choose between 'VALID' or 'SAME'

# Compute the 2D convolution using the tf.nn.conv2d
conv_output = tf.nn.conv2d(
    input=tf.cast(input_tensor, tf.float32),
    filters=tf.cast(filter_tensor, tf.float32),
    strides=strides,
    padding=padding
)

# Print the output
print(conv_output.numpy())
