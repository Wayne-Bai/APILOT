import tensorflow as tf

# Define the computation graph
a = tf.constant(2, name='a')
b = tf.constant(3, name='b')
c = tf.add(a, b, name='add')  # c = a + b
d = tf.multiply(c, a, name='multiply')  # d = c * a

# Create a session
with tf.Session() as sess:
    # Partial run by specifying which operations to run
    fetches = [c, d]
    result_c, result_d = sess.run(fetches)
    
    print("Result of c (a + b):", result_c)
    print("Result of d (c * a):", result_d)
