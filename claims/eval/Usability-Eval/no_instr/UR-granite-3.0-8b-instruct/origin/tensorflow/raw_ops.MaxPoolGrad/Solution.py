import tensorflow as tf

@tf.custom_gradient
def maxpooling_grad(x, pool_size, strides, padding):
    def grad(dy):
        # Compute gradients of the maxpooling function
        # ...
        return grad_x, grad_pool_size, grad_strides, grad_padding

    return x, grad
