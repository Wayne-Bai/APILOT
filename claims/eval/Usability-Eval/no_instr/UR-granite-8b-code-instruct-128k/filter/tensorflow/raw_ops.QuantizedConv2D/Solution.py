import tensorflow as tf

# Define the input and filter tensors
input_tensor = tf.quantized_placeholder(tf.qint8, shape=[None, 28, 28, 1])
filter_tensor = tf.quantized_placeholder(tf.qint8, shape=[5, 5, 1, 32])

# Define the convolution operation
conv_tensor = tf.raw_ops.QuantizedConv2D(
    input=input_tensor,
    filter=filter_tensor,
    min_input=0.0,
    max_input=0.0,
    min_filter=0.0,
    max_filter=0.0,
    strides=[1, 1, 1, 1],
    padding="SAME",
    dilations=[1, 1, 1, 1],
    name="conv"
)

# Get the output tensor and its min/max values
output_tensor = conv_tensor[0]
min_output = conv_tensor[1]
max_output = conv_tensor[2]
