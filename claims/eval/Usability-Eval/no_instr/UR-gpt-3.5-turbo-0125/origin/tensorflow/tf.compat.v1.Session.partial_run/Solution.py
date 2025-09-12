import tensorflow as tf

# Define computational graph
x = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32)
z = x + y

# Create a session and run the computational graph
with tf.Session() as sess:
    # Feed data to placeholders using feed_dict
    output = sess.run(z, feed_dict={x: 5.0, y: 3.0})
    print(output)
    
    # Continue the execution with more feeds and fetches
    output2 = sess.run(z, feed_dict={x: 2.0, y: 4.0})
    print(output2)
