import tensorflow as tf

# Create a tensor-like object (e.g., a list of lists)
tensor_like_object = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Convert the tensor-like object to a constant tensor
constant_tensor = tf.constant(tensor_like_object)

# Print the resulting tensor
print(constant_tensor)
