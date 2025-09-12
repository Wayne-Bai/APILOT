import tensorflow as tf

# Define a simple computational graph
a = tf.constant(5, name='a')
b = tf.constant(3, name='b')
c = tf.multiply(a, b, name='c')
d = tf.add(a, b, name='d')
e = tf.multiply(c, d, name='e')

# Execute the operations in the graph with partial run
with tf.compat.v1.Session() as sess:
    # Convert session to interactive session to allow partial run
    handle = sess.partial_run_setup([e], [a, b, c, d])

    # Execute the partial graph up to operation 'c'
    # Feed the values of tensor 'a' and 'b'
    c_val = sess.partial_run(handle, c, feed_dict={a: 5, b: 3})
    
    # Use the computed value 'c_val' in future computations
    result = sess.partial_run(handle, e, feed_dict={d: c_val + b.eval()})

    print(f"Result of the computation: {result}")
