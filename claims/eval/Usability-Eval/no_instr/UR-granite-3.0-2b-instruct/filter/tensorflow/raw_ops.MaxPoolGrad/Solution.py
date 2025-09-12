import tensorflow as tf
from tensorflow.python.ops import gen_math_ops

def max_pool_grad(dy, dy_grad, y, y_grad, pool_size, stride):
    """Computes gradients of the maxpooling function.

    Args:
    dy: The gradient of the output with respect to the output.
    dy_grad: The gradient of the output with respect to the input.
    y: The input to the maxpooling operation.
    y_grad: The gradient of the input with respect to the output.
    pool_size: The size of the pooling window.
    stride: The stride of the pooling operation.

    Returns:
    The gradient of the input with respect to the input.
    """
    # Compute the indices of the maximum values in the pooling window.
    max_indices = tf.argmax(y, dimension=2)

    # Compute the gradient of the output with respect to the max indices.
    dy_grad_max_indices = tf.reduce_sum(dy_grad * tf.one_hot_encoding(max_indices, depth=pool_size**2), axis=1)

    # Compute the gradient of the input with respect to the max indices.
    dy_grad_max_indices_grad = tf.reduce_sum(dy_grad_max_indices * y_grad, axis=1)

    # Compute the gradient of the input with respect to the input.
    dy_grad_input = tf.zeros_like(y)
    for i in range(pool_size**2):
        dy_grad_input += dy_grad_max_indices_grad[i] * y_grad[i]

    return dy_grad_input
