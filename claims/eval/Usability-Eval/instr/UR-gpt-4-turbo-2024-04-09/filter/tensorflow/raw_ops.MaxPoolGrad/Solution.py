import tensorflow as tf

def maxpool_grad(orig_input, orig_output, grad, ksize, strides, padding):
    """
    Compute the gradient for max pooling on the input.

    Parameters:
    - orig_input: the original input tensor to the max pooling layer.
    - orig_output: the output tensor of the max pooling layer.
    - grad: gradient of the cost function with respect to the output of the max pooling layer.
    - ksize: the size of the window for each dimension of the input tensor.
    - strides: the stride of the sliding window for each dimension of the input tensor.
    - padding: a string, either 'VALID' or 'SAME'.

    Returns:
    - Tensor: gradients with respect to the input to the max pooling operation.
    """
    return tf.raw_ops.MaxPoolGrad(
        orig_input=orig_input,
        orig_output=orig_output,
        grad=grad,
        ksize=ksize,
        strides=strides,
        padding=padding
    )

# Example usage:
with tf.GradientTape() as tape:
    # Create a sample input (e.g., an image in batch)
    input_tensor = tf.random.normal([1, 4, 4, 3])  # Batch of 1, 4x4 size, 3 channels
    tape.watch(input_tensor)
    
    # Perform max pooling operation
    pooled = tf.nn.max_pool(input_tensor, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='VALID')
    
# Compute the gradient of some cost (e.g., sum of pooled output) with respect to the original input
grads = tape.gradient(pooled, input_tensor)

# Use the custom function for max pooling gradients
max_pool_gradients = maxpool_grad(input_tensor, pooled, grads, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='VALID')

print("Max Pooling Gradients:")
print(max_pool_gradients)
