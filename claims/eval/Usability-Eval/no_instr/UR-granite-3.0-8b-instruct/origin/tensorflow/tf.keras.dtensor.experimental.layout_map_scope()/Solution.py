import tensorflow as tf

# Define a scope
with tf.name_scope('my_scope'):
    # Create variables under this scope
    var1 = tf.Variable(tf.random.normal([3, 3]), name='var1')
    var2 = tf.Variable(tf.random.normal([3, 3]), name='var2')

    # Apply layout to all variables under this scope
    layout = tf.layout.Layout(var1, var2)

    # Print the layout
    print(layout)
