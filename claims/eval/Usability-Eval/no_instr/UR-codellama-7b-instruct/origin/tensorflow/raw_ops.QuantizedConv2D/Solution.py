
import tensorflow as tf

# Create input and filter tensors
input_tensor = tf.constant([[1, 2, 3], [4, 5, 6]])
filter_tensor = tf.constant([[1, 0], [-1, 0], [0, 1]])

# Perform the convolution using the raw_ops method
conv_op = tf.raw_ops.Conv2D(
    input=input_tensor,
    filter=filter_tensor,
    strides=[1, 1, 1, 1],
    padding="SAME"
)

# Print the output of the convolution
print(conv_op)
