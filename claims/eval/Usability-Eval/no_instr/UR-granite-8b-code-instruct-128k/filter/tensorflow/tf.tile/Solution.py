
import tensorflow as tf

# Define the input tensor
input_tensor = tf.constant([[1, 2, 3], [4, 5, 6]])

# Define the tiling multipliers
multipliers = [2, 2]

# Construct the output tensor by tiling the input tensor
output_tensor = tf.tile(input_tensor, multipliers)

# Print the output tensor
print(output_tensor)
