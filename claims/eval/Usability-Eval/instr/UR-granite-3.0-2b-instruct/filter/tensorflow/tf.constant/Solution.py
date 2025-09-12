import tensorflow as tf

# Create a tensor-like object
tensor_like_object = tf.constant([[1, 2, 3], [4, 5, 6]])

# Create a constant tensor from the tensor-like object
constant_tensor = tf.constant(tensor_like_object)

# Print the constant tensor
print(constant_tensor)
