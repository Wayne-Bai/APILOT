import tensorflow as tf

# Define input tensor (BatchSize, Height, Width, Channels)
input_tensor = tf.placeholder(tf.float32, shape=[None, 32, 32, 3])

# Define filter tensor (FilterHeight, FilterWidth, InputChannels, OutputChannels)
filter_tensor = tf.Variable(tf.random.normal([5, 5, 3, 32], dtype=tf.float32))

# Compute 2-D convolution
conv = tf.nn.conv2d(input_tensor, filter_tensor, strides=[1, 1, 1, 1], padding='SAME')
