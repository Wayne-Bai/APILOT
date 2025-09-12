import tensorflow as tf

# Define the input and filter tensors
input_tensor = tf.random.uniform(shape=(1, 10, 10, 1), minval=0, maxval=1, dtype=tf.float32)
filter_tensor = tf.random.uniform(shape=(3, 3, 1, 1), minval=0, maxval=1, dtype=tf.float32)

# Define the strides and padding
strides = [1, 2, 2, 1]
padding = 'SAME'

# Use the Conv2D operation
conv2d_result = tf.raw_ops.Conv2D(
    input=input_tensor,
    filter=filter_tensor,
    strides=strides,
    padding=padding,
    data_format="NHWC"
)

# Print the result
print(conv2d_result)

# Alternatively, you can use the tf.nn.conv2d function which is a wrapper around the Conv2D operation
conv2d_result_tf = tf.nn.conv2d(
    input=input_tensor,
    filters=filter_tensor,
    strides=strides,
    padding=padding
)

# Print the result
print(conv2d_result_tf)
