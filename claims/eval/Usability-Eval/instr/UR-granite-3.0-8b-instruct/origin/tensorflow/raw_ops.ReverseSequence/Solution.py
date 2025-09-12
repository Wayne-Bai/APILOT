import tensorflow as tf

# Assuming 'input_tensor' is your input tensor
input_tensor = tf.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Reverse the slices along the last axis
reversed_tensor = tf.raw_ops.ReverseV2(input_tensor, axes=[-1])

# Print the reversed tensor
print(reversed_tensor)
