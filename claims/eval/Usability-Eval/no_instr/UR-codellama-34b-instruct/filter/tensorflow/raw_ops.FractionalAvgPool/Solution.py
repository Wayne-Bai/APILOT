import tensorflow as tf

# Define the input tensor
input_tensor = tf.constant([[1, 2], [3, 4]])

# Perform fractional average pooling with a window size of 2 and stride 1
output = tf.raw_ops.fractional_avg_pool(
    value=input_tensor,
    window_size=(2, 2),
    stride=1
)

# Print the output tensor
print(output)
