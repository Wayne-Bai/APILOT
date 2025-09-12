import tensorflow as tf

# Define the computation graph
a = tf.placeholder(tf.float32, shape=[None, 1], name='a')
b = tf.placeholder(tf.float32, shape=[None, 1], name='b')
c = tf.add(a, b, name='c')

# Initialize the session
sess = tf.Session()

# Run the initial computation with some feeds
feed_dict_1 = {a: [[1.0]], b: [[2.0]]}
result_1 = sess.run(c, feed_dict=feed_dict_1)
print("Result 1:", result_1)

# Continue the execution with more feeds
feed_dict_2 = {a: [[3.0]], b: [[4.0]]}
result_2 = sess.run(c, feed_dict=feed_dict_2)
print("Result 2:", result_2)

# Close the session
sess.close()
