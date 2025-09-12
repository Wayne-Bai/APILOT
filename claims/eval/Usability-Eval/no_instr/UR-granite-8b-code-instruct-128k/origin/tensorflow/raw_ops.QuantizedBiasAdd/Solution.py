
import tensorflow as tf

# Create a placeholder for the input tensor
input = tf.placeholder(tf.float32, shape=(10, 10))

# Create a placeholder for the bias tensor
bias = tf.placeholder(tf.float32, shape=(10,))

# Add the bias to the input tensor
output = tf.raw_ops. biasAdd(input=input, bias=bias)

# Initialize the variables
init = tf.global_variables_initializer()

# Create a TensorFlow session
with tf.Session() as sess:
    # Run the session and print the output
    sess.run(init)
    print(sess.run(output, feed_dict={input: [[1.0, 2.0], [3.0, 4.0]], bias: [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]}))
