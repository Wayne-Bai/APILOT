import tensorflow as tf

# Define the input tensor
input = tf.random.normal([1, 2, 2, 1])

# Define the filter tensor
filter = tf.random.normal([1, 1, 1, 1])

# Compute the gradients of convolution with respect to the input
grad_input, grad_filter = tf.raw_ops.Conv2DBackpropInput(input=input, filter=filter, out_backprop=out_backprop)

# Print the gradients
print("Gradients of input:")
print(grad_input)
print("Gradients of filter:")
print(grad_filter)
