import tensorflow as tf

# Create a custom scope to apply layout to variables
def custom_scope(value, shape, name=None):
    with tf.name_scope(name):
        var = tf.Variable(value, shape=shape)
        tf.add_to_collection('custom_scope_vars', var)

# Here is how you can use this scope
with tf.compat.v1.Session() as sess:
    W = custom_scope(tf.zeros([784, 10]), [784, 10], name="Weights")
    b = custom_scope(tf.zeros([10]), [10], name="Biases")
    sess.run(tf.global_variables_initializer())
