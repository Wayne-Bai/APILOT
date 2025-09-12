import tensorflow as tf

# Create a variable scope
with tf.variable_scope('my_scope'):
    # Create some variables
    var1 = tf.Variable(1.0, name='var1')
    var2 = tf.Variable(2.0, name='var2')
    var3 = tf.Variable(3.0, name='var3')

    # Apply layout to all the variables
    var1.set_shape([None, 1])
    var2.set_shape([1, None])
    var3.set_shape([1, 1])

# Print the shapes of the variables
print(var1.shape)
print(var2.shape)
print(var3.shape)
