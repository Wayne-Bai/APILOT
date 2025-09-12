
import tensorflow as tf

# Define function to compile into a callable TensorFlow graph
def my_function(x, y):
    return tf.add(tf.square(x), tf.square(y))

# Create TensorFlow graph
input_x = tf.placeholder(tf.float32)
input_y = tf.placeholder(tf.float32)
output = my_function(input_x, input_y)

# Start TensorFlow session
with tf.Session() as sess:
    result = sess.run(output, feed_dict={input_x: 3.0, input_y: 4.0})
    print(result)
