import tensorflow as tf

def max_pool_with_argmax(input_tensor, pool_size, strides, padding='VALID'):
    # Apply max pooling with argmax to return both the output and indices
    pooled_output, argmax_indices = tf.nn.max_pool_with_argmax(
        input_tensor,
        ksize=pool_size,
        strides=strides,
        padding=padding
    )
    return pooled_output, argmax_indices

def compute_maxpool_gradients(grad, input_tensor, pool_size, strides, padding='VALID'):
    # Get the pooled output and argmax indices
    pooled_output, argmax_indices = max_pool_with_argmax(input_tensor, pool_size, strides, padding)

    # Create a tensor of zeros with the same shape as the input
    input_shape = tf.shape(input_tensor)
    gradients = tf.zeros_like(input_tensor)

    # Scatter the gradient from the output gradient to the location of the max values
    gradients = tf.tensor_scatter_nd_update(gradients, argmax_indices[..., tf.newaxis], grad)

    return gradients

# Example usage
input_tensor = tf.constant([[1.0, 2.0, 3.0, 4.0],
                             [5.0, 6.0, 7.0, 8.0],
                             [9.0, 10.0, 11.0, 12.0],
                             [13.0, 14.0, 15.0, 16.0]], shape=[1, 4, 4, 1])

pool_size = [1, 2, 2, 1]
strides = [1, 2, 2, 1]
padding = 'VALID'

pooled_output, argmax_indices = max_pool_with_argmax(input_tensor, pool_size, strides, padding)

# Assume the gradient from the next layer is received
grad = tf.constant([[1.0, 1.0], [1.0, 1.0]], shape=[1, 2, 2, 1])
gradients = compute_maxpool_gradients(grad, input_tensor, pool_size, strides, padding)

print("Pooled Output:", pooled_output)
print("Gradients:", gradients)
