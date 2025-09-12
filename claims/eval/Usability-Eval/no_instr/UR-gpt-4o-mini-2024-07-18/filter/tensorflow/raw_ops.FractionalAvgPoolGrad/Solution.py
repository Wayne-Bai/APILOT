import tensorflow as tf

@tf.function
def fractional_avg_pool_grad(inputs, output_shape, rand_indices):
    """
    Computes the gradient of the Fractional Average Pooling operation.

    Args:
    - inputs: The input tensor (gradients of the output).
    - output_shape: The shape of the output of the Fractional Avg Pool operation.
    - rand_indices: Random indices used during pooling.

    Returns:
    - gradients: The computed gradients with respect to the input tensor.
    """
    # Reshape the input gradients according to the output shape
    reshaped_inputs = tf.reshape(inputs, output_shape)

    # Initialize the output gradients tensor
    gradients = tf.zeros_like(inputs)

    # Compute the gradients by pooling the input gradients
    for i in range(output_shape[0]):
        for j in range(output_shape[1]):
            idx = rand_indices[i, j]
            gradients = tf.tensor_scatter_nd_add(gradients, [[idx[0], idx[1]]], reshaped_inputs[i, j:j+1])

    return gradients
