import tensorflow as tf

def compute_fractional_max_pool_gradient(grad, orig_input, pooled_output, overlaps, rand_indices, pool_size, jitter):
    """Computes the gradient of the FractionalMaxPool function.

    Args:
        grad: Gradient with respect to output of forward pass.
        orig_input: Original input to forward pass.
        pooled_output: Output of forward pass.
        overlaps: The number of overlaps for each pool region.
        rand_indices: Random indices for each pool region.
        pool_size: Size of pools.
        jitter: Jitter parameter.

    Returns:
        Gradient with respect to input of forward pass.
    """
    grad_one = tf.expand_dims(grad, 3)
    grad_one = tf.expand_dims(grad_one, 4)

    grad_all = tf.zeros_like(orig_input)
    grad_all = tf.tensor_scatter_nd_update(grad_all, tf.where(rand_indices), grad)

    pooled_output = tf.expand_dims(pooled_output, -1)

    normalized_grad = grad_all / pool_size / pool_size
    normalized_grad = tf.where(orig_input == pooled_output, normalized_grad, tf.zeros_like(orig_input))

    overlap_mask = tf.reduce_sum(overlaps, 3)
    overlap_mask = 1 - tf.floor(overlap_mask)
    overlap_mask = tf.expand_dims(overlap_mask, 2)

    grad_pool = normalized_grad * overlap_mask

    return grad_pool

# Example usage:
grad = tf.constant([1.0, 2.0, 3.0], dtype=tf.float32)
orig_input = tf.constant([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]], dtype=tf.float32)
pooled_output = tf.constant([[3.0, 6.0], [6.0, 9.0]], dtype=tf.float32)
overlaps = tf.constant([[[1.0, 2.0, 1.0], [2.0, 4.0, 2.0]]], dtype=tf.float32)
rand_indices = tf.constant([[1, 0, 1], [0, 2, 1]], dtype=tf.int32)
pool_size = tf.constant(2, dtype=tf.int32)
jitter = tf.constant(0.5, dtype=tf.float32)

grad_pool = compute_fractional_max_pool_gradient(grad, orig_input, pooled_output, overlaps, rand_indices, pool_size, jitter)
print(grad_pool)
