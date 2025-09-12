import tensorflow as tf

def maxpool_grad(input, grad, ksize, strides, padding, data_format='NHWC'):
    # Compute the forward pass of max pooling
    with tf.name_scope('maxpool_grad'):
        input_shape = tf.shape(input)
        grad_shape = tf.shape(grad)

        # Determine the output shape of the max pooling operation
        if data_format == 'NHWC':
            output_shape = [input_shape[0], grad_shape[1], grad_shape[2], input_shape[3]]
        else:  # NCHW
            output_shape = [input_shape[0], input_shape[1], grad_shape[2], grad_shape[3]]

        # Perform the max pooling operation
        maxpool_output = tf.nn.max_pool(input, ksize=ksize, strides=strides, padding=padding, data_format=data_format)

        # Compute the gradient of the max pooling operation
        grad_output = tf.nn.max_pool_with_argmax(input, ksize=ksize, strides=strides, padding=padding, data_format=data_format)
        argmax = grad_output.argmax

        # Create a tensor of zeros with the same shape as the input
        grad_input = tf.zeros_like(input)

        # Use scatter_nd to place the gradients at the correct locations
        updates = tf.ones_like(grad)
        indices = tf.stack([tf.range(tf.shape(argmax)[0])[:, tf.newaxis, tf.newaxis, tf.newaxis],
                            tf.unstack(argmax, axis=3)], axis=4)
        grad_input = tf.tensor_scatter_nd_add(grad_input, indices, updates)

        return grad_input

# Example usage
input_tensor = tf.random.normal([1, 28, 28, 1])
grad_tensor = tf.random.normal([1, 14, 14, 1])
ksize = [1, 2, 2, 1]
strides = [1, 2, 2, 1]
padding = 'SAME'

grad_input = maxpool_grad(input_tensor, grad_tensor, ksize, strides, padding)
print(grad_input)
