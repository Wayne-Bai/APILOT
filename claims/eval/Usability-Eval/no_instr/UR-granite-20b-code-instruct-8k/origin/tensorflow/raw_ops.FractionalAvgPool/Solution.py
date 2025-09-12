import tensorflow as tf

# Define the input tensor and its shape
input_tensor = tf.placeholder(tf.float32, shape=[None, None, None, 3])
input_shape = tf.shape(input_tensor)

# Define the pooling size
pooling_size = [8, 8]

# Define the strides
strides = [1, 8, 8, 1]

# Define the size of the output
output_size = [input_shape[1] // pooling_size[0], input_shape[2] // pooling_size[1]]

# Perform fractional average pooling
output_tensor = tf.nn.avg_pool(input_tensor, ksize=pooling_size, strides=strides, padding='VALID')
