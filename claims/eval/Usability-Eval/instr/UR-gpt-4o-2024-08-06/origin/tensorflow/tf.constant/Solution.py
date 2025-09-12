import tensorflow as tf

# Define a tensor-like object, for example, a Python list
tensor_like_object = [[1, 2], [3, 4]]

# Create a constant tensor from the tensor-like object
constant_tensor = tf.convert_to_tensor(tensor_like_object)

# Print the constant tensor
print(constant_tensor)
