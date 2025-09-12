import tensorflow as tf

# Define a scope for our variables
with tf.variable_scope('MyScope'):

    # Create a tf.Variable
    var1 = tf.get_variable('var1', shape=[10], initializer=tf.random_normal_initializer())

    # Create another tf.Variable
    var2 = tf.get_variable('var2', shape=[10], initializer=tf.random_normal_initializer())

# Now all the tf.Variables created under the scope 'MyScope' will have the layout applied
print(var1.shape)  # -> (10,)
print(var2.shape)  # -> (10,)
