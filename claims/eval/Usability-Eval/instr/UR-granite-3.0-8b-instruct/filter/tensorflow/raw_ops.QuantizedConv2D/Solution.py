import tensorflow as tf

# Assuming input and filter are quantized 4D tensors
# input shape: (batch, height, width, channels)
# filter shape: (height_filter, width_filter, in_channels, out_channels)

# Perform 2D convolution
output = tf.nn.conv2d(input, filter, strides=[1, 1, 1, 1], padding='SAME')

# Quantize the output if needed
output = tf.quantization.quantize_v2(output)
