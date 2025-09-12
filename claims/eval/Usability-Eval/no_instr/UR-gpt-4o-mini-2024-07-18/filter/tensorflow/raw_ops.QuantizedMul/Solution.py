import tensorflow as tf

def quantized_elementwise_multiply(x, y, x_min, x_max, y_min, y_max):
    # Ensure input tensors are quantized
    x_quantized = tf.quantization.quantize(x, x_min, x_max, tf.qint8)
    y_quantized = tf.quantization.quantize(y, y_min, y_max, tf.qint8)

    # Element-wise multiplication of quantized tensors
    result_quantized = tf.raw_ops.Mul(x=x_quantized, y=y_quantized)

    # Dequantizing the result
    return tf.quantization.dequantize(result_quantized, x_min, x_max)

# Example usage
x = tf.constant([[1, 2], [3, 4]], dtype=tf.float32)
y = tf.constant([[5, 6], [7, 8]], dtype=tf.float32)

result = quantized_elementwise_multiply(x, y, x_min=0.0, x_max=8.0, y_min=0.0, y_max=8.0)
print(result)
