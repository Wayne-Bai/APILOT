import tensorflow as tf

def quantized_batch_norm(x, mean, variance, offset, scale, variance_epsilon):
    # Create operation constants for the QuantizedBatchNormWithGlobalNormalization operation
    input_shape = x.get_shape().as_list()
    num_channels = input_shape[-1]

    mean = tf.reshape(mean, [1, 1, 1, num_channels])
    variance = tf.reshape(variance, [1, 1, 1, num_channels])
    offset = tf.reshape(offset, [1, 1, 1, num_channels])
    scale = tf.reshape(scale, [1, 1, 1, num_channels])

    # Define the QuantizedBatchNormWithGlobalNormalization operation
    quantized_bn = tf.raw_ops.QuantizedBatchNormWithGlobalNormalization(
        inputs=x,
        mean=mean,
        variance=variance,
        offset=offset,
        scale=scale,
        variance_epsilon=variance_epsilon,
        output_dtype=tf.float32
    )

    return quantized_bn
