import tensorflow as tf

def quantized_mul(x, y):
    # Prepare the quantized buffers
    x_min, x_max = tf.reduce_min(x), tf.reduce_max(x)
    y_min, y_max = tf.reduce_min(y), tf.reduce_max(y)
    x_range, y_range = x_max - x_min, y_max - y_min
    x_scale, y_scale = 255 / x_range, 255 / y_range
    x_quantized = tf.cast(tf.round(x * x_scale) - tf.round(x_min * x_scale), dtype=tf.qint32)
    y_quantized = tf.cast(tf.round(y * y_scale) - tf.round(y_min * y_scale), dtype=tf.qint32)

    # Perform quantized multiplication
    result_quantized = tf.raw_ops.QuantizedMul(x=x_quantized, y=y_quantized,
                                               min_x=x_min, max_x=x_max,
                                               min_y=y_min, max_y=y_max)

    # Dequantize the result
    result_dequantized = tf.cast(result_quantized, dtype=tf.float32) / (x_scale * y_scale)

    return result_dequantized
