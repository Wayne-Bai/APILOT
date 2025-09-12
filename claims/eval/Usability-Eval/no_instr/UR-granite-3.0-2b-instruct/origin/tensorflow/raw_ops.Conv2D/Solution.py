import tensorflow as tf

# Define the input and filter tensors
input_tensor = tf.random.normal([1, 10, 10, 3])  # 4-D input tensor
filter_tensor = tf.random.normal([3, 3, 3, 1])  # 4-D filter tensor

# Compute the 2-D convolution
output_tensor = tf.raw_ops.Conv2D(input=input_tensor, filter=filter_tensor, strides=[1, 1, 1, 1], padding='SAME')

# Print the output tensor
print(output_tensor)
