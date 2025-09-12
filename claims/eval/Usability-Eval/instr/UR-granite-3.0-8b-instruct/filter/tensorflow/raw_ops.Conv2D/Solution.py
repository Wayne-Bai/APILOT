import tensorflow as tf

# Assuming input and filter tensors are already defined
# input_tensor has shape (batch_size, height, width, channels)
# filter_tensor has shape (height_filter, width_filter, in_channels, out_channels)

# Perform 2D convolution
output_tensor = tf.raw_ops.Conv2DNative(
    input_tensor,
    filter_tensor,
    strides=[1, 1, 1, 1],
    padding='SAME'
)
