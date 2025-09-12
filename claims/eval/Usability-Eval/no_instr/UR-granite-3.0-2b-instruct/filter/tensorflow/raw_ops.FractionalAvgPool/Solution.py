import tensorflow as tf

# Define the fractional average pooling operation
def fractional_avg_pool(input, pool_size, stride, fractional_stride):
    # Create a fractional average pooling layer
    layer = tf.raw_ops.FractionalAveragePool(input, pool_size, stride, fractional_stride)

    # Perform the fractional average pooling operation
    output = layer

    return output
