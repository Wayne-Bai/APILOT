import tensorflow as tf

with tf.variable_scope("example_scope"):
    variable1 = tf.Variable(initial_value=1.0, name="variable1")
    variable2 = tf.Variable(initial_value=2.0, name="variable2")
    # Apply the layout to all the tf.Variables created under the scope.
