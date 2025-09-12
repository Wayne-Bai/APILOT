import tensorflow as tf

# Creating a constant tensor from a tensor-like object
tensor_like_object = [1, 2, 3]  # Example tensor-like object can be a list, tuple, etc.
constant_tensor = tf.constant(tensor_like_object)

print("Constant Tensor:", constant_tensor)
