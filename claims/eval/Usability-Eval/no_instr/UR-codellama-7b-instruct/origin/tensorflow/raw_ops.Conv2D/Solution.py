
import tensorflow as tf

# Create the tensors for the input and filter
input_tensor = tf.constant([[1., 2., 3.], [4., 5., 6.]])
filter_tensor = tf.constant([[0.5, 1.5], [2., -1.]])

# Perform the convolution using raw ops
output = tf.raw_ops.Conv2D(input=input_tensor, filter=filter_tensor)

# Print the output
print(output)
