import tensorflow as tf

# Create a Constant for the filter, input, and strides tensors
filter = tf.constant([
    [1, 0, 1],
    [1, 0, -1],
    [1, 0, -1]
])

input_tensor = tf.constant([
    [1, 2, 3],
    [2, 1, 4]
])

strides = [1, 1, 1, 1]

# Create an empty tensor to hold the output
output = tf.raw_ops.Method(
    None,         # do not input input tensor
    None,         # do not input filter tensor
    strides=strides
)

# Output the tensor containing the convolution result
print(output)
