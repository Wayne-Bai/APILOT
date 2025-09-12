import tensorflow as tf

def max_pool_grad(orig_input, orig_output, out_backprop):
    """
    Computes gradients of the maxpooling function.

    Parameters:
        orig_input (Tensor): Original input tensor.
        orig_output (Tensor): Original output tensor.
        out_backprop (Tensor): Output gradient tensor.

    Returns:
        Tensor: Gradient of the maxpooling function.
    """

    with tf.GradientTape() as tape:
        pool = tf.nn.max_pool(orig_input, ksize=3, strides=2, padding='SAME')
        
        # Compute gradients of the output with respect to the input
        grads = tape.gradient(pool, orig_input, output_gradients=out_backprop)

    return grads

# Define some example inputs
input_tensor = tf.constant([1, 2, 3, 4, 5, 6, 7, 8, 9], shape=[1, 3, 3, 1])
output_tensor = tf.nn.max_pool(input_tensor, ksize=3, strides=2, padding='SAME')
output_backprop = tf.constant([1, 1])

# Compute the gradient of the maxpooling function
gradient = max_pool_grad(input_tensor, output_tensor, output_backprop)

print(gradient)
