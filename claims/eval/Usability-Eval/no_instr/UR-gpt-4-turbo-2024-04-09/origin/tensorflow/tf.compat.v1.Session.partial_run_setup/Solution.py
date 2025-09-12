import tensorflow as tf

# Define the graph
a = tf.placeholder(dtype=tf.float32, shape=(), name='input_a')
b = tf.placeholder(dtype=tf.float32, shape=(), name='input_b')
c = tf.add(a, b, name='add_c')
d = tf.multiply(a, b, name='multiply_d')
e = tf.subtract(c, d, name='subtract_e')

# Start a session
sess = tf.compat.v1.Session()

# Setup the parts of the graph that will be executed in parts
handle = sess.partial_run_setup([c, e], [a, b])

# Execute part 1
result_c = sess.partial_run(handle, c, feed_dict={a: 3, b: 4})
print("Result of c (a + b):", result_c)

# Execute part 2
result_e = sess.partial_run(handle, e)
print("Result of e (c - d):", result_e)

# Close the session
sess.close()
