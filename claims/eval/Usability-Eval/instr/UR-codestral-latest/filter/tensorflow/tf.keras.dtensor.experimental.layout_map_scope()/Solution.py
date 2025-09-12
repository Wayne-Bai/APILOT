import tensorflow as tf

# Define the initializer
initializer = tf.random_uniform_initializer(minval=-1.0, maxval=1.0)

# Define the variable scope
with tf.variable_scope("example", reuse=False, initializer=initializer) as scope:
    # Create a tf.Variable
    my_var = tf.get_variable("my_var", shape=[2, 2])

# Now, my_var conform to the layout defined in the initializer under the variable scope "example"
