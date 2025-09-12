import tensorflow as tf

# Define a 4D input tensor with shape [batch, height, width, channels]
input_tensor = tf.constant(
    [[[[1.0], [2.0], [3.0], [4.0]],
      [[5.0], [6.0], [7.0], [8.0]],
      [[9.0], [10.0], [11.0], [12.0]],
      [[13.0], [14.0], [15.0], [16.0]]]], dtype=tf.float32)

# Define a 4D filter/kernel tensor with shape [filter_height, filter_width, in_channels, out_channels]
filter_tensor = tf.constant(
    [[[[1.0]], [[2.0]]],
     [[[3.0]], [[4.0]]]], dtype=tf.float32)

# Carry out the 2-D convolution using tf.nn.conv2d
output_tensor = tf.nn.conv2d(
    input=input_tensor,
    filters=filter_tensor,
    strides=[1, 1, 1, 1],  # Strides for each dimension
    padding='VALID'        # 'VALID' means no padding.
)

print(output_tensor.numpy())
