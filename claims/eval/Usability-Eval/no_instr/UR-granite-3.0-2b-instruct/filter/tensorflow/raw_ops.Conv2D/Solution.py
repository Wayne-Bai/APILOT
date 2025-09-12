import tensorflow as tf

# Define the input tensor
input_tensor = tf.placeholder(tf.float32, shape=(None, None, 3, 3))

# Define the filter tensor
filter_tensor = tf.placeholder(tf.float32, shape=(3, 3, 1, 1))

# Compute the 2-D convolution
conv2d = tf.raw_ops.Conv2D(input_tensor, filter_tensor, strides=[1, 1, 1, 1], padding='SAME')

# Create a session and run the computation
with tf.Session() as sess:
    result = sess.run(conv2d, feed_dict={input_tensor: np.random.rand(1, 16, 16, 3), filter_tensor: np.random.rand(3, 3, 1, 1)})
