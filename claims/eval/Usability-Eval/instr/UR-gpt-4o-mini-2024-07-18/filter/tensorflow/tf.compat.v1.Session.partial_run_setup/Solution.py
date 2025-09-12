import tensorflow as tf

# Create a simple computational graph
a = tf.constant(5, name='a')
b = tf.constant(3, name='b')
c = tf.add(a, b, name='add')

# Create a session to run the graph
with tf.compat.v1.Session() as sess:
    # Fetch the result of the addition operation
    result = sess.run(c)
    print("Result of a + b = ", result)
