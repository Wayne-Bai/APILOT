import tensorflow as tf

# Create a constant tensor from a tensor-like object
tensor_like_object = tf.constant([1.0, 2.0, 3.0])

constant_tensor = tf.constant(tensor_like_object)
constant_tensor
