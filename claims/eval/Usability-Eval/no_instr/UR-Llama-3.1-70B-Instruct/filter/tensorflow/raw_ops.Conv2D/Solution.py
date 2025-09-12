import tensorflow as tf

# Define the input tensor (4-D) with shape (batch_size, height, width, channels)
input_tensor = tf.random.normal((1, 10, 10, 1))

# Define the filter tensor (4-D) with shape (filter_height, filter_width, channels, num_filters)
filter_tensor = tf.random.normal((3, 3, 1, 1))

# Use tf.raw_ops.Conv2D to compute the 2D convolution
conv_output = tf.raw_ops.Conv2D(
    input=input_tensor,
    filter=filter_tensor,
    strides=[1, 1, 1, 1],
    padding="SAME",
    data_format="NHWC",
)

# Alternative using tf.nn.conv2d (higher level API)
conv_output_alt = tf.nn.conv2d(
    input=input_tensor,
    filters=filter_tensor,
    strides=[1, 1, 1, 1],
    padding="SAME",
    data_format="NHWC",
)

# Print the output shapes
print("Conv2D output shape:", conv_output.shape)
print("Conv2D alt output shape:", conv_output_alt.shape)
