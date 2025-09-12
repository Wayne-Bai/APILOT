import tensorflow as tf

def quantized_mul(x, y):
    x_min = tf.reduce_min(x)
    x_max = tf.reduce_max(x)
    y_min = tf.reduce_min(y)
    y_max = tf.reduce_max(y)

    scale_x = (x_max - x_min) / 255.0
    scale_y = (y_max - y_min) / 255.0

    x_quant = tf.quantization.quantize_and_dequantize(x, scale_x, 0, tf.uint8)
    y_quant = tf.quantization.quantize_and_dequantize(y, scale_y, 0, tf.uint8)

    return tf.quantization.quantize_and_dequantize(x_quant * y_quant, scale_x * scale_y, 0, tf.uint8)
