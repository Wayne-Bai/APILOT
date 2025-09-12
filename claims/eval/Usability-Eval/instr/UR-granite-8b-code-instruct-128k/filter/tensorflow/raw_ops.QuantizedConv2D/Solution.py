
import tensorflow as tf

# Define the input and filter tensors
input_quantized = tf.constant([[[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]])
filter_quantized = tf.constant([[[[1, 0, -1], [0, 0, 0]], [[-1, 0, 1], [0, 0, 0]]]])

# Define the convolution operation
convolution = tf.raw_ops.QuantizedConv2D(
    input=input_quantized,
    filter=filter_quantized,
    min_input=0.0,
    max_input=12.0,
    min_filter=0.0,
    max_filter=1.0,
    strides=[1, 1, 1, 1],
    padding="SAME",
    dilations=[1, 1, 1, 1],
    data_format="NHWC",
    leakyrelu_alpha=0.2,
    name="convolution"
)

# Print the result
print(convolution)
