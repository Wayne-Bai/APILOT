import tensorflow as tf

@tf.function
def fractional_max_pool_grad(orig_input, orig_output, rois, output_shape):
    return tf.raw_ops.FractionalMaxPoolGrad(
        orig_input=orig_input,
        orig_output=orig_output,
        rois=rois,
        output_shape=output_shape
    )

# Example usage:
# orig_input = tf.random.normal([1, 5, 5, 1])
# orig_output = tf.random.normal([1, 3, 3, 1])
# rois = tf.constant([[0, 0, 1, 1], [0, 1, 2, 2]], dtype=tf.float32)
# output_shape = tf.constant([1, 3, 3, 1], dtype=tf.int32)
# gradients = fractional_max_pool_grad(orig_input, orig_output, rois, output_shape)
