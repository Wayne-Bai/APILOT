import tensorflow as tf

# Example tensor-like object
tensor_like_object = tf.constant([1.0, 2.0, 3.0])

# Create a constant tensor from the tensor-like object
constant_tensor = tf.constant(tensor_like_object)

print(constant_tensor)
