import tensorflow as tf

def compute_gradients(input_val, filter_val, out_backprop, strides, padding):
    # Define the gradient computation operation
    gradients = tf.gradients(tf.nn.conv2d(input_val, filter_val, strides, padding), [filter_val])

    # Create a TensorFlow session to run the computation
    with tf.Session() as sess:
        gradients_val = sess.run(gradients, feed_dict={input_val: your_input_value, filter_val: your_filter_value, out_backprop: your_out_backprop_value})

    return gradients_val
