import tensorflow as tf

# Create a TensorFlow variable
variable = tf.Variable([[1.0, 2.0], [3.0, 4.0]])

# Define sparse indices and updates
indices = tf.constant([[0], [1]])
updates = tf.constant([[5.0, 6.0], [7.0, 8.0]])

# Perform scattered update to the variable
updated_variable = tf.tensor_scatter_nd_update(variable, indices, updates)

tf.print("Updated Variable:", updated_variable)
