import tensorflow as tf

# Create a constant tensor from a tensor-like object, which could be a list or a numpy array
tensor_like_object = [1, 2, 3, 4, 5]

# Convert the tensor-like object to a constant tensor
constant_tensor = tf.constant(tensor_like_object)

# Print the constant tensor
print("Constant Tensor:")
print(constant_tensor)
