import tensorflow as tf

# Create a sample tensor
original_tensor = tf.constant([[1, 2], [3, 4]])

# Specify the tiling multiples for each dimension
multiples = [2, 3]

# Construct a tiled tensor
tiled_tensor = tf.repeat(tf.repeat(original_tensor, multiples[0], axis=0), multiples[1], axis=1)

# Print the original and tiled tensors
print("Original Tensor:")
print(original_tensor.numpy())

print("\nTiled Tensor:")
print(tiled_tensor.numpy())
