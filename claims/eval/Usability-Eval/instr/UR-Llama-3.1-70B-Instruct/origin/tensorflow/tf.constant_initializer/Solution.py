# Import necessary libraries
import tensorflow as tf

# Initialize a session
sess = tf.compat.v1.Session()

# Create a constant initializer
constant_initializer = tf.compat.v1.constant_initializer(value=1.0)

# Initialize a variable with constant initializer
var = tf.compat.v1.get_variable(name="var", shape=[2, 2], initializer=constant_initializer)

# Initialize variables
sess.run(tf.compat.v1.global_variables_initializer())

# Print the variable
print(sess.run(var))

# Output: [[1. 1.]
#          [1. 1.]]

# We can also directly create a constant tensor using tf.constant
constant_tensor = tf.constant([[1.0, 1.0], [1.0, 1.0]])

# Print the constant tensor
print(sess.run(constant_tensor))

# Output: [[1. 1.]
#          [1. 1.]]

# Close the session
sess.close()
