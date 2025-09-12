import tensorflow as tf

# Example input data
input_data = tf.random.normal([1, 2, 2, 1])
filter_data = tf.random.normal([1, 1, 1, 1])

# Compute gradients of convolution with respect to the input
grad_input = tf.raw_ops.Conv2DBackpropInput(input_sizes=[1, 2, 2, 1], filter=filter_data, out_backprop=input_data)

print(grad_input)
