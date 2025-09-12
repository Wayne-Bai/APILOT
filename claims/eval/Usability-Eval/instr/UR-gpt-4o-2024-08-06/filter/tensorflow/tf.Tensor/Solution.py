import tensorflow as tf

# Create a 3-dimensional tensor (multidimensional array) of shape (2, 3, 4)
# Initialize with random values
tensor_3d = tf.random.uniform((2, 3, 4), minval=0, maxval=10, dtype=tf.float32)

# Print the tensor
print("3D Tensor:")
print(tensor_3d)

# Create a 4-dimensional tensor of shape (3, 2, 3, 5)
tensor_4d = tf.random.uniform((3, 2, 3, 5), minval=0, maxval=10, dtype=tf.float32)

# Print the tensor
print("\n4D Tensor:")
print(tensor_4d)

# Create a tensor with specific values (example with 2x2 matrix)
tensor_specific = tf.constant([[1, 2], [3, 4]])

# Print the tensor
print("\n2D Specific Tensor:")
print(tensor_specific)
