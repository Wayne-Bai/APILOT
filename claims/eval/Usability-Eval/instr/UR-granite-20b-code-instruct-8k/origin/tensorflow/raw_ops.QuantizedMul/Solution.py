import tensorflow as tf
x = tf.placeholder(tf.float32, shape=(2, 2))
y = tf.placeholder(tf.float32, shape=(2, 2))
z = tf.multiply(x, y)

with tf.Session() as sess:
    # Run the initializer to initialize x and y.
    sess.run(tf.global_variables_initializer(), feed_dict={x:[[1,2],[3,4]], y:[[5,6],[7,8]]})
    print(sess.run(z))
