import tensorflow as tf

def fractional_max_pool(inputs, size, strides, rates, name=None):
    """
    Performs fractional max pooling on the input tensor.

    Args:
        inputs: Input tensor.
        size: Size of the pooling window.
        strides: Stride size.
        rates: Pooling rate.
        name: Name prefix for the operation.

    Returns:
        Pooled tensor.
    """
    assert inputs.shape.ndims == 4, "Only supports inputs with four dimensions"

    # Compute stride masks
    input_shape = tf.shape(inputs)
    rates_shape = tf.concat([size, strides], axis=0)
    outputs_shape = tf.concat([
        [input_shape[i] // strides * rates]
        for i in range(input_shape.shape.size)
        if i not in [0, 2]
    ], axis=0)

    stride_mask = tf.cast(tf.tile(
        tf.expand_dims(tf.ones((size, size)), 0) * strides, outputs_shape[:2]
    ))
    rate_mask = tf.cast(tf.tile(
        tf.expand_dims(tf.ones((rates, rates)), 0) * rates, outputs_shape
    ))

    # Apply pooling
    pooled = tf.nn.max_pool_with_argmax(
        inputs,
        ksize=size,
        strides=strides,
        padding='VALID'
    )
    return pooled

# Test
input_data = tf.random.uniform(shape=[8, 8, 4, 16])
size = [2, 2]
strides = [2, 2]
rates = [1, 2], [2, 1]
pooled_data = fractional_max_pool(input_data, size, strides, rates)

print(pooled_data)
