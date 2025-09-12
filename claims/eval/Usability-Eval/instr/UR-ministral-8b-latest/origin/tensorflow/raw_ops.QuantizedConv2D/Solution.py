import tensorflow as tf

# Example input and filter tensors
# Assuming input should be quantized and in the shape (batch_size, height, width, channels)
input_quantized = tf.constant([[[[3, 4], [1, 2]], [[5, 6], [7, 8]]]], dtype=tf.int32)

# Assuming the filter should also be quantized and in the shape (filter_height, filter_width, in_channels, out_channels)
filter_quantized = tf.constant([[[[1, -1], [1, -1]], [[0, 0], [0, 0]]], [[[1, -1], [1, -1]], [[1, 0], [0, 1]]]], dtype=tf.int32)

# Performing the convolution with quantized inputs and filters using tf.raw_ops.
result_convolution_qu量 = tf.raw_ops.Conv2D(
    input=input_quantized,
    filters=filter_quantized,
    strides=[1, 1],
    padding='VALID',
    data_format='NHWC'
)

print(result_convolution_qu量.numpy())
