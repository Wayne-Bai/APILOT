import tensorflow as tf

def conv2d_gradients(input_tensor, filter_tensor, out_backprop):
    # Compute the gradients of convolution with respect to the input
    gradients = tf.raw_ops.Conv2dBackpropInput(
        input_shape=input_tensor.shape,
        filter=filter_tensor,
        out_backprop=out_backprop,
        strides=tf.constant([1, 1, 1, 1], dtype=tf.int32),
        padding='SAME'
    )
    return gradients
