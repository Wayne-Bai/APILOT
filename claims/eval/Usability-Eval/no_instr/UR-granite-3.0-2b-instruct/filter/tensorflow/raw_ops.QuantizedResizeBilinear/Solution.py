import tensorflow as tf

# Define the input and output tensors
input_tensor = tf.placeholder(tf.float32, shape=[None, None, None, 1])
output_tensor = tf.raw_op.resize_quantized(input_tensor, [new_height, new_width], interpolation='BILINEAR')

# Create a session and run the operation
with tf.Session() as sess:
    result = sess.run(output_tensor, feed_dict={input_tensor: input_image})
