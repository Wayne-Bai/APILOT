import tensorflow as tf

# Define the input and filter tensors
input_tensor = tf.random.normal([1, 256, 256, 3])
filter_tensor = tf.random.normal([3, 3, 3, 64])

# Define the strides and padding
strides = [1, 2, 2, 1]
padding = 'SAME'

# Compute the convolution
conv = tf.raw_ops.Conv2D(
    input=input_tensor,
    filter=filter_tensor,
    strides=strides,
    padding=padding,
)

# Print the result
print(conv)
