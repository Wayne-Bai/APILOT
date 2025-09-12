import tensorflow as tf

# Define the input and filter tensors
input = tf.constant([[[[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]]]], dtype=tf.float32)
filter = tf.constant([[[[1.0, 0.0, -1.0], [0.0, 0.0, 0.0], [-1.0, -0.0, 1.0]]]], dtype=tf.float32)

# Use the tf.raw_ops.Conv2D function to compute the convolution
output = tf.raw_ops.Conv2D(
    input=input,
    filter=filter,
    strides=[1, 1, 1, 1],
    padding="SAME",
    data_format="NHWC",
    dilations=[1, 1, 1, 1],
    name="conv2d"
)

# Print the output tensor
print(output)
