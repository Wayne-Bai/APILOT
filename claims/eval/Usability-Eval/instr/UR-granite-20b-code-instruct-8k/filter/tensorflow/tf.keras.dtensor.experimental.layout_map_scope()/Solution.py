import tensorflow as tf

with tf.variable_scope("foo"):
    var1 = tf.get_variable("var1", [1, 10])
    var2 = tf.get_variable("var2", [10, 10])

# Apply the layout to all the tf.Variables created under the scope
for v in tf.global_variables():
    v._set_initial_value(tf.Variable(v.initialized_value(), trainable=False))
