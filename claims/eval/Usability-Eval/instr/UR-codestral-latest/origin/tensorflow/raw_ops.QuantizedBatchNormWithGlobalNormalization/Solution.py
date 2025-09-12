import tensorflow as tf

def quantized_batch_normalization(inputs, mean, variance, offset, scale, variance_epsilon):
    # Normalize the inputs
    normalized_inputs = tf.raw_ops.BatchNormWithGlobalNormalization(
        t=inputs,
        m=mean,
        v=variance,
        beta=offset,
        gamma=scale,
        variance_epsilon=variance_epsilon)

    # Define the quantization parameters
    min_value = tf.reduce_min(normalized_inputs)
    max_value = tf.reduce_max(normalized_inputs)
    num_bits = 8

    # Quantize the inputs
    normalized_inputs = tf.raw_ops.QuantizeV2(
        input=normalized_inputs,
        min_range=min_value,
        max_range=max_value,
        T=tf.uint8)

    # Dequantize the inputs
    normalized_inputs = tf.raw_ops.Dequantize(
        input=normalized_inputs,
        min_range=min_value,
        max_range=max_value,
        mode="MIN_COMBINED")

    return normalized_inputs
