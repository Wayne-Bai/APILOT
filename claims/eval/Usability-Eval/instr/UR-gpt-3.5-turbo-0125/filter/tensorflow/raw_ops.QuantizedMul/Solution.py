
import tensorflow as tf

def quantized_multiply(x, y, min_x, max_x, min_y, max_y, out_type=tf.int32):
    x_scale = (max_x - min_x) / (2**8 - 1)
    x_zero_point = tf.cast(0 - min_x / x_scale, tf.int32)
    y_scale = (max_y - min_y) / (2**8 - 1)
    y_zero_point = tf.cast(0 - min_y / y_scale, tf.int32)
    
    x = tf.quantize(x, x_scale, x_zero_point, out_type=out_type)
    y = tf.quantize(y, y_scale, y_zero_point, out_type=out_type)
    result = tf.raw_ops.QuantizedMul(x=x, y=y)
    
    return result

# Example usage:
x = tf.constant([1.5, 2.3, 3.1, 4.5], dtype=tf.float32)
y = tf.constant([0.5, 1.0, 1.5, 2.0], dtype=tf.float32)
min_x = tf.reduce_min(x)
max_x = tf.reduce_max(x)
min_y = tf.reduce_min(y)
max_y = tf.reduce_max(y)

result = quantized_multiply(x, y, min_x, max_x, min_y, max_y)
