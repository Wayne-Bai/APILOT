import tensorflow as tf

# Create a constant tensor from a tensor-like object
tensor_like_object = [1.0, 2.0, 3.0, 4.0]
constant_tensor = tf.constant(tensor_like_object)

# Print the constant tensor
print(constant_tensor)
