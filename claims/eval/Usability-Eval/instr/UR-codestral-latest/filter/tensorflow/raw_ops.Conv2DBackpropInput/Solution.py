import tensorflow as tf

def compute_conv2d_gradient(input_tensor, filter_tensor):
    # Define the input and filter tensors
    input_tensor = tf.constant(input_tensor, dtype=tf.float32)
    filter_tensor = tf.constant(filter_tensor, dtype=tf.float32)

    # Use tf.GradientTape to record the operations for automatic differentiation
    with tf.GradientTape() as g:
        g.watch(input_tensor)
        # Compute the convolution
        conv = tf.nn.conv2d(input_tensor, filter_tensor, strides=1, padding='SAME')

    # Compute the gradient with respect to the input
    grad = g.gradient(conv, input_tensor)

    return grad
