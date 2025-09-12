import tensorflow as tf

# Assuming input shape (N, H, W, C) and filter shape (FH, FW, C, F)
input_tensor = tf.placeholder(tf.qint32, shape=[None, None, None, None])
filter_tensor = tf.placeholder(tf.float32, shape=[None, None, None, None])

# Decode the input tensor from quantized format to float32
decoded_input_tensor = tf.cast(input_tensor, tf.float32)

# Perform the 2D convolution
output_tensor = tf.nn.conv2d(decoded_input_tensor, filter_tensor, strides=[1, 1, 1, 1], padding='SAME')

# The output tensor will be in float32 format
