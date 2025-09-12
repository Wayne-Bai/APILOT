import tensorflow as tf

# Define a sample tensor
input_tensor = tf.constant([[1, 2], [3, 4]])

# Specify the number of times to replicate the tensor along each axis
multiples = [2, 3]

# Create a tiled version of the input tensor
tiled_tensor = tf.repeat(input_tensor, repeats=multiples[1], axis=1)
tiled_tensor = tf.repeat(tiled_tensor, repeats=multiples[0], axis=0)

print(tiled_tensor.numpy())
