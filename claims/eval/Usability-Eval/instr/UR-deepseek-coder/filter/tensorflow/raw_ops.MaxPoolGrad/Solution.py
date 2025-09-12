import tensorflow as tf

def maxpool_grad(input, grad, ksize, strides, padding, data_format='NHWC'):
    # Compute the indices of the maximum values in the input tensor
    _, argmax = tf.nn.max_pool_with_argmax(input, ksize=ksize, strides=strides, padding=padding, data_format=data_format)
    
    # Reshape the gradient tensor to match the shape of the input tensor
    grad = tf.reshape(grad, [-1])
    
    # Gather the gradients using the indices from the maxpool operation
    grad_flat = tf.gather(grad, argmax)
    
    # Reshape the gathered gradients back to the original input shape
    grad_output = tf.reshape(grad_flat, tf.shape(input))
    
    return grad_output

# Example usage:
# input_tensor = ...
# grad_tensor = ...
# ksize = [1, 2, 2, 1]
# strides = [1, 2, 2, 1]
# padding = 'SAME'
# result = maxpool_grad(input_tensor, grad_tensor, ksize, strides, padding)
