import tensorflow as tf

def max_pool_grad(input_grad, input, pool_size, strides, padding, data_format):
    """Computes gradients of the maxpooling function.

    Args:
        input_grad: The gradient of the maxpooling operation.
        input: The input to the maxpooling operation.
        pool_size: The size of the pooling window.
        strides: The stride of the pooling operation.
        padding: The padding type to be applied.
        data_format: The data format of the input.

    Returns:
        The gradient of the maxpooling operation.
    """
    # Calculate the indices of the maximum values in the input.
    max_indices = tf.argmax(input, axis=None, output_type=tf.int32)

    # Calculate the gradients of the maxpooling operation.
    grad = tf.gather_nd(input_grad, max_indices, batch_dims=0)

    # Reshape the gradients to match the shape of the input.
    grad = tf.reshape(grad, input.shape)

    return grad
