import tensorflow as tf

# Assume 'x' is a tensor-like object
x = tf.constant([1, 2, 3, 4])

# Create a constant tensor directly from the tensor-like object
constant_tensor = tf.constant(x)

print(constant_tensor)
