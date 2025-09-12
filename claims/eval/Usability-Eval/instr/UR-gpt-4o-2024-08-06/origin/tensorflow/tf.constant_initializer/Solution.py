import tensorflow as tf

# Initialize a constant tensor with the value of 5
constant_initializer = tf.constant_initializer(5.0)

# Create a variable using the constant initializer
variable = tf.Variable(
    initial_value=constant_initializer(shape=[3, 3], dtype=tf.float32)
)

# Display the initialized tensor
print(variable)
