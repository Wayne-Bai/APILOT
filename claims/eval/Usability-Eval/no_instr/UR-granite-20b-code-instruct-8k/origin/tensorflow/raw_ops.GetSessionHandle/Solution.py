import tensorflow as tf

# Create a tensor
tensor = tf.constant([1.0, 2.0, 3.0])

# Store the tensor in the state of the current session
session = tf.compat.v1.Session()
session.run(tf.compat.v1.global_variables_initializer())

# Create a handle to the tensor's value
tensor_handle = session.run(tf.compat.v1.get_variable_handle('tensor', initializer=tensor))
