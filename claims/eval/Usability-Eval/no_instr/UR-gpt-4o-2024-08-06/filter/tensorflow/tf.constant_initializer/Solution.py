import tensorflow as tf

# Define the shape and value of the constant tensor
shape = (3, 3)
value = 42.0

# Create a Constant Initializer with the specified value
constant_initializer = tf.constant_initializer(value)

# Use the initializer to create a tensor
constant_tensor = constant_initializer(shape=shape, dtype=tf.float32)

# Print the created constant tensor
print("Constant Tensor:\n", constant_tensor)
