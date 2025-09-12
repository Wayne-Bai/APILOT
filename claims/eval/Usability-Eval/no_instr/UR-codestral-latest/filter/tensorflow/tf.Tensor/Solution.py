import tensorflow as tf

# Define a multidimensional tensor
# Here is an example of a 2D tensor
tensor_2d = tf.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Define a 3D tensor
# Here is an example of a 3D tensor with shape 2x3x4
tensor_3d = tf.ones([2, 3, 4])

# Print the tensors to see the multidimensional arrays
print("2D tensor:")
print(tensor_2d)
print("\n3D tensor:")
print(tensor_3d)
