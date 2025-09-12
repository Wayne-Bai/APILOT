import tensorflow as tf

# Using a variable scope to apply settings to all variables created within this scope
with tf.variable_scope("scope", reuse=tf.AUTO_REUSE) as scope:
    # Creating some variables under the defined scope
    var1 = tf.get_variable(name="var1", shape=[2, 2], initializer=tf.zeros_initializer())
    var2 = tf.get_variable(name="var2", shape=[3, 3], initializer=tf.ones_initializer())

# To see the result, let's run a session and initialize and print these variables
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    print("var1: ", sess.run(var1))
    print("var2: ", sess.run(var2))
