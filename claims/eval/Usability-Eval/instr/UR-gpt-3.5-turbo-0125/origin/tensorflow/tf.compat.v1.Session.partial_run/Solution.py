
import tensorflow as tf

# Create a placeholder for input
input_placeholder = tf.placeholder(tf.float32, shape=[None])

# Create a constant tensor
constant_tensor = tf.constant(5.0)

# Define the operation to multiply input and constant
output_tensor = input_placeholder * constant_tensor

# Create a session
with tf.Session() as sess:
    # Feed the input and fetch the output
    output_result = sess.run(output_tensor, feed_dict={input_placeholder: [1.0, 2.0, 3.0]})
    print(output_result)
