import tensorflow as tf

# Define the quantized 4D input and filter tensors
input_tensor = tf.Variable(tf.random.normal([1, 10, 10, 3]))
filter_tensor = tf.Variable(tf.random.normal([3, 3, 3, 64]))

# Quantize the input and filter tensors
input_tensor_quantized = tf.quantization.quantize_with_min_max_stats(input_tensor, tf.float16)
filter_tensor_quantized = tf.quantization.quantize_with_min_max_stats(filter_tensor, tf.float16)

# Compute the 2D convolution
output_tensor = tf.raw_ops.Convolution2D(input=input_tensor_quantized, filter=filter_tensor_quantized, strides=[1, 1, 1, 1], padding='SAME')
