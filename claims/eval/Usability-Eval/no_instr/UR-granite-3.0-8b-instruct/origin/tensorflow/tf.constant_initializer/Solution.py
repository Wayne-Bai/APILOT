import tensorflow as tf

# Create a constant initializer with value 1.0
constant_initializer = tf.constant_initializer(1.0)

# Create a constant tensor with shape (2, 3) using the initializer
constant_tensor = tf.Variable(constant_initializer(shape=(2, 3)), dtype=tf.float32)

# Print the tensor
print(constant_tensor)
